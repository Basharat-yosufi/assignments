#Exercise 6: Vowel Checker
#1.	Create a function named is_vowel that takes a character (a single letter)
# as a parameter and returns True if it's a vowel (a, e, i, o, u - both uppercase and lowercase), otherwise False.
#2.	Demonstrate the usage of this function by checking whether the characters 'a', 'b', 'E', and 'Z' are vowels.

def is_vowel(letter):
    if letter =='a' or 'e' or 'i' or 'o' or 'u' or 'A' or "E" or 'I' or 'O' or 'U':
        print("true")
    else:
        print("false")
is_vowel('a')
is_vowel('e')
is_vowel('E')
is_vowel('z')
