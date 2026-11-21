# no.3
import logging
import sys

logging.basicConfig(
    level=logging.WARNING,
    format="%(levelname)-8s | %(name)s | %(message)s",
    stream=sys.stdout,
)
log = logging.getLogger("logtool")

log.debug("debug 看不到")
log.info("info 也看不到")
log.warning("warning 看得到")
log.error("error 看得到")
log.critical("critical 看得到")
print()
print("有效级别:", log.getEffectiveLevel())