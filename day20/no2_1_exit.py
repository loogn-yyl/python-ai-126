# no.2-1
import argparse
import contextlib
import io

parser = argparse.ArgumentParser(prog="logtool", description="分析 nginx 访问日志")
parser.add_argument("path", help="日志文件路径")
parser.add_argument("-n", "--top", type=int, default=3, help="Top N, 默认 3")
parser.add_argument("--format", choices=["text", "csv", "json"], default="text")

for argv in (["-n", "5"], ["--format", "xml", "a.log"], ["-n", "abc", "a.log"]):
    err = io.StringIO()
    try:
        with contextlib.redirect_stderr(err):
            parser.parse_args(argv)
        print(f"{argv} -> 正常返回")
    except SystemExit as e:
        print(f"{argv} -> 退出码 {e.code}")
        print("   ", err.getvalue().strip().splitlines()[-1])