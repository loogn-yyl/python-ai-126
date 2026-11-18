# no.5
import requests
from requests.exceptions import (
    ConnectionError, HTTPError, Timeout, TooManyRedirects,
)

def fetch(url):
    try:
        r = requests.get(url, timeout=(3, 10))
        r.raise_for_status()
        return r.text
    except Timeout:
        print(f"超时     : {url}")
    except HTTPError as e:
        print(f"状态码错  : {e.response.status_code}")
    except ConnectionError:
        print(f"连不上    : {url}")
    except TooManyRedirects:
        print(f"跳转太多  : {url}")
    return None

print("四种异常各对应一类失败, 抓的时候要分开")
print("顺序也有讲究: ConnectTimeout 既是 Timeout 又是 ConnectionError 的子类")