#!/bin/bash
set -eEuo pipefail

FAIL_LINE=?
TMPDIR_X=$(mktemp -d)
echo "TMPDIR_X=$TMPDIR_X"

on_err() { FAIL_LINE=${BASE_LINENO[0]}; }
trap on_err ERR

cleanup() {
  local rc=$?
  rm -rf "$TMPDIR_X"
  if [[ $rc -ne 0 ]]; then
    echo "失败于第 ${FAIL_LINE} 行，退出码 $rc" >&2
  fi
  return 0
}
trap cleanup EXIT
