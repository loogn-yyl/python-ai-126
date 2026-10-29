# p3_wordCount.py 词频统计：输入一句英文，输出每个单词出现几次（用 dict.get）

sentence = input("请输入一句英文: ")

freq = {}

for w in sentence.split():
    freq[w] = freq.get(w, 0) + 1

for k, v in freq.items():
    print(k, v)