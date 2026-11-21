# no.6-2
import logging
import sys

logging.basicConfig(level=logging.INFO,
                    format="%(levelname)-8s | %(message)s",
                    stream=sys.stderr)      # 日志 -> stderr
log = logging.getLogger("logtool")

log.info("进度, 开始处理")
print("报告正文: 总请求 7 条")
log.info("进度: 结束")