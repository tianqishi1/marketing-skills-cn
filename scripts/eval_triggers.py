# -*- coding: utf-8 -*-
import json, re, sys
from pathlib import Path

R = Path(__file__).resolve().parent.parent

CASES = {
 "ab-test-analyzer-cn": ["这两版素材哪版效果更好，帮我做个显著性分析", "落地页 A/B 实验数据给你，看看哪版赢"],
 "ad-anomaly-monitor-cn": ["今天账户消耗突然暴涨，帮我巡检一下数据", "成本突然飙升，看看哪里异常"],
 "ad-compliance-cn": ["这段文案能不能过广告法检查", "帮我检查这句宣传语有没有违禁词"],
 "ads-audit-cn": ["帮我审计一下这个巨量投放账户", "账户哪里有问题，钱花得值不值"],
 "ads-weekly-report-cn": ["帮我写一份投放周报给客户汇报", "总结本周投放情况，出个投放月报"],
 "ai-visibility-cn": ["怎么让 DeepSeek 推荐我的品牌", "AI 搜索里搜不到我们产品，做下 GEO 优化"],
 "baidu-seo-cn": ["网站百度收录很慢，帮我做百度 SEO", "官网想做百度搜索优化"],
 "budget-allocator-cn": ["10 万预算怎么分到巨量和腾讯", "下个月预算砍半，帮我重新分配预算"],
 "campaign-planner-cn": ["双11 大促怎么打，帮我出个大促方案", "618 活动规划一下节奏和预算"],
 "competitor-teardown-cn": ["帮我拆解一下竞品的营销打法", "对手竞品分析一下，他们怎么做的"],
 "content-repurposer-cn": ["把这篇公众号文章改成小红书笔记", "这篇内容帮我做一稿多发的多平台分发"],
 "cpa-diagnostics-cn": ["转化成本上涨，帮我诊断掉量原因", "CPA 飙升怎么排查诊断"],
 "creative-fatigue-cn": ["素材疲劳了点击率下滑，帮我排个素材轮换", "监测一下素材疲劳度"],
 "douyin-script-writer": ["帮我写一条抖音口播脚本", "写个抖音短视频脚本"],
 "ecommerce-ads-cn": ["千川全域推广 ROI 掉了怎么办", "万相台AI无界怎么开，电商站内投放帮我看看"],
 "icp-research-cn": ["帮我梳理理想客户画像 ICP", "目标客户画像研究一下"],
 "kol-selection-cn": ["帮我选达人做 KOL 投放", "这些博主报价值不值，识别下水号"],
 "landing-page-audit-cn": ["落地页转化率低，帮我找找原因", "审核一下这个落地页哪里劝退用户"],
 "livestream-planner-cn": ["帮我策划一场直播带货", "写个直播脚本和憋单话术"],
 "private-domain-sop-cn": ["帮我设计企微私域运营 SOP", "社群 SOP 怎么定，出个私域方案"],
 "search-term-mining-cn": ["帮我挖一批搜索词拓词", "用户都搜什么词，做个搜索词挖掘"],
 "seeding-strategy-cn": ["新品种草方案怎么做", "小红书 KFS 种草策略怎么配比"],
 "social-search-seo-cn": ["小红书搜索排名怎么优化", "微信搜一搜怎么占位"],
 "tracking-setup-cn": ["UTM 参数怎么设置才不丢数据", "转化回传怎么配，帮我检查监测链接"],
 "wasted-spend-finder-cn": ["看看哪些计划在浪费钱", "帮我找出无效消耗止损"],
 "wechat-article-writer": ["帮我写一篇公众号文章", "写个公众号推文，标题要吸引人"],
 "wecom-touch-sequence-cn": ["设计一套企微私域触达序列", "新客加微后怎么跟进，写个触达话术序列"],
 "xhs-note-writer": ["帮我写小红书笔记和标题", "写篇小红书种草笔记文案"],
}

def bigrams(text):
    text = re.sub(r"\s+", "", text.lower())
    zh = re.findall(r"[\u4e00-\u9fff]", text)
    en = re.findall(r"[a-z0-9]+", text)
    grams = set()
    for i in range(len(zh) - 1):
        grams.add(zh[i] + zh[i+1])
    grams.update(en)
    return grams

def load_skills():
    skills = {}
    for d in sorted((R / "skills").iterdir()):
        if not d.is_dir():
            continue
        s = (d / "SKILL.md").read_text(encoding="utf-8")
        m = re.search(r"description:\s*(.+)", s)
        desc = m.group(1) if m else ""
        quoted = re.findall(r'[\u201c"]([^\u201d"]+)[\u201d"]', desc)
        skills[d.name] = {"desc": desc, "quoted": quoted}
    return skills

def main():
    gate = "--gate" in sys.argv
    skills = load_skills()
    # discoverability: quoted trigger phrases must exist (they come from the description itself)
    # routing index: bigrams of description + quoted phrases + name tokens
    index = {}
    for name, info in skills.items():
        text = info["desc"] + " " + " ".join(info["quoted"]) + " " + name.replace("-cn", "").replace("-", " ")
        index[name] = bigrams(text)
    cases = [{"text": t, "expect": k} for k, ts in CASES.items() for t in ts]
    results, correct, confusion = [], 0, []
    for c in cases:
        utt = bigrams(c["text"])
        scores = {n: len(utt & g) / max(len(utt), 1) for n, g in index.items()}
        best = max(scores, key=scores.get)
        pred = best if scores[best] >= 0.15 else None
        ok = pred == c["expect"]
        correct += ok
        results.append({**c, "pred": pred, "score": round(scores[best], 3), "ok": ok})
        if not ok:
            confusion.append({"text": c["text"], "expect": c["expect"], "pred": pred,
                              "expect_score": round(scores[c["expect"]], 3)})
    acc = correct / len(cases)
    covered = {c["expect"] for c in cases}
    report = {"cases": len(cases), "skills": len(skills), "covered": len(covered),
              "accuracy": round(acc, 4), "confusion": confusion, "results": results}
    out = R / "evals" / "report.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"trigger-routing proxy eval: {correct}/{len(cases)} = {acc:.1%}, skills covered {len(covered)}/{len(skills)}")
    for x in confusion:
        print("  MISS:", x)
    if gate and (acc < 0.85 or len(covered) < len(skills)):
        print("GATE FAILED"); sys.exit(1)
    if gate:
        print("GATE PASSED")

if __name__ == "__main__":
    main()