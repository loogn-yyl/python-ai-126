# p4_note_txt.py 写文本文件：把 3 行文字写进 note.txt，再读出来逐行打印

with open("note.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")

with open("note.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())