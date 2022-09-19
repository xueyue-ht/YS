import requests
from Test_WeiWork.api.GetToken import GetToken

class Department:
    list_url='https://qyapi.weixin.qq.com/cgi-bin/department/simplelist'
    def get_alldepart(self,id):
        params={'access_token':GetToken.access_token,'id':id}
        req=requests.get(url=self.list_url,params=params)
        return req.json()
