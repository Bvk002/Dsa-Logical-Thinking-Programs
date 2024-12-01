class solution:
    def calculate_digit_sum(self,N1, N2):
        b=N1
        a=N1
        sum=0
        diff = N2-N1
        for i in range(1,(diff+2)):
            while(a!=0):
                lastd=a%10
                sum=sum+lastd
                a=a//10
            a=b+i
        return sum