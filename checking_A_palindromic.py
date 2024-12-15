class solution:
    def is_palindrome(self,n):
        n1=n 
        co=0
        while(n1!=0):
            l_d=n1%10
            co=co*10+l_d
            n1=n1//10
        if(co==n):
            return "Yes"
        else:
            return "No"