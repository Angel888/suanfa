class A(object):
    def m1(self, n):
        print("self:", self)

    @classmethod
    def m2(cls, n):
        print("cls:", cls)

    @staticmethod
    def m3(n):
        pass


if __name__ == '__main__':
    a = A()
    a.m1(1) # self: <__main__.A object at 0x000001E596E41A90>
    A.m2(1) # cls: <class '__main__.A'>
    A.m3(1)


class Kls(object):
    num_inst = 0

    def __init__(self):
        # self.num_inst = self.num_inst + 1
        Kls.num_inst = Kls.num_inst + 1
    @classmethod
    def get_no_of_instance(cls):
        return cls.num_inst


ik1 = Kls()
print(ik1.get_no_of_instance())
ik2 = Kls()
print(ik1.get_no_of_instance())
print(Kls.get_no_of_instance())

# class Kls(object):
#     def foo(self, x):
#         print('executing foo(%s,%s)' % (self, x))
#
#     @classmethod
#     def class_foo(cls,x):
#         print('executing class_foo(%s,%s)' % (cls,x))
#
#     @staticmethod
#     def static_foo(x):
#         print('executing static_foo(%s)' % x)
#
#
# ik = Kls()
#
# # 实例方法
# ik.foo(1)
# print(ik.foo)  #todo 不加括号时打印出来的是什么东西？地址吗？
# print('==========================================')
#
# # 类方法
# ik.class_foo(1)
# Kls.class_foo(1)
# print(ik.class_foo)
# print('==========================================')
#
# # 静态方法
# ik.static_foo(1)
# Kls.static_foo('hi')
# print(ik.static_foo)