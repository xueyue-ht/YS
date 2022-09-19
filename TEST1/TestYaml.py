import json
import yaml
from TEST1 import TestYaml1.

class TestYaml:
    def testread_yaml(self):
        data=yaml.unsafe_load(open('./test_yaml1.yaml'))
        print(data)
    def testread_json(self):
        data=json.load(open('../TestFile/test_json'))
        print(data)
    def setup(func):
        def newread(*args,**kwargs):
            print('新6')
            func(*args,**kwargs)
        return newread

    @setup
    def read(a,b):
        print('老6')
        print(a+b)
    def read1(self):
        read(1,5)

