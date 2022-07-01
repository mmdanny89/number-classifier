# -*-coding:utf-8 -*-
"""
File    :   unit_tests_web_service.py
Date    :   2022/07/01 16:07:00
Author  :   Ing. Danny Molina Morales
Version :   1.0
E-mail  :   mmdanny89@gmail.com
"""


import importlib.machinery
import importlib.util
from pathlib import Path

import unittest
import cherrypy
import requests
 
script_dir = Path( __file__ ).parent.parent
server_api_path = str( script_dir.joinpath('server_api.py' ) )
loader = importlib.machinery.SourceFileLoader( 'server_api', server_api_path    )
spec = importlib.util.spec_from_loader( 'server_api', loader )
server_api = importlib.util.module_from_spec( spec )
loader.exec_module( server_api )



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
