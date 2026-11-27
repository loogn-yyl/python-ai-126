#!/bin/bash
set -euo pipefail

if [[ $# -eq 0 ]]; then
  echo "用法：dir_size.sh 一组目录（空格隔开；无参数遍历当前目录）"
  set -- .
fi

for dir in "$@"; do
  if [[ ! -d "$dir" ]]; then
    echo "跳过（不是目录）：$dir" >&2
    continue
  fi
  echo "$(basename "$dir") $(du -sh "$dir" | cut -f1)"
done

