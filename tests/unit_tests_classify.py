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

import importlib.machinery
import importlib.util
from pathlib import Path
script_dir = Path( __file__ ).parent.parent
classifier_path = str( script_dir.joinpath('classifier.py' ) )
loader = importlib.machinery.SourceFileLoader( 'classifier', classifier_path    )
spec = importlib.util.spec_from_loader( 'classifier', loader )
classifier = importlib.util.module_from_spec( spec )
loader.exec_module( classifier )


class ClassifyTest(unittest.TestCase):
    
    
    def test_prepare_data(self):
        data = pd.DataFrame({'Number':[1010, 1111, 10100] })
        result_prepare = classifier.prepare_data_to_classify([30,40,90])
        self.assertEqual(True, data.equals(result_prepare))


if __name__ == '__main__':
    unittest.main()
