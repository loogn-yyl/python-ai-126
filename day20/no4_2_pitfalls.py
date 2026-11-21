# no.4-2
import logging

log = logging.getLogger("logtool")
log.info("这行不会出现")
log.warning("只有这行会出来")
print("上面没有 INFO, 就是默认级别 WARNING 在拦")