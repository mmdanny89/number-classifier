import cherrypy as http
import cherrypy
from contextlib import contextmanager


class RestApi:

    def __init__(self, msg_post="[TypeFizz, TypeBUzz, TypeNone, TypeFizzBuzz]") -> None:
        self.msg_post = msg_post

    @http.expose
    def index(self):
        return "<html><body><p>{0}</p></body></html>".format(self.msg_post)


@contextmanager
def test_run_server():
    cherrypy.config.update({'server.socket_port': 8181})
    cherrypy.engine.start()
    cherrypy.engine.wait(cherrypy.engine.states.STARTED)
    yield
    cherrypy.engine.exit()
    cherrypy.engine.block()


def run_server(msg=None):
    http.config.update( {'server.socket_host':"0.0.0.0", 'server.socket_port':8181 } )
    if msg:
        http.quickstart( RestApi(msg) )
    else:
        http.quickstart( RestApi() )


if __name__ == '__main__':
    run_server()
