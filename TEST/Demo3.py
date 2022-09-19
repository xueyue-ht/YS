class A:
    def m(self):
        print('aaa')
class B:
    def n(self):
        print('bb')
    @classmethod
    def v(cls):
        print('ces ')


print(A)
a=A()
a.m()
B.v()