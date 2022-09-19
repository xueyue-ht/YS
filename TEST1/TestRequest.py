
import requests
import jsonpath

def test_get2():
    url = 'https://xueqiu.com/query/v1/suggest_stock.json'
    parmer = {'q': '60', 'count': '5'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Cookie': 'xq_a_token=45c480b02f280aa5399cbb8b545dbdfb8df3758b;xq_r_token=51853a11eb578337c65418905433e0ee029472fb'}
    re = requests.get(url=url,params=parmer, headers=headers)
    print(re.json())
    print(jsonpath.jsonpath(re.json(), "$.[?(@.code=='SH600519').query]"))