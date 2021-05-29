class A(object):
    def __init__(self):
        self.a = 5

    def function_a(self):
        # print('I am from A, my value is %d' % self.a)
        print(1,self.__class__.__name__)
        print(2,A.__base__.__name__)  # todo


class B(A):
    def __init__(self):
        super(B, self).__init__()   # 此处修改了
        self.b = 10

    def function_b(self):
        # print('I am from B, my value is %d' % self.b)
        self.function_a()

if __name__ == '__main__':
    b = B()
    b.function_b()
    print(3,B.__class__.__name__)   # type
    print(4,B.__class__)   #<class 'type'>
    print(5,b.__class__.__name__)
    print(6, B.__base__.__name__)  # todo
