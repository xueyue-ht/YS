import requests
class Test_Yusuan:
    def test_login(self):
        url='https://vue-test.mophone.net/idea-system/sys/login'
        data={'username': "admin", 'password': "123456", 'captcha': "YWXZ", 'checkKey': 1663147177566, 'remember_me': 'true'}

    def test_button(self):
        url='https://vue-test.mophone.net/idea-system/sys/permission/getUserPermissionByToken'
        params={'_t': '1663147882'}
        headers={'X-Access-Token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjMxNDk2ODIsInVzZXJuYW1lIjoiMTM3NTUwNTM1NzUifQ.Ib_NmHsIHu2gDaB8d9JCUwocST4DK-R0-5JRdTLutYA'}
        req=requests.get(url=url,params=params,headers=headers)
        print(req.json())
    
