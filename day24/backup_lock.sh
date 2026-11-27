#!/bin/bash
set -euo pipefail

LOCK="/tmp/backup.lock"

if ! mkdir "$LOCK" 2>/dev/null; then
  echo "已有备份在跑，本次跳过" >&2
  exit 1
fi
trap 'rmdir "$LOCK"' EXIT

SRC="${1:-$HOME/python-learn}"
DEST="${2:-$HOME/backups}"
KEEP="${KEEP:-7}"
STAMP=$(date +%Y%m%d-%H%M%S)
base=$(basename "$SRC")
NAME="backup-$base-$STAMP.tar.gz"

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
    -C "$(dirname "$SRC")" "$base"

log "完成：$DEST/$NAME ($(du -h "$DEST/$NAME" | cut -f1))"

# 清理旧备份：只清同一个来源的，别的来源不动
shopt -s nullglob
mine=("$DEST"/backup-"$base"-*.tar.gz)
COUNT=${#mine[@]}
if [[ "$COUNT" -gt "$KEEP" ]]; then
  log "来源 $base，现有 $COUNT 个备份，保留最近 $KEEP 个"
  ls -1t "${mine[@]}" | tail -n +$((KEEP + 1)) | while read -r old; do
    rm -f "$old"
    log "删除旧备份 $(basename "$old")"
  done
fi

log "全部完成"