import scrapy
# line="booooobby123"
# regex_str='.*?(b.*b).*'
# a=re.match(regex_str,line)
# print(a.group(0))

#
# from selenium import webdriver
# import os
#
# chromedriver = r"C:\Users\Dell\AppData\Local\Google\Chrome\Application"  # 这里是你的驱动的绝对地址
# browser = webdriver.Chrome(chromedriver)
#
# # 设置浏览器需要打开的url
# url = "http://www.baidu.com"
# browser.get(url)

def q4(*args,**kwargs):
    print('例4')
    # print(args)
    # print(args[0])
    # print(kwargs)
    print(kwargs.get('name1'))
# t1 = 123,234,345
di = {
    'name1': 'jack',
    'name2': 'rose',
}
# q4(*t1)
print('---')
q4(**di)
print('-----------------')