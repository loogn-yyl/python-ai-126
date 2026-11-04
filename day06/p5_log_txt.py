# p5_log_txt.py 追加日志：用 "a" 模式往 log.txt 追加 3 条记录，每次追加一条，跑两次看文件内容是否累加

for i in range(3):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"第 {i + 1} 条记录\n")

print("追加完成, 再跑一次会继续累加")