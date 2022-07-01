import unittest
import server_api
import cherrypy
import requests


class TestRestApi(unittest.TestCase):


    def test_index(self):
        cherrypy.tree.mount(server_api.RestApi())
        with server_api.test_run_server():
            url = "http://127.0.0.1:8181/"
            r = requests.get(url)
            self.assertEqual(r.status_code, 200)


    def test_posted(self):
        cherrypy.tree.mount(server_api.RestApi())
        with server_api.test_run_server():
            url = "http://127.0.0.1:8181/posted/"
            params ={'list_numbers':'[Fizz Buzz FizzBuzz None None FizzBuzz]'}
            r = requests.get(url, params=params)
            self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()