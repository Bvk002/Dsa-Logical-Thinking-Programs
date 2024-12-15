class solution:
    def reverseNumber(self, N):
        var=0
        while(N!=0):
            lastdigit=N%10
            var=var*10+lastdigit
            N=N//10
        return var