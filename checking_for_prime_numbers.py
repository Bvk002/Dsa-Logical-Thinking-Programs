class solution:
    def isPrime(self, n):
        cont=0
        for i in range(1,int(n**0.5)+1):
            if(n%i==0):
                cont+=1 
                if(i!=n//i):
                    cont+=1
        if cont==2:
            return 1 
        else:
            return 0