# 线程执行的函数
import threading
import time
from asyncio import as_completed
import asyncio

from distributed._concurrent_futures_thread import ThreadPoolExecutor
from sphinx.util import requests


# def add(n1, n2):
#     v = n1 + n2
#     print('add :', v, ', tid:', threading.currentThread().ident)
#     time.sleep(n1)
#     return v


# 通过submit把需要执行的函数扔进线程池中.
# submit 直接返回一个future对象
# ex = ThreadPoolExecutor(max_workers=3)  # 制定最多运行N个线程
# f1 = ex.submit(add, 2, 3)
# f2 = ex.submit(add, 2, 2)
# print('main thread running')
# print(f1.done())  # done 看看任务结束了没
# print(f1.result())  # 获取结果 ,阻塞方法


# URLS = ['http://www.baidu.com', 'http://www.qq.com', 'http://www.sina.com.cn']
# def get_html(url):
#     print('thread id:',threading.currentThread().ident,' 访问了:',url)
#     return requests.get(url)            #这里使用了requests 模块
# ex = ThreadPoolExecutor(max_workers=3)
# res_iter = ex.map(get_html,URLS)        #内部迭代中, 每个url 开启一个线程
# for res in res_iter:                    #此时将阻塞 , 直到线程完成或异常
#     print('url:%s ,len: %d'%(res.url,len(res.text)))


#这是一个简单的 as_completed  todo  为什么报错了？？
URLS = ['http://www.baidu.com', 'http://www.qq.com', 'http://www.sina.com.cn']
def get_html(url):
    time.sleep(1)
    print('thread id:',threading.currentThread().ident,' 访问了:',url)
    return requests.get(url)            #这里使用了requests 模块
ex = ThreadPoolExecutor(max_workers=3)   #最多3个线程
future_tasks = [ex.submit(get_html,url) for url in URLS] #创建3个future对象
print("--------")
print(future_tasks)

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

for future in as_completed(future_tasks):       #迭代生成器
    try:
        resp = future.result()
    except Exception as e:
        print('%s'%e)
    else:
        print('%s has %d bytes!'%(resp.url, len(resp.text)))



# def mark_done(future, result):
#     print('setting future result to {!r}'.format(result))
#     future.set_result(result)
#
#
# event_loop = asyncio.get_event_loop()
# try:
#     all_done = asyncio.Future()
#
#     print('scheduling mark_done\n')
#     print("1--------")
#     event_loop.call_soon(mark_done, all_done, 'the result')
#
#     print('entering event loop\n')
#     print("2--------")
#     result = event_loop.run_until_complete(all_done)
#     print('returned result: {!r}'.format(result))
# finally:
#     print('closing event loop')
#     event_loop.close()
#
# print('future result: {!r}'.format(all_done.result()))


# import time
# import asyncio
#
# now = lambda : time.time()
#
# async def do_some_work(x):
#     print("waiting:", x)
#
# start = now()
# # 这里是一个协程对象，这个时候do_some_work函数并没有执行
# coroutine = do_some_work(2)
# print(coroutine)
# print("-------")
# #  创建一个事件loop
# loop = asyncio.get_event_loop()
# # 将协程加入到事件循环loop
# loop.run_until_complete(coroutine)
#
# print("Time:",now()-start)

# async def test2(i):
#      r = await other_test(i)
#      print(i,r)
#
# async def other_test(i):
#  r = requests.get(i)
#  print(i)
#  await asyncio.sleep(4)
#  print(time.time()-start)
#  return r
#
# url = ["https://segmentfault.com/p/1210000013564725",
#         "https://www.jianshu.com/p/83badc8028bd",
#         "https://www.baidu.com/"]
#
# loop = asyncio.get_event_loop()  # 创建一个循环
# task = [asyncio.ensure_future(test2(i)) for i in url]
# start = time.time()
# loop.run_until_complete(asyncio.wait(task))  # 检测task运行情况并返回结果
# endtime = time.time()-start
# print(endtime)
# loop.close()
@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()