#!/bin/bash
set -euo pipefail
echo "脚本名:$0"
echo "参数个数:$#"
echo "全部参数（带引号）:$@"
echo "第一个:$1"
shift
echo "shift 之后第一个:$1"
# 执行：bash args.sh one two three
