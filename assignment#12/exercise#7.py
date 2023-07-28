##Exercise 7: Factorial of a Number
#1.	Create a function named factorial that takes a positive integer as a parameter and returns its factorial. 
#The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
#2.	Demonstrate the usage of this function by calculating the factorial of 5.

def factorial(n):
    if n == 1:
     return n
    elif n < 1:
       return("false") 
    else:
       return n * factorial(n-1)
print(factorial(int(5)))
factorial(5)
    