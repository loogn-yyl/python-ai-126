# D004 笔记

## 流程控制
- if / elif / else, 冒号 + 缩进, 没有 {} 和 ()
- and / or / not, 不是 && || !
- 缩进是语法不是排版, 混用 Tab 和空格会 IndentationError

## 真值判断
- 假: 0 / "" / [] / {} / set() / None / False
- 所以 if nums: 等价于 if len(nums) > 0:
- 但 0 和 None 要区分时用 if x is not None:

## 循环
- while 和 C 一样, 但没有 ++ / -- , 要写 n += 1
- do-while 不存在, 用 while True + break
- for 遍历元素, 不是数下标：for x in nums
- range(n) 左闭右开, range(5) 是 0~4
- enumerate 拿序号, zip 并行遍历
- break 整个结束, continue 跳过本次
- for-else 表示「没被 break 打断」, 替代 C 里的 flag 变量

## 推导式
- [x * x for x in range(5)]
- if 在后面 = 过滤; if-else 在前面 = 每个都转换
- () 是生成器, 用时才求值, 不占内存

## C 对比
- for (i=0;i<n;i++) → for i in range(n)
- arr[i] 遍历 → for x in arr
- 带下标 → enumerate
- 两个数组 → zip
- n++ 在 Python 里等于 n, 不会自增, 要用 i += 1 

## 踩过的坑
- print("") 无显示, print(repr("")) 才显示 ""
- "".join(row), 把列表 row 元素加入字符空串中