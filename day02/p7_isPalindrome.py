# isPalindrome.py 判断回文：输入一个字符串，判断正着读和反着读是否一样，输出「是回文」或「不是回文」

s = input("请输入字符串: ")

if s == s[::-1] :
    print("是回文")
else :
    print("不是回文")