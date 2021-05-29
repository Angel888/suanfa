if __name__ == '__main__':
    with open("aa",mode="a+") as f:
        f.write("\n ddd127.0.0.1 gw.api.taobao.com")
    data = f.read("aa")
    f.close()
    print(data)