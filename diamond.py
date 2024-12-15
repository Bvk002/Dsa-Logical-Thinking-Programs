N=int(input())
for i in range(1,N+1):
    sp=" "*(N-i)
    sy=("* ")*(i)
    print(sp+sy)
for i in range(1,N):
    sp=" "*(i)
    sy=("* ")*(N-i)
    print(sp+sy)