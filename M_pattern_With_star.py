n = int(input())
for i in range(1 , n + 1):
    sp = "  " * (n - i)
    pa = "* " * i
    print(pa + sp + sp + pa)