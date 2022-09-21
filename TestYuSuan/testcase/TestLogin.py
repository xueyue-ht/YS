from pprint import pprint

import jsonpath
import requests
from TestYuSuan.untils.Utils import Utils
from TestYuSuan.api.GetToken import GetToken
class TestLogin:
    Token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjM2NjQyODksInVzZXJuYW1lIjoiMTM3NTUwNTM1NzUifQ.wa56OEykK4H599pBVvSjVJfAgN1TpOsAAEe5ei7wkiQ'
    ip='https://vue-test.mophone.net'
    t='1663662514'
    def test_login(self):
        gettoken=GetToken()
        gettoken.get_token()

    def test_button(self):
        # printer=pprint.PrettyPrinter()
        path='/idea-system/sys/permission/getUserPermissionByToken'
        url=self.ip+path
        params={'_t': self.t}
        headers={'X-Access-Token':self.Token}
        req=requests.get(url=url,params=params,headers=headers)
        print(jsonpath.jsonpath(req.json(), "$..result.allAuth[?(@.describe=='添加按钮')].status"))
        pprint(req.json())

    def test_YsList(self):
        path='/idea-budget/budget/budget/list'
        url=self.ip+path
        params={'_t': self.t,'operate': '1','groupBranchId': '125','column': 'createTime','order': 'desc','pageNo': 2,'pageSize': 50}
        headers = {'X-Access-Token': self.Token}
        req=requests.get(url=url,params=params,headers=headers)
        # print(Utils.bejson(req.json()))
        pprint(req.json(),indent=2)
        lis=jsonpath.jsonpath(req.json(), "$..budgetUserName")
    def test_Download(self):
        path='/idea-budget/material/material/dowmloadtemplate'
        url=self.ip+path
        params={'_t': self.t}
        headers = {'X-Access-Token': self.Token}
        req=requests.get(url=url,params=params,headers=headers)
        print(req)




