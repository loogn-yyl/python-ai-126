#!/bin/bash
set -euo pipefail

# for 循环
shopt -s nullglob
for f in ~/linux-lab/logs/*.log; do
  echo "$(basename "$f"): $(wc -l < "$f" | tr -d ' ') 行"
done

for i in 1 2 3; do
  echo "第 $i 次"
done

for i in $(seq 1 3); do echo "seq $i"; done

# 逐行读文件：while read 才对
# 对：一次读一行，保留空格
while IFS= read -r line; do
  echo "[$line]"
done < ~/linux-lab/logs/access.log

# 错：for 会把每一行按空格切成词
for line in $(cat ~/linux-lab/logs/access.log); do
  echo "[$line]"
done | head -n 3

# 反例：管道版，变量留不下来
count=0
cat ~/linux-lab/logs/access.log | while read -r line; do
  count=$((count + 1))
done
echo "管道版数出来:$count"

# 正例：重定向版
count=0
while read -r line; do
  count=$((count + 1))
done < ~/linux-lab/logs/access.log
echo "重定向版数出来:$count"

# 运行：./loop.sh
