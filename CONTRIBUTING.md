# 贡献指南

欢迎新增国内营销 skill、修正平台口径、补充触发用例。

## 新增 / 修改 skill 的硬性要求

1. `skills/<name>/SKILL.md`：frontmatter `name` 与目录一致（小写-连字符），`description` 写清
   **什么时候触发**（含用户口语触发词）与**什么时候不触发**（边界让给哪个 skill）。
2. 正文必须是流程型：数据契约 → 流程 → 阈值/checklist → 输出模板 → 约束。
   阈值注明是经验值并要求用户用自有账户历史校准；禁止臆造平台数据。
3. 平台事实注明口径时间（产品迭代快，以用户后台实际为准）。
4. 内容生成类必须内嵌合规红线（广告法/互联网广告管理办法/行业宣称）。
5. 在 `scripts/eval_triggers.py` 的 `CASES` 中为该 skill 增加 **≥2 条自然语言触发用例**
   （口语化改写，不要照抄 description）。

## 提交前必须通过

```bash
python scripts/validate_repo.py          # 结构校验
python scripts/eval_triggers.py --gate   # 触发路由 ≥85% 且全覆盖
npx -y markdownlint-cli2 "**/*.md"       # 文档 lint
```

CI 会运行以上全部检查 + 内链检查 + gitleaks。任何一项失败都会阻断合并。

## 平台口径纠错

直接在 issue 里给出：平台名 + 后台截图/导出字段 + 现行口径说明。
涉及广告法/合规的修正请附法规条文出处。

## 许可

提交即表示同意以 MIT 许可分发你的贡献。
