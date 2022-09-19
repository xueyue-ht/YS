import json

import requests


class GetToken:
    url='https://vue-test.mophone.net'
    login_path='/idea-system/sys/login'
    checkKey= None
    Token= None
    def get_token(self):
        url=self.url+self.login_path
        print(url)
        data=json.dumps({'username': '13755053575','password':'13755053575','captcha':'cagl','checkKey':'1663312310923','remember_me': 'true'})
        headers={'Content-Type':'application/json;charset=UTF-8'}
        req=requests.post(url=url,data=data,headers=headers)
        print(req.json())
        return req.json()