import tornado.web
import tornado.httpclient
import tornado.httpserver
import tornado.ioloop

import urllib
import json
import os

TURING_KEY = os.environ["TURING_KEY"]
TURING_URL = "http://www.tuling123.com/openapi/api"

class QqHandler(tornado.web.RequestHandler):
    def post(self):
        print self.request.body

        sender_id = self.get_argument("sender_id")
        content = self.get_argument("content")

        request = tornado.httpclient.HTTPRequest(TURING_URL, "POST",
            body = urllib.urlencode({
                                        "key" : TURING_KEY,
                                        "info" : content,
                                        "userid" : sender_id
                                    }))

        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch(request, self.on_response)

    def on_response(self, response):
        body = json.loads(response.body)
        print response.body

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/qq", QqHandler),
        # (r"/console", ConsoleHandler),
    ], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(os.environ["PORT"])
    tornado.ioloop.IOLoop.instance().start()
    print "Server Started"
