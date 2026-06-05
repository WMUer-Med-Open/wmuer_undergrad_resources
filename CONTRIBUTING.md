# Contributing Guide

感谢你为 `wmuer_undergrad_resources` 投稿。这个仓库欢迎清晰、可靠、可维护的医学本科资料，不欢迎无法确认来源或授权的资料堆叠。

## 投稿流程

1. 确认内容可以公开分享。
2. 选择对应年级和类别目录。
3. 复制 [templates/](templates/) 中的模板并填写元信息。
4. 按命名规则保存文件。
5. 检查版权、隐私和医学表述边界。
6. 提交 Pull Request。

## 目录选择

| 内容 | 放置目录 | 说明 |
|---|---|---|
| 课程总结、系统总结、疾病学习总结、复习提纲 | `years/<year>/summaries/` | 优先使用 Markdown。 |
| 学习经验、考试经验、教改班经验、实习经验 | `years/<year>/experience-posts/` | 必须说明适用条件和局限。 |
| 可公开分享的 Markdown/PDF/Word 文档 | `years/<year>/documents/` | PDF/Word 必须配套 Markdown 说明。 |

可用年级目录：

```text
years/freshman/
years/sophomore/
years/junior/
years/senior/
years/fifth-year-internship/
```

## 文件命名

- 使用小写英文、数字和连字符。
- 不使用空格、中文标点、括号或特殊符号。
- 推荐格式：`topic-purpose.md`、`course-topic-review.md`、`rotation-experience.md`。

示例：

```text
cardiovascular-physiology-review.md
pathology-exam-strategy.md
pediatrics-internship-notes.md
clinical-skills-document.md
```

## Markdown 元信息

Markdown 文件顶部建议保留统一元信息：

```md
---
title: 资料标题
year: junior
category: summaries
author: your-github-id
license: CC BY 4.0
last_updated: 2026-06-05
source: original
---
```

`source` 可以填写：

- `original`：原创。
- `authorized`：已获得授权。
- `public-redistributable`：公开且允许再分发。
- `index-only`：仅做资源索引，不搬运原文。

## 可以投稿的内容

- 原创 Markdown 总结、复习框架、疾病学习总结。
- 原创学习经验、考试经验、实习经验。
- 公开授权资源的索引、简介和使用建议。
- 原创、明确授权或可公开再分发的 PDF/Word 文档。

## 不接收的内容

- 盗版教材、教材扫描件、未授权翻拍资料。
- 学校内部课件、内部讲义、未授权题库、原始试卷扫描件。
- PPT、图片包、压缩包、录音、录像。
- 未配套 Markdown 说明的 PDF/Word 文件。
- 含患者隐私、教师个人隐私、科室敏感信息或医院内部非公开流程的内容。
- 无来源、无授权说明、无法判断可信度的搬运内容。
- 把个人经验包装成确定诊疗建议的内容。

## PDF/Word 规则

PDF 和 Word 文件只作为补充资料，不替代 Markdown 说明。

提交 PDF/Word 时必须满足：

- 文件本身是原创、明确授权或可公开再分发。
- 放在对应年级的 `documents/` 目录。
- 同目录有一个同名 Markdown 说明，例如 `clinical-skills.pdf` 配套 `clinical-skills.md`。
- Markdown 说明写清来源、授权、适用年级、适用课程或科室、使用建议。
- 文件体积尽量小；大文件建议外部托管并在 Markdown 中索引。

## 医学内容标准

医学总结建议尽量说明：

- 适用年级、课程、系统或科室。
- 更新时间。
- 参考来源或使用场景。
- 关键知识点和常见误区。
- 个人经验的局限。

涉及临床内容时，不要写成对具体患者的诊疗建议。请使用“学习理解”“考试复习”“课程要求”“指南需更新核对”等表述。

## 隐私检查

提交前必须确认不包含：

- 患者姓名、电话、住址、床号、住院号、门诊号、影像号、病历号。
- 可识别患者身份的时间线、照片、检查图像或病例细节组合。
- 教师、同学、患者、医护人员的私人评价和联系方式。
- 科室内部账号、群聊、排班、非公开流程或敏感安排。

更完整的边界见 [docs/copyright-and-privacy.md](docs/copyright-and-privacy.md)。

## Pull Request Checklist

提交 PR 前请确认：

- 文件已放入正确年级和类别目录。
- 文件名符合小写英文、数字、连字符规则。
- Markdown 文件填写了标题、年级、类别、作者、授权和更新时间。
- PDF/Word 文件已经配套同名 Markdown 说明。
- 已说明资料来源和授权状态。
- 已完成隐私检查。
- 医学内容没有被写成具体医疗建议。
