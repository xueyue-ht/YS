from pprint import pprint

import jsonpath
import requests
from TestYuSuan.untils.Utils import Utils
from TestYuSuan.api.GetToken import GetToken
class TestLogin:
    Token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjM1NTIwMjYsInVzZXJuYW1lIjoiMTM3NTUwNTM1NzUifQ.EihEVUS5KZ0a_4UI16X1JwopTxbI-zrKDUMP7RBPVi0'
    ip='https://vue-test.mophone.net'
    t='1663550952'
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
        # printer.pprint(req.json())

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




