import math

def ArithmeticEquation(N):
    for x in range(1, 10**6):
        if 2 * (1/x) == 1/math.factorial(N):
            break
    eq = x
    
    return y

print(ArithmeticEquation(2))

