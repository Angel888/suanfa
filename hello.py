import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options  # 新导入的options模块

tornado.options.define("port", default=8000, type=int, help="服务器监听端口号")
tornado.options.define("content", default=[], type=str, multiple=True, help="控制台输出内容")


class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""

    def get(self):
        self.write("Hello World!")


if __name__ == "__main__":
    tornado.options.parse_command_line()
    print(tornado.options.options.content)  # 控制台输出内容
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()