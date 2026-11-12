# D006 笔记

## 异常处理
- try / except / else / finally
- else = 没出错时执行；finally = 无论如何执行
- **不要裸 except + pass**，要写具体异常类型
- 不知道怎么办的异常，就让它崩 —— 崩掉比默默跑错好
- raise 主动抛错，会中断当前函数并向上冒泡
- 自定义异常：class MyError(Exception): pass 两行就够

## 常见异常
- ValueError 值不对（int("abc")）
- TypeError 类型不对
- KeyError 字典没这个 key
- IndexError 下标越界
- FileNotFoundError 文件不存在
- ZeroDivisionError 除以 0

## 读报错
- traceback 从下往上读：最后一行是「什么错」，往上是「在哪错的」

## 文件
- 一律 with open(...)，自动关文件
- **encoding="utf-8" 必须写**，否则跨平台乱码
- "w" 会清空文件！追加用 "a"
- 逐行读记得 strip()，去掉 \n
- csv 写文件要 newline=""

## CSV
- csv.reader 读出全是字符串，数字要自己转
- csv.DictReader 按列名取，更推荐
- 有坏数据要 skip + 计数，不要让整个流程崩

## JSON
- dump / load 对文件；dumps / loads 对字符串
- ensure_ascii=False 中文才不转义
- JSON 保留类型，CSV 不保留
- json 的 true/false/null → Python 的 True/False/None

## C 对比
- 错误码 return -1 vs raise 异常自动冒泡
- 必须 fclose() vs with 自动关闭

## 踩过的坑
- open("scores.csv", "w", newline="", encoding="utf-8") 中    
  newline="" 必须加, 关掉 Python 自己的换行符转换, 交给 csv 模块
- json.dump(data, f, ensure_ascii=False, indent=2) 中  
  indent=2 表示每个层级缩进2个空格, 并且每个元素都换行
- 注意 json.dump 和 json.dumps 是两个函数