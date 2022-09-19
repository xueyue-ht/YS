import requests
class GetToken:
    url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    corpid='wwd691b224b33533e0'
    corpsecret='mbP_wVO5mG7LzH71vDXycqxtViBMZbvI-a2ieodJOBU'
    access_token=None
    @classmethod
    def gettoken(cls):
        if cls.access_token==None:
            params = {'corpid': cls.corpid, 'corpsecret': cls.corpsecret}
            cls.req = requests.get(url=cls.url, params=params)
            cls.access_token = cls.req.json()['access_token']
        return GetToken.access_token