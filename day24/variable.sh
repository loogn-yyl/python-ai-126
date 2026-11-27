#!/bin/bash

# 赋值时不能有空格
name="loogn"        # 对
count=3             # 对
# name = "loogn"    # 错！shell 会把 name 当成命令名去执行
dir=/tmp/mydir
echo "$name 有 $count 个文件，目录 $dir"

# $var 和 ${var}：什么时候必须加花括号
file="report"
echo "$file.txt"        # 正常：点不是变量名字符，$file 到点就结束
echo "$file_2026"       # 出错：shell 去找一个叫 file_2026 的变量（不存在）
echo "${file}_2026"     # 正确：花括号划清边界

# 命令替换与算术
today=$(date +%Y-%m-%d)
n=$(ls | wc -l | tr -d ' ')
echo "今天 ${today}，当前目录有 ${n} 项"

a=7
b=2
echo $((a / b))        # 整数除法
echo $((a % b))
echo $((a * b))

# 默认值与只读
log_dir="${LOG_DIR:-$HOME/logs}"
echo "$log_dir"

readonly MAX=7
# MAX=8   # 会报 MAX: readonly variable

echo "脚本名 $0"
echo "第一个参数 ${1:-（没给）}"
echo "参数个数 $#"

# 运行：./variable.sh
