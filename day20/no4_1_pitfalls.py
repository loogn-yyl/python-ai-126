# no.4-1
import logging
import sys

logging.basicConfig(level=logging.INFO,
                    format="%(levelname)-8s | %(message)s",
                    stream=sys.stdout)
logging.getLogger("logtool").info("第一次配置: INFO 级别生效")

# 第二次调用, 所有参数都被忽略
logging.basicConfig(level=logging.DEBUG,
                    format=">>> %(message)s",
                    stream=sys.stdout)
log = logging.getLogger("logtool")
log.info("第二次 basicConfig 被忽略, 格式还是第一次的")
log.debug("级别也没变成 DEBUG, 这行不显示")
print()
print("根 logger 上的 handler 数量:", len(logging.getLogger().handlers))