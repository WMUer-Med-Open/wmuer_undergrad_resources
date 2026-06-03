# Contributing Guide

感谢你为 `wmuer_undergrad_resources` 投稿。这个仓库的目标不是堆积文件，而是建立可追溯、可维护、可复用的医学本科开放资料库。

## What We Accept

- 各年级的原创 Markdown 总结、课程复习、疾病学习总结和学习框架。
- 各年级的学习经验、考试经验、教改班经验、实习经验。
- 原创或明确授权的 PDF、Word 资料，并建议配套 Markdown 索引说明。
- 公开授权资源的索引、简介和使用建议。

## What We Do Not Accept

- PPT、图片包、压缩包、录音、录像等暂不支持的文件类型。
- 未配套 Markdown 索引说明的 PDF 或 Word 文件。
- 盗版教材、教材扫描件、未授权翻拍资料。
- 学校内部课件、内部讲义、未授权题库或原始试卷扫描件。
- 含患者隐私、教师个人隐私、科室敏感信息或医院内部流程细节的内容。
- 无来源、无授权说明、无法判断可信度的搬运内容。
- 把个人经验包装成确定诊疗建议的内容。

## File Rules

- 优先使用 `.md`。
- 支持 `.pdf`、`.doc`、`.docx`，但必须原创、明确授权或可公开再分发。
- PDF/Word 文件必须配套一个 Markdown 索引条目，说明来源、授权、适用阶段和使用建议。
- 文件名使用小写英文、数字和连字符，例如 `heart-failure.md`。
- 中文内容为主；关键页面建议提供英文摘要。
- 所有资料放到对应年级目录：

```text
years/<year>/summaries/
years/<year>/experience-posts/
years/<year>/documents/
```

- Markdown 资料顶部建议使用统一元信息：

```md
---
title: 资料标题
year: junior
category: summaries
author: your-github-id
license: CC BY 4.0
last_updated: 2026-06-04
---
```

## Summaries

总结建议使用 `templates/summary-template.md`。医学主题建议尽量体现疾病学习模式，把以下内容联系起来：

- 基础医学机制。
- 病理生理。
- 临床表现。
- 诊断思路。
- 治疗原则。
- 考试重点。
- 学习或实习经验。

## Experience Posts

经验贴建议使用 `templates/experience-post-template.md`。可以写学习经验、考试经验、教改班经验或实习经验，但必须说明适用年级、适用课程或科室，以及经验的局限。

不要上传原始试卷、扫描件、截图、内部题库或未经授权的课程材料。

## Documents

PDF 和 Word 文件只作为补充资料，不替代 Markdown 索引。

提交要求：

- 文件必须是原创、明确授权或可公开再分发。
- 文件名使用小写英文、数字和连字符。
- 建议同目录配套 Markdown 索引说明。
- 不上传教材扫描件、内部课件、未授权题库、原始试卷扫描件或含隐私的文档。
- 文件应尽量保持小体积；过大的文件建议另行托管并在 Markdown 中索引。

## Internship Posts

实习经验贴必须去除：

- 患者姓名、床号、住院号、影像号等身份信息。
- 教师个人隐私和评价性描述。
- 科室内部敏感流程、账号、联系方式或非公开安排。

## Pull Request Checklist

提交 PR 前请确认：

- 内容为 Markdown 文件，或合规 PDF/Word 文件并配套 Markdown 索引。
- 已说明资料来源和授权状态。
- 已说明适用年级或学习阶段。
- 已说明是否原创；非原创内容仅做索引或引用，不整段搬运。
- 已完成隐私检查。
- 医学内容没有被写成具体医疗建议。
