#Exercise 4: Check Even or Odd
#1.	Create a function named is_even that takes an integer as a parameter and returns True if the number is even, otherwise False.
#2.	Demonstrate the usage of this function by checking whether the number 10 is even or odd.



def is_even(integer):
    if(integer % 2 == 0):
       print("true")
    else:
        print("false")
is_even(10)         