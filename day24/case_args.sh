#!/bin/bash
set -euo pipefail

while [[ $# -gt 0 ]]; do
  case "$1" in
    -v|--verbose) VERBOSE=1; shift ;;
    -o|--output)  OUT="${2:?选项 -o 需要一个参数}"; shift 2 ;;
    -h|--help)    echo "用法：$0 [-v] [-o 文件]"; exit 0 ;;
    *)            echo "未知参数：$1" >&2; exit 2 ;;
  esac
done
echo "verbose=${VERBOSE:-0} output=${OUT:-（未指定）}"
