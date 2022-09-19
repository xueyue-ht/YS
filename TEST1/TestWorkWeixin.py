import pytest
import requests
class TestWorkWein:
    def test_gettoken(self):
        url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        proxies={'https':'127.0.0.1:8886'}
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
        data={'corpid':'wwd691b224b33533e0','corpsecret':'mbP_wVO5mG7LzH71vDXycqxtViBMZbvI-a2ieodJOBU'}
        req=requests.get(url=url,params=data)
        print(req.json())