import sys


class A(object):
    def a(self):
        pass
class B(A):
    def a(self):
        print(sys._getframe().f_code.co_name)
class C(A):
    def c(self):
        self.A=  B().a()

if __name__ == '__main__':
    B().a()
