from ..codegen import codegen
import unittest
import sys
import os
from ..exceptions import exceptions as exc

datas = []
n_tests = 3

dir_path = os.path.dirname(os.path.realpath(__file__))
print (dir_path)

for i in range(n_tests):
    with open(dir_path + '/test_files/test' + str(i+1) + '_codegen.apollo', 'r') as myfile:
        datas.append(myfile.read())
        myfile.close()

