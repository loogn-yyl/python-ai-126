#!/bin/bash
set -euo pipefail

TMPFILE=$(mktemp "${TMPDIR:-/tmp}/demo.XXXXXX")
trap 'rm -f "$TMPFILE"; echo "退出时清理：$TMPFILE"' EXIT

echo "临时文件：$TMPFILE"
echo "数据" > "$TMPFILE"
ls -l "$TMPFILE"
