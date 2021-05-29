import threading
import time
from asyncio import as_completed
from concurrent.futures import ThreadPoolExecutor

# 线程执行的函数
# def add(n1,n2):
#     v = n1 + n2
#     print('add :', v , ', tid:',threading.currentThread().ident)
#     time.sleep(n1)
#     return v
# #通过submit把需要执行的函数扔进线程池中.
# #submit 直接返回一个future对象
# ex = ThreadPoolExecutor(max_workers=3)      #制定最多运行N个线程
# f1 = ex.submit(add,2,3)
# f2 = ex.submit(add,2,2)
# print('main thread running')
# print("------------")
# print(f1.done())                            #done 看看任务结束了没
# print(".............")
# print(f2.result())                          #获取结果 ,阻塞方法
# print(".............")
# print(f1.result())                          #获取结果 ,阻塞方法


# 下面是map 方法的简单使用.  注意:map 返回是一个生成器 ,并且是*有序的*
from sphinx.util import requests

# URLS = ['http://www.baidu.com', 'http://www.qq.com', 'http://www.sina.com.cn']


# def get_html(url):
#     print('thread id:', threading.currentThread().ident, ' 访问了:', url)
#     return requests.get(url)  # 这里使用了requests 模块
#
#
# ex = ThreadPoolExecutor(max_workers=3)
# res_iter = ex.map(get_html, URLS)  # 内部迭代中, 每个url 开启一个线程
# for res in res_iter:  # 此时将阻塞 , 直到线程完成或异常
#     print('url:%s ,len: %d' % (res.url, len(res.text)))
#as_completed 完整的例子
#as_completed 返回一个生成器，用于迭代， 一旦一个线程完成(或失败) 就返回
URLS = ['http://www.baidu.com', 'http://www.qq.com', 'http://www.sina.com.cn']
def get_html(url):
    time.sleep(1)
    print('thread id:',threading.currentThread().ident,' 访问了:',url)
    return requests.get(url)            #这里使用了requests 模块
ex = ThreadPoolExecutor(max_workers=3)   #最多3个线程
future_tasks = [ex.submit(get_html,url) for url in URLS]    #创建3个future对象
for future in as_completed(future_tasks):       #迭代生成器
    try:
        resp = future.result()
    except Exception as e:
        print('%s'%e)
    else:
        print('%s has %d bytes!'%(resp.url, len(resp.text)))
"""
thread id: 5160  访问了: http://www.baidu.com
thread id: 7752  访问了: http://www.sina.com.cn
thread id: 5928  访问了: http://www.qq.com
http://www.qq.com/ has 240668 bytes!
http://www.baidu.com/ has 2381 bytes!
https://www.sina.com.cn/ has 577244 bytes!
"""