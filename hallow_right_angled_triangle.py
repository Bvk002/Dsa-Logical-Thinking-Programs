n = int(input())
for i in range(1 , n + 1):
    if i == 1 or i == n:
        print("* " * i)
    else:
        sp = "  " * (i - 2)
        print("* " + sp + "*")