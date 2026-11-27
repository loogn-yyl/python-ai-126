#!/bin/bash
set -euo pipefail
f="${1:?用法：is_modify.sh 文件名}"
[[ -f "$f" ]] || { echo "不是文件：$f" >&2; exit 1; }
if [[ -n "$(find "$f" -mtime -1 -print -quit  2>/dev/null)" ]]; then
  echo "最近一天改过"
else
  echo "超过一天没动"
fi
