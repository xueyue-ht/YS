import logging
import pytest
import yaml
from TEST.Calc import Calc

logging.basicConfig(level=logging.DEBUG)
def setup_modle():
    logging.info('modle')

class Test_Add:
    @classmethod
    def setup_class(cls):
        logging.info('class setup')
    @classmethod
    def teardown_class(cls):
        logging.info('class end')

    def setup(self):
        self.calc=Calc()
    def teardown(self):
        print('method end')
    @pytest.mark.parametrize('a,b,c',[(1,2,3)])
    def test_add(self,a,b,c):
        assert self.calc.add(a,b)==c
    @pytest.mark.parametrize('a,b,c', yaml.safe_load(open(r'C:\Users\liuyanzi\PycharmProjects\pythonProject4\TestFile\test_yaml')))
    def test_add1(self,a,b,c):
        assert self.calc.add(a,b)==c