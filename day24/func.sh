#!/bin/bash
set -euo pipefail

log() {
  local level="$1"; shift
  printf '[%s] %-5s %s\n' "$(date +%H:%M:%S)" "$level" "$*"
}

is_log_file() {
  [[ "$1" == *.log ]]
}

log INFO "开始处理"
if is_log_file "access.log"; then
  log INFO "是日志文件"
else
  log INFO "不是日志文件"
fi
log ERROR "演示一条错误"
get_size() {
  du -sh "$1" | cut -f1
}
size=$(get_size ~/linux-lab/logs)
echo "logs 大小：$size"

# 运行：bash func.sh
