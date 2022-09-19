import os


class TestRead:
    def debug(func):
        def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
            print("[DEBUG]: enter {}()".format(func.__name__))
            print('Prepare and say...',)
            return func(*args, **kwargs)

        return wrapper  # 返回

    @debug
    def say(something,a):
        print("hello {}!".format(something))
        print("hello {}!".format(a))
    def setup(func):
        def newread(*args,**kwargs):
            print('新6')
            func(*args,**kwargs)
        return newread

    @setup
    def read(a,b):
        print('老6')
        print(a+b)
if __name__=='__main__':
    TestRead.say('早上好','同志们')
    TestRead.read(1,3)
    print(os.getcwd())
    print(os.path.abspath('..'))
    path='/TestFile/test_yaml'
    print(os.path.join(os.path.abspath('..'), path))
    base_dir = os.path.dirname(__file__)
    print(base_dir)