class T:
    def __init__(self, v, l):
        self.v = v
        self.l = l

a = T(1, [1,2,3])
import copy
b = copy.copy(a)
# b = copy.deepcopy(a)

print("id(a)={}, id(b)={}, id(a.l)={}, id(b.l)={}".format(id(a), id(b), id(a.l), id(b.l)))

aa = T(1, [1,2,3])
bb = aa
print(id(aa), id(bb))