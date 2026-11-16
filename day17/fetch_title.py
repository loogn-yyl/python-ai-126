import re
import sys

import requests
from requests.exceptions import HTTPError, RequestException, Timeout

TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.S | re.I)
UA = {"User-Agent": "Mozilla/5.0 (compatible; learn-bot/1.0)"}

def fetch_title(url, timeout=(3, 10)):
    """返回标题字符串; 失败返回 None (不抛异常, 让调用方决定怎么办)"""
    try:
        r = requests.get(url, headers=UA, timeout=timeout)
        r.raise_for_status()
    except Timeout:
        print(f"[超时] {url}", file=sys.stderr)
        return None
    except HTTPError as e:
        print(f"[HTTP {e.response.status_code}] {url}", file=sys.stderr)
        return None
    except RequestException as e:
        print(f"[失败] {url} -> {type(e).__name__}", file=sys.stderr)
        return None

    if not r.encoding or r.encoding.lower() == "iso-8859-1":
        r.encoding = r.apparent_encoding
    m = TITLE.search(r.text)
    return " ".join(m.group(1).split()) if m else None

if __name__ == "__main__":
    for u in sys.argv[1:]:
        t = fetch_title(u)
        print(f"{u}\n    -> {t}")