import pytest
import requests

@pytest.fixture(scope='function')
# @pytest.fixture(autouse=True)
def geturl():
    url = 'https://xueqiu.com/query/v1/suggest_stock.json'
    parmer = {'q': '60', 'count': '5'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Cookie': 'xq_a_token=28ed0fb1c0734b3e85f9e93b8478033dbc11c856;xq_r_token=bf8193ec3b71dee51579211fc4994d03f17c64ac'}
    re = requests.get(url=url, params=parmer, headers=headers)
    return re.json()
@pytest.fixture(scope='function')
def pr1():
    print('print1')