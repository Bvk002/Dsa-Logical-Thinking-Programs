n = int(input())
for i in range(1 , n + 1):
    sp = " " * (i - 1)
    tot = "*" * ((n + 1) - i) + "*" * ((n + 0) - i)
    print(sp + tot)