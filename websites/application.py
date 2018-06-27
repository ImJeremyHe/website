#!/usr/bin/env python
# coding=utf-8


import os.path
import tornado.web
import torndb
import tornado.ioloop
from tornado.options import define, options
import handlers.xzdzd
import model.xzdzd


define("port", default=80, help="run on the given port.", type=int)
define("mysql_host", default="127.0.0.1", help="mysql_host", type=str)
define("mysql_port", default=3306, help="mysql_port", type=int)
define("mysql_user", default="root", help="mysql_user", type=str)
define("mysql_password", default="123", help="password on mysql", type=str)
define("database", default="earthquake", help="database used to the websites", type=str)


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            login_url="/login",
            cookie_secret="cookie_secret_code",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            blog_title="HJM",
            autoescape=None,

        )
        all_handlers = [
            (r'/xzdzd', handlers.xzdzd.XzdzdHandler)
        ]
        super(Application, self).__init__(all_handlers, **settings)
        self.user_info = {}
        self.db = torndb.Connection(host=options.mysql_host, database=options.database,
                                    user=options.mysql_user, password=options.mysql_password)

        self.xzdzd_model = model.xzdzd.XzdzdModel(self.db)


if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
