# class Animal(object):
#     def run(self):
#         print('Animal is running...')
# def run_twice(animal):
#     animal.run()
#     animal.run()
# run_twice(Animal())

# import re
#
# vowels = "AEIOUaeiou"
# consonants = "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"
#
# m = re.findall(r"(?<=[%s])([%s]{2,})(?=[%s])" % (consonants, vowels, consonants), input())
#
# if m:
#     print("\n".join(m))
# else:
#     print("-1")


def indexstr(str1, str2):
    '''查找指定字符串str1包含指定子字符串str2的全部位置，
    以列表形式返回'''
    lenth2 = len(str2)
    lenth1 = len(str1)
    indexstr2 = []
    i = 0
    while str2 in str1[i:]:
        indextmp = str1.index(str2, i, lenth1)
        indexstr2.append(indextmp)
        i = (indextmp + lenth2)
    return indexstr2


if __name__ == '__main__':
    print()
    print(indexstr('aabceeabcddabcdabc', 'abc'))
