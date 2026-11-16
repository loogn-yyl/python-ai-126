# D017 笔记 · 网络编程

## socket：和 C 一模一样的五个函数
| C | Python | 作用 |
| --- | --- | --- |
| socket(AF_INET, SOCK_STREAM, 0) | socket.socket(socket.AF_INET, socket.SOCK_STREAM) | 创建一个 IPv4 的 TCP 套接字 |
｜connect(fd, &addr, len) | s.connect((host, port)) | 发起三次握手 |
| send(fd, buf, n, 0) | s.sendall(b"...") | 发数据 |
| recv(fd, buf, n, 0) | s.recv(4096) | 收数据 |
| close(fd) | s.close() | 关闭(或 with 自动关) |
- 不用传长度、不用 malloc 缓冲、不用 htons
- settimeout 必设（C 里是 setsockopt(SO_RCVTIMEO)）

## HTTP 报文
- 请求 = 请求行 + 头 + 空行 + 正文  
  GET / HTTP/1.1  
  Host: example.com        ★HTTP/1.1 必填，否则 400  
  Connection: close  
  (空行)                   ★是 \r\n\r\n 两个换行，漏了服务器一直等
- 响应 = 状态行 + 头 + 空行 + 正文  
  HTTP/1.1 200 OK  
  Content-Type: ...; charset=utf-8  
  (空行)
- partition("\r\n\r\n") 切头部和正文（比 split 好：只切第一个）

## 手写 socket 的六个坑（requests 全替你处理）
| 坑 | 后果 |
| --- | --- |
| 不设 timeout | 永久阻塞 |
| sendall 传 str | TypeError，必须 encode |
| 不用 with | 句柄泄漏 |
| recv 只调一次 | 拿到半截（TCP 是字节流）|
| bytes 反复 + | O(n²) |
| 硬 decode utf-8 | 服务器发 gbk 就崩 |

## requests
- r.status_code / r.text / r.content / r.json() / r.headers / r.url
- ★4xx 5xx 不抛异常，要 raise_for_status()
- ★r.encoding 可能猜成 ISO-8859-1 → 手动改 r.encoding = r.apparent_encoding  
  （改了之后重新读 r.text 才生效；已存进变量的不会变）

## 六个必设
| 必设项 | 作用 |
| --- | --- |
| timeout=(3, 10) | 连接 3s / 读取 10s，默认无超时是最大的坑 |
| headers | User-Agent 不设，很多站点 403 |
| raise_for_status | 否则 404 页面被当正常内容解析 |
| params | 自动转义 |
| verify=True | 别关 |
| Session() | 复用连接 + 保持登录态 |

## 异常四类
- Timeout / HTTPError / ConnectionError / TooManyRedirects
- 最后用 RequestException 兜底 → 函数永远不抛异常
- 超时可重试，500 重试没用 → 必须分类
- 顺序也有讲究：Timeout 和 ConnectionError 都是 ConnectionError 的子类关系要理清

## 抓标题
- r"<title[^>]*>(.*?)</title>" + re.S | re.I
- " ".join(s.split()) 压掉所有连续空白（strip 只去两头）
- urlparse / parse_qs；parse_qs 的值永远是列表

## 纪律
- 批量任务收集失败列表，别 continue 了事
- 加总数自检：sum(统计) == 输入条数
- 计时结论只记量级，别记具体数字

## 踩过的坑
- AF_INET 就是数字 2，SOCK_STREAM 就是数字 1  
  这些常量在 C 里也是 #define 出来的整数，Python 只是把它们做成了模块属性  
  所以 print(s.family) 输出 2 
- partition("\r\n\r\n") 原始文本切成「头部 / 分隔符 / 正文」三段, 比 split 好用

## 遇到乱码，第一件事是盯住这两行
- print(r.encoding)          -> 如果是 ISO-8859-1 或 None，基本就是它  
  r.encoding = "utf-8"       -> 手动改，然后再读 r.text
- 更稳的做法：从正文里找声明   
  requests 有个内置推断，但它只在 headers 没写 charset 时才用  
  手动指定最可靠：r.encoding = r.apparent_encoding
- 顺序记牢：  
  1. r.encoding       —— headers 里写的，可能是错的  
  2. r.apparent_encoding —— 从正文猜的，比较慢但通常更准  
  3. 都不对 —— 那就自己试 gbk / utf-8-sig
- print("改 r.encoding 之后必须重新读 r.text，值不会自动刷新")