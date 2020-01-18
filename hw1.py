'''
15-110 Homework 1
Name: Clara Ye
Andrew ID: zixuany
Enter your code below the comments
'''

'''
Question 1: Assign 15 to the variable x
'''
x = 15

'''
Question 2: Assign "22" to the variable y
'''
y = "22"

'''
Question 3a: Convert y to an integer and assign it to a new variable
'''
temp = int(y)

'''
Question 3b: Reassign variable x to the value 45
'''
x = 45

'''
Question 4: Compute x modulo y and assign the answer to variable z. Hint: ensure the values are numbers.
'''
z = x % int(y)

'''
Question 5: Print "The value of x is " and the value of x
'''
print("The value of x is",x)

'''
Question 6: Print "The value of y is " and the value of y
'''
print("The value of y is",y)

'''
Question 7: Print "The value of z is " and the value of z
'''
print("The value of z is",z)

'''
Question 8: Algorithm Implementation:
Write the code to match the following algorithm

1. Assign string Stephanie to profS
2. Assign string Kelly to profK.
3. Write a single print statement that greets Stephanie and Kelly by name
using variables profS and profK.
'''
profS = "Stephanie"
profK = "Kelly"
print("Hello",profS,"and",profK + "!")

'''
Question 9: Algorithm Implementation:
Write the code to match the following algorithm

1. Create 4 variables - x1, y1, x2, y2 - and assign them each different
numerical values
2. Compute the difference in y values (y2-y1) and assign to variable diffy:
3. Compute the difference in x values (x2-x1) and assign to variable diffx:
4. Compute the slope m = diffy divided by diffx
'''
x1 = 1
y1 = 2
x2 = 4
y2 = 8
diffy = y2 - y1
diffx = x2 - x1
m = diffy / diffx

'''
Question 10: Suppose you are trying to fill egg cartons with eggs.
Create a function fullEggCartons which takes an integer number of eggs as a parameter
and returns the number of completely full egg cartons.
Remember: Egg cartons have 12 slots for eggs.
'''
def fullEggCartons(x):
    return x // 12

'''
Question 10b: Call your function with values 65, 43, and 96 and print the answers.
'''
print(fullEggCartons(65))
print(fullEggCartons(43))
print(fullEggCartons(96))

'''
Question 11: Now suppose you are trying to fill egg cartons with eggs
and find the remainder. Create a function remainderEggs which takes
an integer number of eggs as a parameter and returns the number of eggs left after
completely filling egg cartons. Remember: Egg cartons have 12 slots for eggs.
'''
def remainderEggs(x):
    return x % 12

'''
Question 11b: Call your function remainderEggs with values 23, 76, and 51 and 
print the answers.
'''
print(remainderEggs(23))
print(remainderEggs(76))
print(remainderEggs(51))