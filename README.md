# WMUer Med Open: Undergraduate Resources

> 面向医学本科生的开放资料库。按年级整理总结、经验贴和可公开分享的文档。
> An open undergraduate medical resource library organized by academic year.

## 项目定位

`wmuer_undergrad_resources` 不是网盘，也不是盗版资料搬运站。它的目标是把同学真正能复用、能维护、能追溯来源的学习资料沉淀下来。

仓库按年级组织，每个年级固定包含三类内容：

- `summaries/`：课程总结、系统总结、疾病学习总结、复习框架。
- `experience-posts/`：学习经验、考试经验、选课经验、实习经验。
- `documents/`：原创、授权或可公开再分发的 Markdown、PDF、Word 文档，以及对应说明。

医学资料不适合简单照搬计算机作业仓库的“课程项目”结构。本仓库先按学习阶段建立入口，再鼓励在具体总结中把基础机制、病理生理、临床表现、诊断思路、治疗原则、考试重点和实习经验串起来。

## 快速入口

| 年级 | 阶段定位 | 总结 | 经验贴 | 文档 |
|---|---|---|---|---|
| 大一 | 适应大学学习，建立基础医学学习方法 | [summaries](years/freshman/summaries/) | [experience-posts](years/freshman/experience-posts/) | [documents](years/freshman/documents/) |
| 大二 | 基础医学核心课程，形成机制理解 | [summaries](years/sophomore/summaries/) | [experience-posts](years/sophomore/experience-posts/) | [documents](years/sophomore/documents/) |
| 大三 | 桥接基础与临床，强化系统和疾病学习 | [summaries](years/junior/summaries/) | [experience-posts](years/junior/experience-posts/) | [documents](years/junior/documents/) |
| 大四 | 临床课程、见习、考试与病例思维 | [summaries](years/senior/summaries/) | [experience-posts](years/senior/experience-posts/) | [documents](years/senior/documents/) |
| 大五/实习 | 临床实习、轮转经验、执业考试准备 | [summaries](years/fifth-year-internship/summaries/) | [experience-posts](years/fifth-year-internship/experience-posts/) | [documents](years/fifth-year-internship/documents/) |

也可以从 [years/](years/) 查看完整年级索引。

## 如何投稿

1. 选择对应年级和类别，例如 `years/junior/summaries/`。
2. 从 [templates/](templates/) 复制合适模板。
3. 使用小写英文、数字和连字符命名，例如 `cardiovascular-physiology-review.md`。
4. 写清楚来源、授权状态、适用年级、更新时间和是否原创。
5. 提交 Pull Request，并完成隐私与版权检查。

详细规范见 [CONTRIBUTING.md](CONTRIBUTING.md)。内容质量标准见 [docs/content-standard.md](docs/content-standard.md)，版权与隐私边界见 [docs/copyright-and-privacy.md](docs/copyright-and-privacy.md)。

## 支持的文件类型

| 类型 | 是否推荐 | 要求 |
|---|---|---|
| Markdown (`.md`) | 推荐 | 最适合作为可维护的总结、经验贴和索引说明。 |
| PDF (`.pdf`) | 支持 | 必须原创、明确授权或可公开再分发，并配套 Markdown 说明。 |
| Word (`.doc`, `.docx`) | 支持 | 必须原创、明确授权或可公开再分发，并配套 Markdown 说明。 |

暂不接收 PPT、压缩包、录音、录像、图片包、教材扫描件、内部课件、未授权题库、原始试卷扫描件或任何含隐私的信息。

## 仓库结构

```text
wmuer_undergrad_resources/
  years/
    freshman/
      summaries/
      experience-posts/
      documents/
    sophomore/
      summaries/
      experience-posts/
      documents/
    junior/
      summaries/
      experience-posts/
      documents/
    senior/
      summaries/
      experience-posts/
      documents/
    fifth-year-internship/
      summaries/
      experience-posts/
      documents/
  templates/
  docs/
  scripts/
```

## 合规边界

- 可以收录：原创总结、原创经验贴、可公开分享的资源索引、明确授权的 PDF/Word 文档。
- 不可收录：盗版教材、教材扫描件、内部讲义、未授权题库、原始试卷扫描件、录音录像、患者隐私、教师个人隐私、科室敏感信息。
- 临床相关内容必须标注更新时间和适用范围，不能写成具体医疗建议。

## Medical Disclaimer

本资料库仅用于医学教育、课程学习和同学间经验交流，不构成医疗建议，不能替代执业医师判断、学校课程要求、医院规章制度或官方指南。任何临床相关内容都应结合最新指南、教师要求和所在机构规范进行判断。

This repository is for medical education, coursework, and peer learning only. It does not provide medical advice and must not replace licensed clinical judgment, institutional requirements, school curricula, or official guidelines.

## License

除非文件中另有说明，本仓库原创内容采用 Creative Commons Attribution 4.0 International License (`CC BY 4.0`) 授权。

Unless otherwise stated, the original content in this repository is licensed under the Creative Commons Attribution 4.0 International License (`CC BY 4.0`).
