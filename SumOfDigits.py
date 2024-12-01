n = int(input())
sum_=0
while n!=0:
    lastD=n%10
    sum_=sum_+lastD
    n=n//10
print(sum_)