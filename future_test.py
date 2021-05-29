from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import requests
URLS = ['http://www.163.com', 'https://www.baidu.com/', 'https://github.com/']
def load_url(url):
        req= requests.get(url, timeout=60)
        print('%r page is %d bytes' % (url, len(req.content)))
executor = ThreadPoolExecutor(max_workers=3)
executor.map(load_url,URLS)
print('主线程结束')
# with ThreadPoolExecutor(max_workers=2) as executor:
#     future = executor.submit(pow, 323, 1235)
#     print(future.result())