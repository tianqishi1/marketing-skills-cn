# 安装 marketing-skills-cn 到 Codex / Claude Code 技能目录
# 用法: .\install.ps1 -Target codex|claude|both [-Force]
param(
  [ValidateSet('codex','claude','both')] [string]$Target = 'codex',
  [switch]$Force
)
$src = Join-Path $PSScriptRoot 'skills'
$dests = @()
if ($Target -in 'codex','both') { $dests += Join-Path $env:USERPROFILE '.codex/skills' }
if ($Target -in 'claude','both') { $dests += Join-Path $env:USERPROFILE '.claude/skills' }
foreach ($d in $dests) {
  New-Item -ItemType Directory -Force -Path $d | Out-Null
  Get-ChildItem $src -Directory | ForEach-Object {
    $t = Join-Path $d $_.Name
    if ((Test-Path $t) -and -not $Force) { Write-Warning "已存在，跳过（加 -Force 覆盖）: $t"; return }
    if (Test-Path $t) { Remove-Item -LiteralPath $t -Recurse -Force }
    Copy-Item $_.FullName $t -Recurse -Force
    Write-Host "已安装: $t"
  }
}
Write-Host "完成。重启或新开会话后生效。"