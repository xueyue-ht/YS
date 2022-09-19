import requests
from Test_WeiWork.api.GetToken import GetToken

class Members:
    list_url='https://qyapi.weixin.qq.com/cgi-bin/user/simplelist'
    def get_allmembers(self,id):
        params={'access_token':GetToken.access_token,'id':id}
        req=requests.get(url=self.list_url,params=params)
        return req.json()