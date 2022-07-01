import cherrypy as http
import uuid 
import cherrypy
from contextlib import contextmanager


class RestApi:


    @http.expose
    def index(self):
        return """
            <html>
                <body>
                    <form method='get' action='/posted'>
                        <input value="%s" name="uuid" size='50'/>
                        <input type='submit' value='Submit' />
                    </form>
                </body>
            </html>
        """ % uuid.uuid4()


    @http.expose
    def posted(self, uuid):

        return """
            <html>
                <body>
                    <p>%s</p>
                </body>
            </html>
        """ % uuid
        

@contextmanager
def test_run_server():
    cherrypy.config.update({'server.socket_port': 8181})
    cherrypy.engine.start()
    cherrypy.engine.wait(cherrypy.engine.states.STARTED)
    yield
    cherrypy.engine.exit()
    cherrypy.engine.block()


def run_server():
    http.config.update( {'server.socket_host':"0.0.0.0", 'server.socket_port':8181 } )
    http.quickstart( RestApi() )


if __name__ == '__main__':
    run_server()
