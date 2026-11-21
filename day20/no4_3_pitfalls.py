# no.4-3
import logging
import sys

logging.basicConfig(level=logging.INFO,
                    format="%(name)-14s | %(levelname)-8s | %(message)s",
                    stream=sys.stdout)
root = logging.getLogger()
app = logging.getLogger("logtool")
sub = logging.getLogger("logtool.report")

print("root 的名字:", repr(root.name))
print("app  的名字:", app.name, "| 父级:", app.parent.name)
print("sub  的名字:", sub.name, "| 父级:", sub.parent.name)
print()
app.info("主模块的消息")
sub.info("子模块的消息, 冒泡上去了")