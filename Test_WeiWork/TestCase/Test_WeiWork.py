from Test_WeiWork.api.Department import Department
from Test_WeiWork.api.GetToken import GetToken
from Test_WeiWork.api.Members import Members


class Test_WeiWork():
    def test_gettoken(self):
        gettoken=GetToken()
        token=gettoken.gettoken()
        assert token!=None
    def setup_class(self):
        self.gettoken = GetToken()
        self.access_token=self.gettoken.gettoken()

    def test_GetAllDepart(self):
        depart=Department()
        print(GetToken.access_token)
        print(depart.get_alldepart(''))
    def test_GetAllMembers(self):
        member=Members()
        print(member.get_allmembers('1'))
