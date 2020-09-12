class sumi:
    def factorial(self,n):
        return n * factorial(n - 1) if n > 1 else 1
    def sum_factorial(self,n):
        summ=0
        for i in range(n+1):
            summ+=factorial(i)
        return summ