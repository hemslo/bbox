# coding = utf-8
#! /usr/bin/python3
import tornado.web
import string, os
from ser import serers

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        global handler
        self.write(str(handler.get()))


if __name__ == "__main__":
  settings = {
  "debug": True,
  }
  handler = serers()
  application = tornado.web.Application([
      (r"/get", MainHandler),
    ],**settings)
  application.listen(8090)
  tornado.ioloop.IOLoop.instance().start()
