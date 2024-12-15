N=int(input())
for i in range(1,N+1):
    sy="* "*(i)
    sp="  "*(N-i)
    print(sy+sp+sp+sy)
for i in range(1,N):
    sy="* "*(N-i)
    sp="  "*(i)
    print(sy+sp+sp+sy)