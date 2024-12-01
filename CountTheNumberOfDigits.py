class solution:
    def count_digits(self,n):
        cont=0
        while(n!=0):
            cont+=1 
            n=n//10
        return cont