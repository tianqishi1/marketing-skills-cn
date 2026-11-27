# marketing-skills-cn：28 个国内营销 Skills（Codex / Claude Code 通用）

[![CI](https://github.com/tianqishi1/marketing-skills-cn/actions/workflows/ci.yml/badge.svg)](https://github.com/tianqishi1/marketing-skills-cn/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)

> **28 China-marketing agent skills** (Codex / Claude Code compatible): ad-platform diagnostics
> (Ocean Engine / Qianchuan, Tencent Ads, Kuaishou, Baidu, Xiaohongshu), e-commerce ads, content
> generation, KOL seeding, livestream, WeCom private-domain ops, Baidu SEO, social search, domestic
> AI-search visibility (GEO) and Advertising-Law compliance. Zero MCP dependencies — every skill
> ships a data contract, workflow, thresholds, output templates and hard constraints.
>
> **生态**：技能生态 marketing-skills-cn · Agent 底座 [agent-base](https://github.com/tianqishi1/agent-base) · 评测流水线 [eval-pipeline](https://github.com/tianqishi1/eval-pipeline)

对标 [irinabuht12-oss/marketing-skills](https://github.com/irinabuht12-oss/marketing-skills)（49 个 Google/Meta 营销 skills）重写的**国内适配版**：不是汉化，而是按中国市场的渠道、平台机制、数据生态与合规约束整体重建。适用性评估见 [docs/evaluation.md](docs/evaluation.md)。

**覆盖**：巨量引擎/千川、腾讯广告、快手磁力、百度营销、小红书聚光/蒲公英、万相台 AI 无界、京准通、拼多多、企微私域、直播电商、百度 SEO、社交搜索、国内 AI 搜索（夸克/DeepSeek/豆包/元宝/Kimi/秘塔）、广告法合规。

## 设计原则

1. **零 MCP 依赖**：国内没有统一的广告数据连接器。所有分析类 skill 的数据契约 = 平台后台导出 CSV/Excel 或粘贴数据（字段按各平台真实导出名对齐）。
2. **流程型 skill**：每个都有数据契约 → 流程 → 阈值/checklist → 输出模板 → 约束，不写空泛描述。
3. **合规内嵌**：内容生成类自带红线清单；系统检查用 `ad-compliance-cn`（广告法/互联网广告管理办法/行业宣称/平台规范）。
4. **阈值是经验值**：所有数字门槛要求用自有账户历史校准；输出必带置信度与数据缺口说明，不臆造数据。
5. **平台事实为 2025–2026 现行口径**：千川全域推广、万相台 AI 无界（关键词推广/人群推广/货品全站推）、微信小店、磁力金牛、灵犀 AIPS、如翼 5R 等；产品迭代快，以用户后台实际为准。

## 安装

### Codex（本应用）

```powershell
# 复制全部 skills 到 Codex 技能目录
.\install.ps1 -Target codex
```

或手动：把 `skills/` 下各文件夹复制到 `~/.codex/skills/`（Windows：`C:\Users\<你>\.codex\skills\`）。

### Claude Code

```powershell
.\install.ps1 -Target claude     # 复制到 ~/.claude/skills/
```

或作为插件市场安装：

```
claude plugin marketplace add tianqishi1/marketing-skills-cn
claude plugin install marketing-skills-cn@marketing-skills-cn
```

安装后直接用自然语言触发，例如：

- "帮我审计这个巨量账户，数据我粘贴给你"
- "写 5 个小红书标题，产品是 XX，人群是 XX"
- "千川全域推广 ROI 掉了，帮我诊断"
- "检查这段文案有没有违反广告法"

## 技能目录（5 组 28 个）

### A. 投放诊断与优化（11）

| Skill | 用途 |
|---|---|
| ads-audit-cn | 信息流/搜索账户审计（巨量/腾讯/快手/百度/聚光，分平台 checklist） |
| ecommerce-ads-cn | 电商站内投放（千川全域/万相台AI无界/京准通/拼多多） |
| cpa-diagnostics-cn | 转化成本上涨/掉量诊断树 |
| wasted-spend-finder-cn | 无效消耗排查与止损清单 |
| budget-allocator-cn | 跨渠道预算分配与情景推演（边际成本视角） |
| creative-fatigue-cn | 素材疲劳监测与轮换排期（国内短生命周期口径） |
| ab-test-analyzer-cn | A/B 测试设计与显著性（含平台分发偏差纠正） |
| ad-anomaly-monitor-cn | 每日数据异常巡检（P0–P2 分级） |
| ads-weekly-report-cn | 投放周报/客户汇报（结论先行） |
| search-term-mining-cn | 搜索词挖词与否词（百度/巨量搜索/小红书/电商） |
| landing-page-audit-cn | 落地页审计（基木鱼/橙子/微信原生页/小程序/详情页） |

### B. 内容与种草（7）

| Skill | 用途 |
|---|---|
| xhs-note-writer | 小红书笔记（标题/正文/标签/封面/评论区+违规规避） |
| douyin-script-writer | 抖音脚本（前3秒钩子/完播结构/千川变体） |
| wechat-article-writer | 公众号文章（打开率/搜一搜埋词/广告标注） |
| content-repurposer-cn | 一稿多发（公众号/小红书/抖音/视频号/知乎/微博/B站） |
| kol-selection-cn | 达人筛选与假数据识别（蒲公英/星图/花火/聚星/芝士） |
| seeding-strategy-cn | 种草策略（KFS/人群反漏斗/AIPS/O-5A/5R） |
| livestream-planner-cn | 直播策划（排品/脚本话术/流量节奏/复盘） |

### C. 私域与转化（3）

| Skill | 用途 |
|---|---|
| private-domain-sop-cn | 企微私域 SOP（引流/标签/触达/复购/合规） |
| wecom-touch-sequence-cn | 私域触达序列（替代 email sequence） |
| campaign-planner-cn | 大促节点全案（618/双11/年货节节奏与机制） |

### D. 搜索与 AI 可见性（3）

| Skill | 用途 |
|---|---|
| baidu-seo-cn | 百度 SEO（收录/落地页规范/算法红线/百度系占位） |
| social-search-seo-cn | 社交搜索卡位（小红书/抖音/微信搜一搜） |
| ai-visibility-cn | 国内 GEO（夸克/DeepSeek/豆包/元宝/Kimi/秘塔/百度AI） |

### E. 策略与合规（4）

| Skill | 用途 |
|---|---|
| icp-research-cn | 人群洞察与画像（反漏斗分层+平台人群资产映射） |
| competitor-teardown-cn | 竞品拆解（蝉妈妈/千瓜/新榜等公开数据） |
| ad-compliance-cn | 广告合规检查（极限词/行业红线/软文标注/平台规范） |
| tracking-setup-cn | 渠道追踪与归因（UTM局限/clickid回传/渠道活码/小程序参数） |

## 与原仓库的关系

- 继承其工程范式（数据契约→流程→阈值→输出模板→置信度），MIT 协议兼容。
- 渠道知识整体重写；新增原仓库没有的国内必需能力（种草/达人/直播/私域/电商站内/合规/社交搜索）。
- 不捆绑任何商业 MCP 导流。

## 免责声明

- 所有阈值为行业经验起点，非平台官方标准；请以自有账户数据校准。
- 平台产品名与规则迭代快，以各平台当期后台与官方公告为准。
- 合规检查为营销辅助，不构成法律意见；重大投放请法务复核。

## License

MIT

## 开发与质量门禁（CI/CD）

[![CI](https://github.com/tianqishi1/marketing-skills-cn/actions/workflows/ci.yml/badge.svg)](https://github.com/tianqishi1/marketing-skills-cn/actions/workflows/ci.yml)

`main` 为保护分支：**禁止直接 push**，所有变更走「新分支 → PR → CI 全绿 → 合并」。

PR 必须通过 4 项质量门禁（`.github/workflows/ci.yml`）：

| 检查 | 内容 |
|---|---|
| `validate` | 每个 skill 有 SKILL.md、frontmatter 合法且 name=目录名、description 非空≤1024 字符、正文非空壳；plugin.json/marketplace.json 合法且一致、version 为 semver；install.ps1 语法检查 |
| `markdown-lint` | markdownlint（中文文档友好配置，见 `.markdownlint-cli2.jsonc`） |
| `link-check` | lychee 离线检查全部 Markdown 内部链接与锚点 |
| `secret-scan` | gitleaks 密钥/凭据泄漏扫描 |

本地预检：

```powershell
python scripts/validate_repo.py          # 结构校验
npx -y markdownlint-cli2 --fix "**/*.md" # lint + 自动修复
```

### 发布（CD）

`.github/workflows/release.yml`：打 `v*.*.*` tag 自动触发——校验 tag 与 `plugin.json` version 一致 → 重跑质量校验 → `git archive` 打包插件 zip → 创建 GitHub Release 并附产物。

```powershell
# 1. 在 PR 中把 .claude-plugin/plugin.json 的 version 升到 1.1.0 并合并
# 2. 打 tag 推送：
git checkout main; git pull
git tag v1.1.0; git push origin v1.1.0
# 3. Actions 自动发布 Release
```

## 质量门禁（Skill 也是被评测对象）

本仓库把"技能质量"当作工程问题，CI 每次提交运行四层检查：

1. **结构校验**（`scripts/validate_repo.py`）：frontmatter 合法、命名规范、manifest 一致、引用路径存在。
2. **触发路由评测**（`scripts/eval_triggers.py --gate`）：56 条自然语言用例覆盖全部 28 个 skill，
   离线确定性代理评测（字符二元组重叠打分），门禁要求 **准确率 ≥85% 且 28/28 全覆盖**。
   当前基线见 `evals/report.json`；误路由用例即 badcase，改进 description 触发词后必须重跑。
3. **Markdown lint + 内链检查**：文档质量与链接完整性。
4. **gitleaks 密钥扫描**：防止凭据入库。

> 代理评测的局限：词面重叠无法理解语义改写，3 条已知误路由记录在 `evals/report.json` 的 confusion 列表。
> 下一阶段计划接入 LLM judge（用 [eval-pipeline](https://github.com/tianqishi1/eval-pipeline) 的校准与门禁机制，
> judge 与人工标注 Cohen κ ≥ 0.7 才可信）。

本地运行：

```bash
python scripts/validate_repo.py
python scripts/eval_triggers.py --gate
```

## 贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)：新增 skill 必须带数据契约 + 阈值来源说明 + 至少 2 条触发用例，并通过全部门禁。
