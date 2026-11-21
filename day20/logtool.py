# no.7-2
import argparse
import logging
import sys

def parse_args(argv=None):
    p = argparse.ArgumentParser(prog="logtool", description="分析 nginx 访问日志")
    p.add_argument("path", help="日志文件路径")
    p.add_argument("-n", "--top", type=int, default=3, help="Top N, 默认 3")
    p.add_argument("-q", "--quiet", action="store_true", help="不打进度日志")
    p.add_argument("--format", choices=["text", "csv", "json"], default="text")
    return p.parse_args(argv)    # 若 argv=None 走 sys.argv

def setup_log(quiet):
    logging.basicConfig(
        level=logging.WARNING if quiet else logging.INFO,
        format="%(levelname)-8s | %(message)s",
        stream=sys.stderr,    # 日志走 stderr, 结果走 stdout
    )
    return logging.getLogger("logtool")

def main(argv=None):
    args = parse_args(argv)
    log = setup_log(args.quiet)
    log.info("开始处理 %s", args.path)
    code = run(args)
    log.info("结束, 退出码 %d", code)
    return code

if __name__ == "__main__":
    sys.exit(main())