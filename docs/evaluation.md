# marketing-skills（Ryze AI）国内适用性评估报告

评估对象：https://github.com/irinabuht12-oss/marketing-skills （49 个 Claude 营销 skills，MIT 协议）
评估日期：2026-11-19

## 一、原仓库是什么

由 Ryze AI（get-ryze.ai）维护的营销技能包，本质是 **49 份 Markdown 格式的方法论 SOP**，供 Claude Code / Claude Desktop / Cursor 等按需加载。每个 skill 告诉模型：要什么数据、按什么步骤分析、用什么阈值判断、输出什么格式的报告。

| 分类 | 数量 | 代表 skill |
|---|---|---|
| Google Ads（含 Google+Meta 跨平台） | 35 | 账户审计、无效消耗排查、CPA 诊断、搜索词挖掘、质量分拆解、预算分配、A/B 测试、周报 |
| Meta Ads 专属 | 6 | 素材疲劳监测、受众重叠、频次上限、再营销窗口、竞品素材分析 |
| SEO（Google） | 3 | 端到端 SEO 助手、程序化 SEO 构建器与打法手册 |
| AI 可见性（GEO/AEO） | 4 | AI 引用审计、信源缺口、AEO 内容优化、品牌答案监控 |

商业动机：仓库是 Ryze MCP 连接器（Google Ads / Meta Ads / GA4 / Search Console 数据）的获客入口，每个 skill 尾部都带连接器导流。skills 本身不依赖 MCP，可用粘贴的导出数据运行。

质量分层：约 1/3 是"流程型"（有 checklist、阈值表、输出模板、示例，如 google-ads-audit），约 2/3 是"描述型"（what/how/example 三段式，约束较弱）。**流程型的骨架值得借鉴，描述型的信息密度偏低。**

## 二、国内适用性矩阵

### 1. 直接可用：几乎为零（数据接入层）

- Ryze MCP 只接 Google / Meta / GA4 / GSC，**无法接任何国内平台**（巨量引擎、腾讯广告、聚光、百度营销、阿里妈妈均不在内）。
- Google / Meta / LinkedIn / Reddit 在中国大陆不可直接访问，对纯内贸业务这些渠道本身不存在。

### 2. 方法论可迁移：约 30%（需换阈值、换术语、换数据源）

A/B 显著性计算、预算分配框架、异常检测思路、报告叙事结构、ICP 画像方法、竞品落地页拆解、转化漏斗分析——这些"分析骨架"跨市场通用。但：

- 阈值需重标定（如 Google 搜索 CTR≥1.5% 的及格线，放到国内信息流/搜索场景完全不适用）；
- 指标口径不同（国内投放核心是消耗/转化成本/ROI/跑量，而不是 Quality Score / Impression Share）；
- 数据源不同（平台后台导出 CSV、蝉妈妈/千瓜等三方工具，而非 GA4）。

### 3. 需整体重写：约 60%（渠道机制层）

| 原 skill 依赖 | 国内现实 |
|---|---|
| Google 搜索广告、质量分、广告附加信息 | 百度搜索推广（oCPC）、巨量搜索、小红书搜索广告；无"质量分"公开体系 |
| Meta 受众/频次/再营销窗口 | 巨量/腾讯的定向包、莱卡/行为兴趣、人群资产（O-5A / 5R / AIPS）、自动化托管投放占比高 |
| LinkedIn / Reddit 广告审计 | 国内无对应物；B2B 对应的是知乎、公众号、百度、企微私域 |
| Email 序列写作 | 国内 email 打开率极低；对应物是企微私域触达序列、公众号、短信 |
| 内容分发到 LinkedIn/Twitter/YouTube | 对应物是公众号/小红书/抖音/视频号/B站/知乎/微博，且各平台文体差异远大于西方平台 |
| Google 程序化 SEO | 百度收录机制、移动落地页规范、算法（飓风/惊雷/冰桶等）完全不同 |
| ChatGPT/Perplexity/AI Overviews 可见性 | 国内入口是夸克、DeepSeek、豆包、元宝（独家可搜公众号）、Kimi、秘塔、百度 AI 搜索；信源生态是知乎/公众号/百家号/百科 |

### 4. 原仓库完全没覆盖、但国内必需的能力（最大缺口）

1. **内容种草**：小红书笔记、抖音短视频脚本、公众号文章——国内营销的主战场是内容，不是搜索广告。
2. **达人营销**：星图/蒲公英/花火/聚星/芝士的达人筛选、报价评估、假数据识别。
3. **直播电商**：排品、脚本、憋单、流量承接（千川全域推广 + 内容场/货架场联动）。
4. **私域运营**：企微 SOP、社群、朋友圈、触达序列（国内 LTV 经营的核心）。
5. **电商站内投放**：千川、万相台 AI 无界（关键词推广/人群推广/货品全站推）、京准通、拼多多。
6. **合规**：《广告法》极限词、《互联网广告管理办法》（2023 施行，软文须标"广告"）、化妆品功效宣称、食品/医疗/教育/金融红线、平台社区规范（虚假种草治理）。**这是国内的硬约束，原仓库完全没有对应物。**
7. **社交搜索**：小红书/抖音/微信搜一搜的搜索优化（"万物皆可搜"，搜索流量占比持续上升）。
8. **渠道追踪的国内现实**：UTM 在微信内打开/小程序/APP 场景大量失效，需要 clickid、渠道活码、小程序路径参数等替代方案。

