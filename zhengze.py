import re
# print(re.findall(r'/','http://www.hackerrank.com/'))
def indexstr(str1,str2):
    '''查找指定字符串str1包含指定子字符串str2的全部位置，
    以列表形式返回'''
    lenth2=len(str2)
    lenth1=len(str1)
    indexstr2=[]
    i=0
    while str2 in str1[i:]:
        indextmp = str1.index(str2, i, lenth1)
        indexstr2.append(indextmp)
        i = (indextmp + lenth2)
    return indexstr2

if __name__ == '__main__':
    print()
    print(indexstr('aabceeabcddabcdabc','abc'))
