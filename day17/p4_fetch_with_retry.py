# p4_fetch_with_retry.py 给抓取加重试：失败时重试 3 次，每次间隔递增（1s / 2s / 4s）。别真 sleep，把要等的时间打印出来就行
def fetch_with_retry(url, retries=3):
    for attempt in range(1, retries + 1):
        ok = attempt == 3 and "bad" not in url
        if ok:
            print(f"第 {attempt} 次成功: {url}")
            return "内容"
        if attempt < retries:
            print(f"第 {attempt} 次失败, 等 {2 ** (attempt - 1)} 秒后重试")
        else:
            print(f"第 {attempt} 次失败, 已是最后一次")
    print("放弃")
    return None

print(fetch_with_retry("https://example.com"))
print()
print(fetch_with_retry("https://bad.example"))