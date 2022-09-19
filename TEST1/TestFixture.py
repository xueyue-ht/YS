import logging

import pytest
import requests

logging.basicConfig(level=logging.DEBUG)
class TestFixture():
    @pytest.fixture()
    def test_req(self):
        logging.info('开始')
        print('kaishi')
        yield logging.info('结束')
        print('jieshu')

    # @pytest.mark.usefixtures('geturl')
    def test_req1(self,geturl):
        print(geturl)
        assert  geturl['data'][0]['query']=='贵州茅台'
    


