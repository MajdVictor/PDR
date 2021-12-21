def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

def printFib(n):
    a = 0
    b = 1
    cnt = 0
    while cnt <n:
        a ,b = b, a+b
        print(b)
        cnt += 1



if __name__ == "__main__":
    print(fib(5))
    printFib(5)