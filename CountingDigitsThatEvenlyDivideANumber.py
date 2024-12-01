class solution:
    def evenly_divides(self,N):
        #Code here
        cont=0
        temp=N
        while(temp!=0):
            lastdigit=temp%10
            temp=temp//10
            if lastdigit!=0 and N%lastdigit==0:
                cont=cont+1
        return cont