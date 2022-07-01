import cherrypy as http
import cherrypy
from contextlib import contextmanager


class RestApi:


    @http.expose
    def index(self):
        return """
            <html>
                <body>
                    <form method='get' action='/posted'>
                        <label for="list-number">Enter a List of Numbers: Example: 3,4,5,6</label>
                        <input value="%s" name="list-number"/>
                        <input type='submit' value='Classify'/>
                    </form>
                </body>
            </html>
        """ % "3,4,5,6"


    @http.expose
    def posted(self, list_numbers):
        #classify here and return value
        return """
            <html>
                <body>
                    <p>%s</p>
                </body>
            </html>
        """ % list_numbers
        

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
