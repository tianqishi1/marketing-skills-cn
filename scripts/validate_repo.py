#!/usr/bin/env python3
"""marketing-skills-cn 仓库质量校验（CI 门禁核心）。

校验项：
1. skills/<dir>/SKILL.md 必须存在，YAML frontmatter 合法
2. frontmatter.name 与目录名一致，且为小写字母/数字/连字符（<=64 字符）
3. frontmatter.description 非空且 <=1024 字符
4. SKILL.md 正文有实质内容（>=200 字符）
5. plugin.json / marketplace.json 为合法 JSON，名称一致，version 为 semver
6. manifest 中引用的路径必须存在
7. README.md / LICENSE 必须存在
"""
import json
import re
import sys
from pathlib import Path

import yaml

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(-[0-9A-Za-z.-]+)?$")
errors = []


def err(msg):
    errors.append(msg)
    print(f"  [FAIL] {msg}")


def ok(msg):
    print(f"  [ok] {msg}")


def check_skills():
    print("== Skills 结构校验 ==")
    skills_dir = ROOT / "skills"
    if not skills_dir.is_dir():
        err("skills/ 目录不存在")
        return 0
    dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir())
    if not dirs:
        err("skills/ 下没有任何 skill 目录")
    for d in dirs:
        f = d / "SKILL.md"
        if not f.is_file():
            err(f"{d.name}: 缺少 SKILL.md")
            continue
        text = f.read_text(encoding="utf-8")
        m = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
        if not m:
            err(f"{d.name}: SKILL.md 缺少 YAML frontmatter（--- 包裹）")
            continue
        try:
            fm = yaml.safe_load(m.group(1))
        except yaml.YAMLError as e:
            err(f"{d.name}: frontmatter YAML 解析失败: {e}")
            continue
        if not isinstance(fm, dict):
            err(f"{d.name}: frontmatter 不是键值映射")
            continue
        name = fm.get("name", "")
        desc = fm.get("description", "")
        if name != d.name:
            err(f"{d.name}: frontmatter.name={name!r} 与目录名不一致")
        if not isinstance(name, str) or not NAME_RE.match(name) or len(name) > 64:
            err(f"{d.name}: name 不符合规范（小写字母/数字/连字符，<=64 字符）: {name!r}")
        if not isinstance(desc, str) or not desc.strip():
            err(f"{d.name}: description 为空")
        elif len(desc) > 1024:
            err(f"{d.name}: description 超过 1024 字符（当前 {len(desc)}）")
        body = text[m.end():].strip()
        if len(body) < 200:
            err(f"{d.name}: 正文过短（{len(body)} 字符 < 200），疑似空壳 skill")
    ok(f"共检查 {len(dirs)} 个 skill")
    return len(dirs)


def check_manifests():
    print("== 插件清单校验 ==")
    plugin_f = ROOT / ".claude-plugin" / "plugin.json"
    market_f = ROOT / ".claude-plugin" / "marketplace.json"
    plugin = market = None
    for f in (plugin_f, market_f):
        if not f.is_file():
            err(f"缺少 {f.relative_to(ROOT)}")
            continue
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            err(f"{f.name}: JSON 解析失败: {e}")
            continue
        if f is plugin_f:
            plugin = data
        else:
            market = data
    if plugin:
        if not SEMVER_RE.match(str(plugin.get("version", ""))):
            err(f"plugin.json version 不是 semver: {plugin.get('version')!r}")
        skills_path = plugin.get("skills")
        if not skills_path or not (ROOT / skills_path).exists():
            err(f"plugin.json skills 路径不存在: {skills_path!r}")
    if plugin and market:
        if plugin.get("name") != market.get("name"):
            err("plugin.json 与 marketplace.json 的 name 不一致")
        for p in market.get("plugins", []):
            src = p.get("source", "")
            if isinstance(src, str) and src.startswith("./") and not (ROOT / src).exists():
                err(f"marketplace.json plugins.source 路径不存在: {src!r}")
    ok("清单检查完成")


def check_root_files():
    print("== 根文件校验 ==")
    for name in ("README.md", "LICENSE", "install.ps1"):
        if not (ROOT / name).is_file():
            err(f"缺少 {name}")
    ok("根文件检查完成")


if __name__ == "__main__":
    n = check_skills()
    check_manifests()
    check_root_files()
    print()
    if errors:
        print(f"校验失败：{len(errors)} 个问题")
        sys.exit(1)
    print(f"全部通过 ✅（{n} 个 skills）")

