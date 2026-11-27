#!/bin/bash
set -euo pipefail

# 用法：./backup.sh [源目录] [备份目录]
#       KEEP=3 ./backup.sh ~/python-learn ~/backups


SRC="${1:-$HOME/python-learn}"
DEST="${2:-$HOME/backups}"
KEEP="${KEEP:-7}"
STAMP=$(date +%Y%m%d-%H%M%S)
NAME="backup-$(basename "$SRC")-$STAMP.tar.gz"

log() { printf '[%s] %s\n' "$(date +%H:%M:%S)" "$*"; }

# 前置检查
[[ -d "$SRC" ]] || { log "错误：$SRC 不是目录"; exit 1; }
command -v tar >/dev/null || { log "错误：没有 tar"; exit 1; }

mkdir -p "$DEST"

# 打包
log "开始打包：$SRC"
tar -czf "$DEST/$NAME" \
    --exclude="__pycache__" \
    --exclude=".git" \
    --exclude="*.pyc" \
    -C "$(dirname "$SRC")" "$(basename "$SRC")"

log "完成：$DEST/$NAME ($(du -h "$DEST/$NAME" | cut -f1))"

# 清理旧备份
COUNT=$(ls -1 "$DEST"/backup-*.tar.gz 2>/dev/null | wc -l | tr -d ' ')
if [[ "$COUNT" -gt "$KEEP" ]]; then
  log "现有 $COUNT 个备份，保留最近 $KEEP 个"
  ls -1t "$DEST"/backup-*.tar.gz | tail -n +$((KEEP + 1)) | while read -r old; do
    rm -f "$old"
    log "删除旧备份 $(basename "$old")"
  done
fi

log "全部完成"
