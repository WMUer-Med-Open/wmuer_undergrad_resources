# WMUer Undergraduate Medical Resources

> 面向医学本科生的开放资料库，以 Markdown 为主，并支持合规的 PDF 和 Word 文件。  
> An open resource library for undergraduate medical students, Markdown-first with compliant PDF and Word support.

## 中文简介

`wmuer_undergrad_resources` 是一个面向医学本科生的开放资料库，目标是用开放、可维护、可协作的方式整理医学本科阶段的学习资料。

本项目强调 **按照疾病的学习模式进行资料整合与分享**：围绕具体疾病或临床问题，把基础医学机制、病理生理、临床表现、诊断思路、治疗原则、考试重点、实习经验和推荐资料放到同一条学习路径中，帮助同学从“课程章节”走向“临床问题”。

本仓库以 Markdown 资料为主，也支持上传合规的 PDF 和 Word 文件。PDF/Word 必须是原创、明确授权或可公开再分发的资料，并需要配套 Markdown 索引说明来源、授权、适用阶段和用途。不要上传教材扫描件、学校内部课件、未授权题库、录音录像或任何含隐私的信息。

## English Overview

`wmuer_undergrad_resources` is an open resource library for undergraduate medical education, primarily maintained in Markdown with compliant PDF and Word support.

The project is organized around a **disease-based learning model**. Instead of collecting isolated course notes, it links basic mechanisms, pathophysiology, clinical manifestations, diagnostic reasoning, treatment principles, exam-focused review, internship experience, and recommended resources around diseases or clinical problems.

The repository primarily accepts Markdown files and also supports compliant PDF and Word documents. PDF/Word files must be original, clearly licensed, or publicly redistributable, and should be accompanied by a Markdown index explaining source, license, target stage, and intended use. Scanned textbooks, internal courseware, unauthorized question banks, recordings, videos, and privacy-sensitive materials are not accepted.

## Repository Structure

```text
wmuer_undergrad_resources/
  years/                    # 按年级组织的学习路径入口
  disease-based-learning/   # 以疾病和系统为中心的核心资料区
  tracks/                   # 特殊培养路径，如教改班资料
  exams/                    # 真题回忆、复习经验、题型说明和考点整理
  internship/               # 实习科室指南和经验贴
  files/                    # 合规 PDF 和 Word 文件的索引与存放说明
  templates/                # 资料条目模板
```

## Main Sections

| Section | 中文说明 | English |
|---|---|---|
| `years/` | 从大一下开始，按学习阶段整理入口和推荐路径 | Stage-based entry points from freshman spring onward |
| `disease-based-learning/` | 核心区域，按疾病或系统整合基础与临床资料 | Core disease- and system-based learning resources |
| `tracks/education-reform-class/` | 教改班相关资料、路径和经验 | Education reform track resources |
| `exams/` | 真题回忆、复习经验、题型说明、考点整理 | Exam memory notes, review guidance, formats, and key points |
| `internship/` | 实习科室指南和经验贴 | Clerkship guides and internship experience posts |
| `files/` | 合规 PDF 和 Word 文件说明、索引和存放建议 | Guidance and index for compliant PDF and Word files |
| `templates/` | 疾病笔记和资源条目模板 | Templates for disease notes and resource entries |

## How To Use

1. 如果你正在按年级学习，先进入 `years/`，从对应学期的 README 找到推荐路径。
2. 如果你想围绕某个疾病或系统复习，进入 `disease-based-learning/`。
3. 如果你准备考试，进入 `exams/` 查看复习经验、题型说明和考点整理。
4. 如果你准备实习，进入 `internship/` 查看科室指南和经验贴。
5. 如果你想投稿，先阅读 `CONTRIBUTING.md`，再使用 `templates/` 中的模板。
6. 如果你需要上传 PDF 或 Word，请先在 `files/` 建立 Markdown 索引，再提交文件本体。

## Contribution Principles

- 优先提交 `.md` 文件；合规 PDF/Word 可作为补充资料提交。
- 文件名使用小写英文、数字和连字符。
- 优先提交原创整理、公开授权资料索引、学习路径和经验总结。
- 必须说明资料来源、授权状态、适用年级和是否原创。
- 不得提交盗版教材、内部课件、未授权题库、原始试卷扫描件或含患者/教师/科室隐私的信息。
- PDF/Word 必须配套 Markdown 说明，避免仓库变成无法检索的文件堆。
- 医学内容应尽量标注更新时间，避免把过时经验写成固定结论。

## Medical Disclaimer

本资料库仅用于医学教育、课程学习和同学间经验交流，不构成医疗建议，不能替代执业医师判断、学校课程要求、医院规章制度或官方指南。任何临床相关内容都应结合最新指南、教师要求和所在机构规范进行判断。

This repository is for medical education, coursework, and peer learning only. It does not provide medical advice and must not replace licensed clinical judgment, institutional requirements, school curricula, or official guidelines.

## License

Unless otherwise stated, the original content in this repository is licensed under the Creative Commons Attribution 4.0 International License (`CC BY 4.0`).
