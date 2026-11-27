#!/bin/bash
set -euo pipefail

# 条件判断：[ ] 里的空格不是排版，是语法
f=~/linux-lab/logs/access.log

if [ -f "$f" ]; then
  echo "是文件，行数：$(wc -l < "$f" | tr -d ' ')"
else
  echo "不存在：$f"
fi

if [ -d ~/linux-lab ]; then echo "目录存在"; fi
# set -u 下：未定义 ≠ 空，必须给默认值，因此不能用 ${UNSET_VAR}
if [ -z "${UNSET_VAR:-}" ]; then echo "变量是空的"; fi

# case：多重判断比 if-elif 干净
mode="${1:-text}"
case "$mode" in
  text|csv)  echo "输出格式：$mode" ;;
  json)      echo "输出格式：JSON" ;;
  -h|--help) echo "用法: demo.sh [text|csv|json]" ;;
  *)         echo "不认识的参数：$mode" >&2; exit 2 ;;
esac

# 运行：./condition.sh
# ./condition.sh; echo "rc=$?"            # text + 5 行 + 目录存在 + 变量是空的 + 输出格式：text
# ./condition.sh json; echo "rc=$?"       # 输出格式：JSON
# ./condition.sh --help; echo "rc=$?"     # 用法: ...
# ./condition.sh xx; echo "rc=$?"         # 不认识的参数：xx（走 stderr）+ rc=2
