n=int(input())
n1=n
len_n=len(str(n))
sum_=0
while n1!=0:
    lastD=n1%10
    pow_=lastD**len_n
    sum_+=pow_
    n1=n1//10
if(n==sum_):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")