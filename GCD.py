m = int(input())
n = int(input())
if m > n:
    ln = m
else:
    ln = n
a = 0
for i in range(1,ln+1):
    if m%i == 0 and n%i == 0:
        a =i
print(a)