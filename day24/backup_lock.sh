LOCK="/tmp/backup.lock"

if ! mkdir "$LOCK" 2>/dev/null; then
  echo "已有备份在跑，本次跳过" >&2
  exit 1
fi
trap 'rmdir "$LOCK"' EXIT
