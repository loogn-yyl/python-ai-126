# no.1
import argparse

parser = argparse.ArgumentParser(prog="logtool", description="分析 nginx 访问日志")
parser.add_argument("path", help="日志文件路径")
parser.add_argument("-n", "--top", type=int, default=3, help="Top N, 默认 3")
parser.add_argument("-q", "--quiet", action="store_true", help="只输出结果, 不打进度")
parser.add_argument("--format", choices=["text", "csv", "json"], default="text")

args = parser.parse_args(["-n", "5", "--format", "json", "access.log"])
print(args)
print("path   =", args.path)
print("top    =", args.top)
print("quiet  =", args.quiet)
print("format =", args.format)
print()
print("只给位置参数:", parser.parse_args(["a.log"]))