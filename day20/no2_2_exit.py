# no.2-2
import argparse
import contextlib
import io

parser = argparse.ArgumentParser(prog="logtool")
parser.add_argument("path")
group = parser.add_mutually_exclusive_group()
group.add_argument("-q", "--quiet", action="store_true", help="只输出结果")
group.add_argument("-v", "--verbose", action="store_true", help="打印每一行")

print("只给 -q :", parser.parse_args(["-q", "a.log"]))

err = io.StringIO()
try:
    with contextlib.redirect_stderr(err):
        parser.parse_args(["-q", "-v", "a.log"])
except SystemExit as e:
    print("两个都给: 退出码", e.code)
    print("   ", err.getvalue().strip().splitlines()[-1])