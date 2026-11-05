[x] 1. 字符串能不能改？"hello"[0] = "H" 会怎样？
     字符串不能改， 会报错TypeError
[x] 2. s[::-1] 是什么？s[1:5] 含不含下标 5？
     s[::-1]倒序， s[1:5]左闭右开， 不含5
[x] 3. b = a 之后改 b，a 会变吗？为什么？
     会变， 只对可变对象成立, 类似c语言指针指向同一对象
[x] 4. sort() 和 sorted() 有什么区别？
     sort() 原地排序， 返回 None； sorted() 返回新列表
[x] 5. 字典取值，d["x"] 和 d.get("x") 差在哪？
     d["x"] 不存在报错 KeyError, d.get("x") 返回 None（或者自己设置的默认值）
[x] 6. for i in len(nums) 为什么报错？
     len() 返回 int， 应该用 for i in nums: 或者 for i in range(len(nums))
[x] 7. enumerate 和 zip 分别解决什么问题？
     enumerate 同时拿序号和元素， zip 并行遍历多个列表（以最短列表为准）
[x] 8. 默认参数写 def f(x=[]) 会出什么事？
     x=[] 只创建一次， 后续调用会累积数据
[x] 9. if __name__ == "__main__" 到底在判断什么？
    判断这个文件是直接运行，还是被import
[x] 10. csv 读出来的数字是 int 还是 str？
     全是 str， 需要 int() 转
