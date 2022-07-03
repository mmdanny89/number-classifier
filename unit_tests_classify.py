# -*-coding:utf-8 -*-
"""
File    :   unit_tests_classify.py
Date    :   2022/07/03 10:51:45
Author  :   Ing. Danny Molina Morales
Version :   1.0
E-mail  :   mmdanny89@gmail.com
"""

import unittest
import pandas as pd

import classifier


class ClassifyTest(unittest.TestCase):
    
    
    def test_prepare_data(self):
        data = pd.DataFrame({'Number':[1010, 1111, 10100] })
        result_prepare = classifier.prepare_data_to_classify([30,40,90])
        self.assertEqual(True, data.equals(result_prepare))


if __name__ == '__main__':
    unittest.main()
