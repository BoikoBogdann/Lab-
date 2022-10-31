# Recursion for factorial
import random


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

u = random.randint(0,10)
print("Choose int:",u)
print("Recursion for factorial:",factorial(u))
# Cycle for factorial
def cycle_fact(x):
    for i in range(x + 1):
        if i == 0:
            j = i = 1
        else:
            j = j * i
    print("cycle_fact : ", j)
u = random.randint(0,10)
print("Choose int:",u)
cycle_fact(u)
# Recursion for fibonacci
def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)
u = random.randint(0,30)
print("Choose index of any Fibonacci number:",u)
print("Fibonacci number:", fibo(u))
# Cycle for fibo
n = random.randint(1,30)
def cycle_fibo(n):
    afp = 0
    bfn = 1
    i = 1
    fib = 1
    while i < n:
        fib = afp + bfn
        afp = bfn
        bfn = fib
        i += 1
    return fib
print("Choose index of any Fibonacci number:",n)
print("Fibonacci number:",cycle_fibo(n))
# Recursion division

def dev(x):
    if x < 10:
        return x
    elif x == 10:
        return 1
    else:
        return x % 10 + dev(x//10)
x = random.randint(10,1000)

print("Random value from 10 to 1000:", x)
print("Sum digit of number:", dev(x))
# Recursion for sum a + b
def plus(a, b):
    if b == 0:
        return a
    else:
        return plus(a ^ b, (a & b) << 1)

x = random.randint(0,1000)
y = random.randint(0,1000)
print("Sum of next numbers:", x ,'and',y)
print('Sum:', plus(x, y))




