#!/bin/bash
set -uo pipefail

command -v nc >/dev/null || { echo "缺少 nc，先 brew install netcat"; exit 1; }

fail=0
check() {
  local name="$1"; shift
  if "$@" >/dev/null 2>&1; then
    printf '  OK   %s\n' "$name"
  else
    printf '  FAIL %s\n' "$name"; fail=1
  fi
}

check "静态目录存在"   test -d /var/www/html
check "80 端口在监听"  nc -z -w 2 127.0.0.1 80
check "nginx 进程在跑" pgrep -x nginx

[[ $fail -eq 0 ]] && echo "全部通过" || { echo "有检查未通过"; exit 1; }
