# p3_ScoreError.py 成绩校验：自定义 ScoreError，分数不在 0–100 之间时 raise，写个 try 接住

class ScoreError(Exception):
    pass

def check(score):
    if score > 100 or score < 0:
        raise ScoreError("分数不在 0-100 之间")
    return score

try:
    check(-1)
except ScoreError as e:
    print("校验失败:", e)