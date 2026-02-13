#Write a Python program that finds the factorial 
# of a number using recursion and returns the result. 
#(Example - If number = 5, factorial = 5*4*3*2*1 = 120)
def factorial(number):
    if number==1:
        return 1
    return number*factorial(number-1)
print(factorial(5))