#!/bin/bash
set -euo pipefail
dir="${1:?用法：count_py 目录}"
[[ -d "$dir" ]] || { echo "不是目录：$dir" >&2; exit 1; }
n=$(find "$dir" -name "*.py" -type f | wc -l | tr -d ' ')
echo "$dir 下有 $n 个 .py 文件"
