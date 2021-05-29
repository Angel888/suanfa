def fib(N):
    n_1=1
    n_2=1
    while N>n_2:
        tmp=n_2
        n_2=n_2+n_1
        n_1=tmp
    cha_1=N-n_1
    cha_2=n_2-N
    print(n_2,n_1)
    return cha_2 if cha_2<cha_1 else cha_1
print(fib(15))