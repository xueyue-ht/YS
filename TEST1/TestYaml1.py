import requests
import yaml



class HttpApi(yaml.YAMLObject):
    # yaml_tag = '!Demo'
    def __init__(self,method,url,parmers,headers):
        self.method=method
        self.url=url
        self.parmers=parmers
        self.headers=headers
    def send(self):
        return  requests.request(method=self.method,url=self.url,params=self.parmers,headers=self.headers).json()
def test_yaml1():
    req=HttpApi('get','https://xueqiu.com/query/v1/suggest_stock.json',{'q': 60},{
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Cookie': 'xq_a_token=45c480b02f280aa5399cbb8b545dbdfb8df3758b;xq_r_token=51853a11eb578337c65418905433e0ee029472fb'})
    print(req.send())
    print(yaml.dump(req))
    # req: HttpApi=yaml.unsafe_load(open('./test_yaml1.yaml','r'))
    # print(req.send())