## 三、结论：是否有必要开发国内版？

**有必要，且价值主要不在"翻译"，而在"重写渠道知识 + 补齐缺口"。**

理由：

1. **直接搬运可用度 <20%**：渠道、数据、合规三层全部错位，汉化版会误导用户（例如按 Google 阈值诊断百度账户）。
2. **国内渠道知识密度高且分散**：平台产品名迭代快（直通车→关键词推广、视频号小店→微信小店、万相台→万相台 AI 无界），一线运营大量时间耗在"平台机制常识"上，正是 skill 最适合固化的知识。
3. **合规是刚需**：极限词/功效宣称/软文标注直接关系罚款与封号，内容生成类 skill 内置合规检查有真实价值。
4. **生态时机**：Codex / Claude Code 国内可用，百炼等国内生态也在推 skill 体系，中文垂直 skill 包稀缺。
5. **方法论已被验证**：原仓库 49 个 skill 的分析骨架（数据契约→流程→阈值→输出模板→置信度）是好的工程范式，可直接继承。

## 四、国内版设计原则（marketing-skills-cn）

1. **不绑定任何 MCP**：国内无统一广告数据连接器。数据契约统一为"平台后台导出 CSV/Excel 或粘贴数据"，字段名用各平台真实导出名。
2. **平台事实用 2025–2026 现行官方名**：巨量千川（全域推广）、万相台 AI 无界、微信小店、磁力金牛、聚光/蒲公英/灵犀、如翼 5R、AIPS 等。
3. **合规内嵌**：所有内容生成 skill 自带红线清单，另有独立的 ad-compliance-cn 做系统检查。
4. **阈值标注为行业经验值**：要求用自有账户历史数据校准，输出必带置信度与缺失数据说明（继承原仓库的优点）。
5. **流程型优先**：每个 skill 都有数据契约/流程/输出模板，不写空泛的"描述型"skill。

## 五、原仓库 → 国内版映射（49 → 28）

| 原版分组 | 国内版去向 |
|---|---|
| google-ads-audit / meta-ads-audit / linkedin / reddit 审计 | ads-audit-cn（巨量/腾讯/快手/百度/聚光分平台 checklist）+ ecommerce-ads-cn（千川/阿里妈妈/京东/拼多多） |
| cpa-diagnostics / wasted-spend / anomaly-detection / pacing | cpa-diagnostics-cn / wasted-spend-finder-cn / ad-anomaly-monitor-cn |
| budget-scenario-planner / ad-spend-allocator / channel-mix | budget-allocator-cn |
| creative-fatigue / frequency-cap / audience-overlap / retargeting | creative-fatigue-cn（国内素材生命周期更短，逻辑重写）；人群重叠并入 ads-audit-cn |
| ab-test-setup / ab-test-analyzer | ab-test-analyzer-cn |
| search-term-mining / keyword-cannibalization | search-term-mining-cn（百度/巨量搜索/小红书搜索/淘宝） |
| landing-page-audit ×2 / competitor-teardown | landing-page-audit-cn（基木鱼/橙子建站/微信原生页/小程序/详情页）/ competitor-teardown-cn |
| ad-copy-variant-generator | 拆入 douyin-script-writer / xhs-note-writer / wechat-article-writer（国内"广告文案"主战场是内容） |
| email-sequence-writer | wecom-touch-sequence-cn（企微私域触达序列） |
| content-repurposer | content-repurposer-cn（一稿多发：公众号→小红书→抖音→知乎→视频号→微博） |
| weekly-account-summary / client-report-narratives | ads-weekly-report-cn |
| icp-research-assistant | icp-research-cn（叠加 O-5A/AIPS/5R 人群资产视角） |
| utm-tracking-generator | tracking-setup-cn（UTM 局限 + clickid/渠道活码/小程序参数） |
| e2e-seo / programmatic-seo ×2 | baidu-seo-cn + social-search-seo-cn |
| ai-visibility ×4 | ai-visibility-cn（夸克/DeepSeek/豆包/元宝/Kimi/秘塔/百度 AI） |
| 无对应物（新增） | xhs-note-writer、douyin-script-writer、wechat-article-writer、kol-selection-cn、seeding-strategy-cn、livestream-planner-cn、private-domain-sop-cn、campaign-planner-cn、ad-compliance-cn |
| google-quality-score / ad-extension / bid-strategy / attribution / geo / device 等 Google 专属机制 | 不单独保留，要点并入 ads-audit-cn 与 cpa-diagnostics-cn |
