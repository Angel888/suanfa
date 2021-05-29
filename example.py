# 迭代器
# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:", res)
#
# g = foo()
# print(next(g))
# print("*" * 20)
# print(next(g))

# assert 1==0

# class Person(object):
#
#     def __new__(cls, name, age):
#         print('__new__ called.')
#         return super(Person, cls).__new__(cls, name, age)
#
#     def __init__(self, name, age):
#         print('__init__ called.')
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return '<Person: %s(%s)>' % (self.name, self.age)

# if __name__ == '__main__':
#     name = Person('xxx', 24)
#     print(name)

#coding:utf-8

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
__author__ = 'okker.ma@gmail.com'

import tornado.ioloop
import tornado.web

import os
from tornado.options import options, define

# 在options中设置几个变量
define('debug', default=True, help='enable debug mode')
define('port', default=9002, help='run on this port', type=int)

# 解析命令行, 有了这行，还可以看到日志...
tornado.options.parse_command_line()


# class MainHandler(tornado.web.RequestHandler):
#
#     def get(self):
#         self.write("hello,a world")
#
#
# settings = {
#     'debug': options.debug,
#     'gzip': True,
#     'autoescape': None,
#     'xsrf_cookies': False,
#     'cookie_secret': 'xxxxxxx'
# }
#
# application = tornado.web.Application([
#     (r'/', MainHandler)
# ], **settings)

if __name__ == '__main__':
    print(os.path.dirname(__file__))