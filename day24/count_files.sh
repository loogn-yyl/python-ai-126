#!/bin/bash
set -euo pipefail
dir="${1:?用法：count_files.sh 目录}"
[[ -d "$dir" ]] || { echo "不是目录：$dir" >&2; exit 1; }

find "$dir" -type f 2>/dev/null | while IFS= read -r f; do
  base=${f##*/}
  ext=${base##*.}
  if [[ "$base" == *.* && "$base" != .* && -n "$ext" ]]; then
    echo "$ext"
  else
    echo "（无扩展名）"
  fi
done | sort | uniq -c | sort -k1,1nr -k2,2
