# p5_name_group.py 命名分组版再写一次：把第 4 题改成命名分组 + \g<name> 的写法，输出成 13.11.2026
import re

s = "2026-11-13 发布, 2026-12-01 更新"
print("命名版:", re.sub(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})",
      r"\g<day>.\g<month>.\g<year>", s))