## argparse 三种形态
| 形态 | 表达式 | 参数 |
| --- | --- | --- |
| 位置参数 | add_argument("path") | args.path |
| 选项带值 | add_argument("-n","--top",type=int) | args.top   ★名字取长选项 |
| 开关 | add_argument("-q",action="store_true") | args.quiet |
| 选择 | add_argument("--format",choices=[...]) | args.format |
| 计数 | add_argument("-v",action="count",default=0) | ★default 不写是 None |

## argparse 替你做的三件事
校验（缺参 / 类型 / choices / 互斥）→ 报错到 stderr → 退出码 2  
-h 自动生成 → 退出码 0   
★ 退出码分工：0 成功 / 1 业务失败 / 2 用法错误（2 是 argparse 专用）   
★ 生产代码别 except SystemExit；argv=None 的形参是留给测试的

## logging 五个级别
DEBUG 10  INFO 20  WARNING 30  ERROR 40  CRITICAL 50  
★ level 是水位线，低于它的连字符串都不拼  

## logging 三行配置
basicConfig(level=..., format="%(levelname)-8s | %(message)s", stream=sys.stderr)  
★ -8s 左对齐补 8 格，日志才成列  
★ 别加 %(asctime)s：输出就不可复现了  

## 三个坑
1 basicConfig 只生效一次，第二次静默忽略 → 只在入口调一次  
  被 import 的模块里只写 getLogger(__name__)  
2 不配置时默认 WARNING，info 全丢，格式也没有  
3 logger 是树：logtool.report 的父级是 logtool，消息向上冒泡  
  → 根配好了，子 logger 自动有格式

## 为什么不用 print
给排错看的过程 → log；给人看的结果 → print  
日志走 stderr，结果走 stdout  
→ python x.py > report.txt 得到的只有干净正文  

## 拼装顺序（今天最重要的一页）
parse_args → load(rows, bad) → build(dict) → render_* → print  
★ 先算成 dict，最后才决定怎么打印：换格式不用动中间逻辑  
★ 过滤在 build 之前：换的是数据，不是打印方式  
★ Top N 必须有第二排序键，否则顺序随机  
★ "10.0.0.11" < "10.0.0.9"（字符串比较），要真实大小得用 ip_address  
★ 共用的函数别写死某一种数据的规则，用 key= 从外面传  

## 出口一行
if __name__ == "__main__":  
    sys.exit(main())  
★ 不写 sys.exit()，return 1 就只是被丢掉的值，进程照样退 0

## 踩过的坑
- 使用 group = p.add_mutually_exclusive_group() + grooup.add_argument(...) 保证 -q 和 -v 互斥
- logging.basicConfig 传了 handlers=[...] 之后，format= 和 stream= 会被静默忽略——格式得自己 setFormatter 到每个 handler 上
- 一个函数被两种数据共用时，别把「某一种数据的规则」写死在函数里，用参数（或者 key=）从外面传进去。改完再跑一次