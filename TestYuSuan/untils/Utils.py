import json


class Utils:
    json1=None
    @classmethod
    def bejson(cls,js):
        cls.json1=json.dumps(js,indent=4,ensure_ascii=False)
        return cls.json1