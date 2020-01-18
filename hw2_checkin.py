'''
15-110 Homework 2 Check-in
Name:Clara Ye
Andrew ID:zixuany
'''

''' #1: intSign(x)
Below this comment, write a function, intSign(x) that takes a number x and 
returns a string representing its sign ("positive", "negative", or "zero"). 
You may assume x will be an int or a float.
'''
def intSign(x):
    if x > 0:
        str = "positive"
    else:
        if x < 0:
            str = "negative"
        else:
            str = "zero"
    return str
            
''' #2: Flow Chart to Program
Given the control flow chart shown on the assignment writeup, write a function, 
mysteryFunction(a, b, c), that implements that control flow chart correctly.
'''
def mysteryFunction(a,b,c):
    d = 0
    while a <= b:
        if a % c == 0:
            d = d + 1
        a = a + 1
    return d

''' To check your work, click 'Run File as Script' to run the test function
shown below. You should also check the autograder results on Gradescope! '''
def testIntSign():
    print("Testing intSign()...", end="")
    assert(intSign(42) == "positive")
    assert(intSign(-20) == "negative")
    assert(intSign(0.5) == "positive")
    assert(intSign(-0.1) == "negative")
    assert(intSign(0) == "zero")
    print("... done!")

def testFlowChart():
    print("Testing mysteryFunction()...", end="")
    assert(mysteryFunction(1, 10, 3) == 3)
    assert(mysteryFunction(1, 8, 3) == 2)
    assert(mysteryFunction(20, 25, 4) == 2)
    assert(mysteryFunction(1, 100, 2) == 50)
    assert(mysteryFunction(7, 11, 6) == 0)
    print("... done!")

def testAll():
    testIntSign()
    testFlowChart()

testAll()