# -*-coding:utf-8 -*-
"""
File    :   unit_tests_web_service.py
Date    :   2022/07/01 16:07:00
Author  :   Ing. Danny Molina Morales
Version :   1.0
E-mail  :   mmdanny89@gmail.com
"""

import unittest
import cherrypy
import requests
 
import server_api



class TestRestApi(unittest.TestCase):


    def test_index(self):
        cherrypy.tree.mount(server_api.RestApi())
        with server_api.test_run_server():
            url = "http://127.0.0.1:8181/"
            r = requests.get(url)
            self.assertEqual(r.status_code, 200)



if __name__ == '__main__':
    unittest.main()
