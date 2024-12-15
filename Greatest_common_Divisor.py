class solution:
    def gcd(self, A, B):
        while(A!=0 and B!=0):
            if(A>=B):
                A=A%B 
            else:
                B=B%A 
        if(A==0):
            return B 
        else:
            return A