# D016 笔记 · 正则实战与文本处理

## re.M 与 re.S 管的是两件不同的事
re.M : 让 ^ $ 认「每一行」的开头结尾（不加只认整段文本）
re.S : 让 . 能吃换行（DOTALL）
两个都要 → re.M | re.S
用 re.S 时几乎总要配非贪婪 .*?，否则跨过所有成对标签

## csv / json
csv.DictReader → 字典列表，★值全是字符串，算数前必须 int()
csv.DictWriter → 必须 writeheader()，否则第一行数据当表头
真写文件：open(path, "w", newline="", encoding="utf-8")   ★newline="" 只在 Windows 有影响
json.dumps(obj, ensure_ascii=False)  ★不加中文变 \u4e2d\u6587
dump/load 收文件对象，dumps/loads 收字符串（s = string）
json 会还原数字/布尔类型，csv 不会

## 编码
- 字符 ≠ 字节。bytes → str 叫 decode，str → bytes 叫 encode
- 程序内部一律 str，只有进出文件和网络才是 bytes
- UnicodeDecodeError = 这个字节按该编码的规则解释不通
- 常见：utf-8（3 字节/汉字）/ gbk（2 字节）/ utf-8-sig（带 BOM）
- BOM：Excel 另存的 csv 几乎都带，读出来第一个字段前面粘了 \ufeff
  → 表现：看着一样，== 是 False，row["ip"] 却 KeyError
  → 解法：读 csv 一律 encoding="utf-8-sig"（对无 BOM 也安全）
- errors 三档：strict（默认，推荐）/ replace（替换成 \ufffd）/ ignore（★静默删掉，危险）
  实测：4 个汉字用 ignore 只剩 1 个字符，不报错

## 统计
- Counter(可迭代) 计数；most_common(n) 取前 n，次数相同按首次出现顺序
- Counter 只会计数，求和要自己 += 或用 defaultdict(int)
- 降序：sorted(items, key=lambda kv: -kv[1]) 或 reverse=True
- 字符串格式化：{x:.1%} 自动 ×100 加百分号
- startswith(("4", "5")) 用元组；startswith("4" or "5") 只判 "4"

## 健壮性
- 除零：rate = errors / total if total else 0
- 空输入必须能跑通，别假设总有数据
- 测试 csv 输出用 io.StringIO()，不用真写文件

## 踩过的坑
- （写你真实遇到的）