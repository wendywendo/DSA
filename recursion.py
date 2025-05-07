# Define a recursive function that takes two integers as input and returns their product using repeated addition, without employing the multiplication operator.
def multiply(a, b):
    if b == 0:
        return 0

    if b < 0:
        return -multiply(a, -b)

    return a + multiply(a, b - 1)

# print(recursive_multiply(2, 3))

# Define a recursive function that computes the result of raising a given base to a specified exponent, without using the exponentiation operator(**)
def exponent(base, n):
    # Base case
    if n == 1:
        return base
    
    else:
        return base * exponent(base, n - 1)
    
# print(exponent(3, 3))

# Implement a recursive function that prints all integers from a given number n down to 0.
def printIntegers(n):
    if n == 0:
        return
    
    print(n)
    return printIntegers(n - 1)

# printIntegers(5)

# Implement a recursive function that prints all integers from 0 up to a given number n by modifying the previous countdown function
def countUp(n, curr = 0):
    if curr > n:
        return
    
    print(curr)
    return countUp(n, curr + 1)

# countUp(5)

#  Write a recursive function that takes a string as input and returns a reversed copy of the string,using only string concatenation.
def reverse(s):
    if s == "":
        return ""
    
    return reverse(s[1:]) + s[0]

# print(reverse("hello"))

# Write a recursive function that determines whether a given integer n is a prime number by checking for divisibility by integers less than n.
def isPrime(n, divisor=None):
    # Base case
    if n <= 1:
        return False
    
    if divisor is None:
        divisor = n - 1

    # If n == 2
    if divisor == 1:
        return True
    
    # If n mod divisor is 0, then the number isn't a prime number
    if n % divisor == 0:
        return False
    
    return isPrime(n, divisor - 1)

# print(isPrime(5))


# Write a recursive function that takes in one argument n and computes Fn, the nth value of the Fibonacci sequence. Recall that the Fibonacci sequence is defined by the relation Fn = Fn−1 + Fn−2 where F0 = 0 and F1 =1
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(5))

