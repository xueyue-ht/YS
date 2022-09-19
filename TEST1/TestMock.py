import pytest
import  requests
# class MockResponse:
#     @staticmethod
#     def json():
#         return {'key':'json response'}

def test_mock(monkeypatch):
    def responce(*args):
        return ({'key':'value'})
    monkeypatch.setattr(requests,'get',responce)
    print(requests.get('http://www.baidu.com')['key'])