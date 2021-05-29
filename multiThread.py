import asyncio

# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # print("----"+str(loop))   # todo  这一行打印出来的会是啥？？
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()



# def consumer():
#     r = ''
#     while True:
#         n = yield r  # 执行的中断点
#         if not n:
#             return
#         print('[消费者] 正在消费:{0}'.format(n))
#         r = '200 人民币'
#
#
# def produce(c):
#     c.send(None)  # 启动消费者（生成器）——实际上是函数调用，只不过生成器不是直接象函数那般调用的   todo  启动这个generator必须要send一下吗？
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[生产者] 正在生产:{0}'.format(n))
#         r = c.send(n)  # 给消费者传入值——实际上也是函数调用
#         print('[生产者] 消费者返回:{0}'.format(r))
#         print('-------------------------------------------------')
#     c.close()
#
#
# c = consumer()  # 构造一个生成器
# produce(c)



import time
# 定义一个消费者，他有名字name
# 因为里面有yield，本质上是一个生成器
def consumer(name):
    print(f'{name}  准备吃包子啦！,呼吁店小二')
    while True:
        baozi = yield  # 接收send传的值，并将值赋值给变量baozi
        print(f'包子 {baozi + 1} 来了,被 {name} 吃了！')


# 定义一个生产者，生产包子的店家，店家有一个名字name,并且有两个顾客c1 c2
# def producer(name, c1, c2):
#     # c1.send(None)
#     # c2.send(None)
#     # next(c1)  # 启动生成器c1   #todo  为什么一开始没有接收send的值时，后面的while True没有执行？？
#     # next(c2)  # 启动生成器c2
#     print(f'{name} 开始准备做包子啦！')
#     for i in range(5):
#         time.sleep(1)
#         print(f'做了第{i + 1}包子，分成两半,你们一人一半')
#         c1.send(i)
#         c2.send(i)
#         print('------------------------------------')


# c1 = consumer('张三')  # 把函数变成一个生成器
# c2 = consumer('李四')
# producer('店小二', c1, c2)


# import time
# import asyncio
# async def say_after_time(delay, what):
#     await asyncio.sleep(delay)
#     print(what)
#
#
# async def main():
#     print(f"开始时间为： {time.time()}")
#     await say_after_time(1, "hello")
#     await say_after_time(2, "world")
#     print(f"结束时间为： {time.time()}")
#
#
# loop = asyncio.get_event_loop()  # 创建事件循环对象
# # loop=asyncio.new_event_loop()   #与上面等价，创建新的事件循环
# loop.run_until_complete(main())  # 通过事件循环对象运行协程函数
# loop.close()

# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)   #阻塞当前task，让其他的执行
#     print("Hello again!")
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()  #创建一个事件循环
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()


# import asyncio
# async def eternity():
#     print('我马上开始执行')
#     await asyncio.sleep(3600)  # 当前任务休眠1小时，即3600秒
#     print('终于轮到我了')
# async def main():
#     # Wait for at most 1 second
#     try:
#         print('等你3秒钟哦')
#         await asyncio.wait_for(eternity(), timeout=3)  # 休息3秒钟了执行任务
#     except asyncio.TimeoutError:
#         print('超时了！')
# asyncio.run(main())


import asyncio
import time

a = time.time()


async def hello1():  # 大约2秒
    print("Hello world 01 begin")
    yield from asyncio.sleep(2)
    print("Hello again 01 end")


async def hello2():  # 大约3秒
    print("Hello world 02 begin")
    yield from asyncio.sleep(3)
    print("Hello again 02 end")


async def hello3():  # 大约4秒
    print("Hello world 03 begin")
    yield from asyncio.sleep(4)
    print("Hello again 03 end")


async def main():  # 入口函数
    done, pending = await asyncio.wait({hello1(), hello2(), hello3()}, return_when=asyncio.FIRST_COMPLETED)
    for i in done:
        print(i)
    for j in pending:
        print(j)


asyncio.run(main())  # 运行入口函数

b = time.time()
print('---------------------------------------')
print(b - a)

