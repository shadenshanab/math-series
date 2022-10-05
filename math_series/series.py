def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def lucas(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)

def sum_series(n, a=0, b=1):
    if a == 0 and b == 1:
        return fib(n)
    elif (a == 1 and b == 2) or (a == 2 and b == 1):
        return lucas(n)
    else :
        sum_list = [0]*n
        sum_list[0] = a
        sum_list[1] = b
        for i in range(2, n):
            sum_list[i] = sum_list[i - 1] + sum_list[i - 2]
        return sum_list[n-1]
        
