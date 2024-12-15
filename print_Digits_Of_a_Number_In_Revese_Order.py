class solution:
    def print_digit(self,n):
        while(n!=0):
            ld=n%10
            print(ld)
            n=n//10