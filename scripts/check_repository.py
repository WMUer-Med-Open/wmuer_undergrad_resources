from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
YEARS = (
    "freshman",
    "sophomore",
    "junior",
    "senior",
    "fifth-year-internship",
)
CATEGORIES = ("summaries", "experience-posts", "documents")
CONTENT_EXTENSIONS = {".md", ".pdf", ".doc", ".docx"}
DOCUMENT_EXTENSIONS = {".pdf", ".doc", ".docx"}
BLOCKED_EXTENSIONS = {
    ".ppt",
    ".pptx",
    ".zip",
    ".rar",
    ".7z",
    ".mp3",
    ".mp4",
    ".mov",
    ".avi",
    ".mkv",
    ".wmv",
}
MAX_DOCUMENT_BYTES = 25 * 1024 * 1024
CONTENT_FILENAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.(md|pdf|doc|docx)$")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def add_error(errors: list[str], path: Path | str, message: str) -> None:
    location = rel(path) if isinstance(path, Path) else path
    errors.append(f"{location}: {message}")


def check_required_structure(errors: list[str]) -> None:
    years_root = ROOT / "years"
    if not years_root.is_dir():
        add_error(errors, "years", "missing years directory")
        return

    for year in YEARS:
        year_dir = years_root / year
        if not year_dir.is_dir():
            add_error(errors, year_dir, "missing year directory")
            continue

        if not (year_dir / "README.md").is_file():
            add_error(errors, year_dir / "README.md", "missing year README")

        for category in CATEGORIES:
            category_dir = year_dir / category
            if not category_dir.is_dir():
                add_error(errors, category_dir, "missing category directory")
                continue
            if not (category_dir / "README.md").is_file():
                add_error(errors, category_dir / "README.md", "missing category README")


def check_markdown_encoding(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        try:
            path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            add_error(errors, path, "Markdown files must be UTF-8 encoded")


def check_blocked_extensions(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() in BLOCKED_EXTENSIONS:
            add_error(errors, path, f"unsupported file type {path.suffix}")


def check_year_files(errors: list[str]) -> None:
    years_root = ROOT / "years"
    if not years_root.is_dir():
        return

    for path in years_root.rglob("*"):
        if not path.is_file():
            continue

        parts = path.relative_to(years_root).parts
        suffix = path.suffix.lower()

        if len(parts) == 1 and parts[0] == "README.md":
            continue
        if len(parts) == 2 and parts[1] == "README.md":
            continue
        if len(parts) == 3 and parts[2] == "README.md" and parts[1] in CATEGORIES:
            continue

        if len(parts) != 3:
            add_error(errors, path, "unexpected file location under years")
            continue

        year, category, filename = parts
        if year not in YEARS:
            add_error(errors, path, "unknown year directory")
        if category not in CATEGORIES:
            add_error(errors, path, "unknown category directory")

        if suffix not in CONTENT_EXTENSIONS:
            add_error(errors, path, f"unsupported content file type {suffix}")
            continue

        if not CONTENT_FILENAME_RE.match(filename):
            add_error(
                errors,
                path,
                "content filenames must use lowercase letters, numbers, and hyphens",
            )

        if suffix in DOCUMENT_EXTENSIONS:
            if category != "documents":
                add_error(errors, path, "PDF/Word files must be placed in documents/")

            companion = path.with_suffix(".md")
            if not companion.is_file():
                add_error(errors, path, "PDF/Word files need a same-name Markdown entry")

            size = path.stat().st_size
            if size > MAX_DOCUMENT_BYTES:
                add_error(errors, path, "document file is larger than 25 MB")


def check_markdown_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue

        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = match.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:", "tel:", "#")):
                continue

            target = target.split("#", 1)[0]
            if not target:
                continue

            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                add_error(errors, path, f"broken Markdown link: {target}")


def main() -> int:
    errors: list[str] = []
    check_required_structure(errors)
    check_markdown_encoding(errors)
    check_blocked_extensions(errors)
    check_year_files(errors)
    check_markdown_links(errors)

    if errors:
        print("Repository checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
