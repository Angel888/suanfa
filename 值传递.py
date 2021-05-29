# 值传递和引用传递，血的教训
# python传递可变对象时安引用传递，传递不可变对象时，按值传递。
a = "abc"
b = {"123": 456}
c=[1,2,3]
if a:
    a="def"
def deal(a, b,c):
    a = a + "def"
    # a=2
    b["456"] = 456
    c.append(3)
    return True


deal(a, b,c)
print(a)
print(b)
print(c)


