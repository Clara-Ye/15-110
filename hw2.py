'''
15-110 Homework 2
Name:Clara Ye
Andrew ID:zixuany
'''

################################################################################

''' #1 - pythagoreanChecker(a, b, c) - 5pts
Write the function pythagoreanChecker(a, b, c) which takes three integers, 
a, b, and c, and checks whether they are a Pythagorean triple. Three numbers 
(x,y,z) are a triple when x squared plus y squared is equal to z squared. Note 
that the numbers a, b, and c may be given in any order.
'''

def pythagoreanChecker(a, b, c):
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return True
    else:
        return False

''' #2 - compoundInterest(base, rate, years) - 5pts
Write the function compoundInterest(base, rate, years), which calculates the 
amount that a base sum will have increased based on an annual interest rate and 
the number of years that have passed. This is computed by adding the current 
amount of money times the rate to the base sum every year.

For example, assume that you invest $1,000 in a retirement account that returns 
0.25% interest annually in 2019. In 2020, the account will have $1,002.50; 
in 2021, the account will have ~$1,005.01; and by 2059, the account will have
~$1,105.03. Note that you do not just add $2.50 every year; the amount of 
interest increases as the base sum increases. You can read more about compound
interest rates at https://en.wikipedia.org/wiki/Compound_interest

You may assume that years is an integer, base and rate are numbers, and that all
three numbers are non-negative.
'''

def compoundInterest(base, rate, years):
    while (years > 0):
        base *= (rate + 1)
        years -= 1
    return base

''' #3 - factorial(x) - 5pts
Write the function factorial(x) which takes a nonnegative integer, x, and 
returns x!. Recall that x! = x*(x-1)*(x-2)*...*3*2*1. You may not use the 
built-in function math.factorial; that would make this too easy.
'''

def factorial(x):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

''' #4 - countSentences(s) - 5pts
Write the function countSentences(s) that takes a string s and returns the 
number of non-empty sentences that occur in s. We define a sentence to be a 
consecutive string of one or more non-whitespace characters that ends in one of 
the following characters: . ! ?

For example, the following string has three sentences.

"You've got to ask yourself a question. Do I feel lucky? Well, do ya, punk?!"

Note that if a sentence ends in multiple punctuation marks, it still only 
counts as one sentence. Also note that the test cases are guaranteed to not 
use ., !, or ? inside a sentence, to simplify the problem.

Hint: consider using the string methods we discussed in class to make this 
problem much easier. Specifically, s.replace() and s.split() might be helpful...
'''

def countSentences(s):
    count = 1
    t = s.replace(". ", "@")
    u = t.replace("! ", "@")
    v = u.replace("? ", "@")
    for i in range(len(v)):
        if v[i] == "@":
            count += 1
    return count

''' #5 - printTriangle(n) - 10pts
Write a function printTriangle(n) which prints an ascii-art triangle out of 
asterisks based on the integer n (which is guaranteed to be positive and odd). 
For example, printTriangle(5) would print the following:

*
**
***
**
*

Note that the triangle is five lines long, with the top and bottom line each 
having only one asterisk, the second and second-from bottom line each having 
two asterisks, etc. So printTriangle(9) would look like:

*
**
***
****
*****
****
***
**
*
'''

def printTriangle(n):
    for i in range(1, ((n+1)//2), 1):
        print("*" * i)
    for i in range((n+1)//2), 0, -1):
        print("*" * i)
    return None

''' #6 - decodeFile(filename) - 10pts
Write the function decodeFile(filename) which takes a string filename as input, 
gets the text out of the file named filename, decodes a secret message in the 
text, and returns that secret message.

The file that the function is given will have a format like the one shown below:

72 101 108 108 111
87 111 114 108 100 33

To decode the message, you need to transform each number into its ascii string 
value, by using the chr() built-in method. If you combine together the resulting
characters in the same line, you'll get a word. Combine together the words 
formed by every line (separated by spaces), and you'll get the secret message!

In the example shown above, the first line produces "Hello" and the second line 
produces "World!", so the function would return "Hello World!"

Make sure to download the files test1.txt and test2.txt and put them in the same 
directory as your hw2.py file, so you can test your code!
'''

def decodeFile(filename):
    file = open(filename,"r")
    str = f.read()
    file.close()
    message = ""
    for line in string.split("\n"):
        for num in line.split(" "):
            char = chr(int(num))
            message += char
        mes += " "
    return mes[:len(mes)-1]

''' #7 - printPrimeFactors(x) - 10pts
Write the function printPrimeFactors(x) which takes a positive integer x and 
prints all of its prime factors.

A prime factor is a number that is both prime and evenly divides the original 
number (with no remainder). So the prime factors of 70 are 2, 5, and 7, because 
2 * 5 * 7 = 70. Note that 10 is not a prime factor because it is not prime, and 
3 is not a prime factor because it is not a factor of 70.

Prime factors can be repeated when the same factor divides the original number 
multiple times; for example, the prime factors of 12 are 2, 2, and 3, 
because 2 and 3 are both prime and 2 * 2 * 3 = 12. The prime factors of 16 are 
2, 2, 2, and 2, because 2 * 2 * 2 * 2 = 16.

This problem is slightly more complex than most of the other homework problems, 
so let's lay out a high-level algorithm for how to approach it. First, note that 
when we solve this problem by hand, we can find the prime factors of a number by 
repeatedly dividing the number by the smallest possible factor until the number 
becomes 1. So our algorithm might look something like this:

Repeat the following procedure until the number x becomes 1
- Define a new number, n, to be 2
- Repeat the following procedure until a factor is found
  - If the current number divides n evenly
    - Print the number n
    - Set x to x divided by n
    - Report that a factor has been found
  - If it does not
    - Add one to n
'''

def printPrimeFactors(x):
    n = 2
    while (x != 1):
        if ((x % n) != 0):
            n += 1
        else:
            print(n)
            x /= n
    return None

################################################################################

''' To check your work, click 'Run File as Script' to run the test function
shown below. You should also check the autograder results on Gradescope! '''
def testPythagoreanChecker():
    print("Testing pythagoreanChecker()...", end="")
    assert(pythagoreanChecker(3, 4, 5) == True)
    assert(pythagoreanChecker(4, 3, 5) == True)
    assert(pythagoreanChecker(4, 5, 3) == True)
    assert(pythagoreanChecker(16, 63, 65) == True)
    assert(pythagoreanChecker(3, 4, 6) == False)
    assert(pythagoreanChecker(10, 10, 10) == False)
    assert(pythagoreanChecker(1, 1, 2) == False)
    print("... done!")

def testCompoundInterest():
    print("Testing compoundInterest()...", end="")
    import math
    # We use math.isclose here to compare floats, which can be close but not 
    # exactly the same. Note that math.isclose has unexpected behavior when 
    # the numbers it compares are close to 0.
    assert(math.isclose(compoundInterest(1000, 0.0025,  1), 1002.50))
    assert(math.isclose(compoundInterest(1000, 0.0025,  2), 1005.00625))
    assert(math.isclose(compoundInterest(1000, 0.0025, 40), 1105.0330101290704))
    assert(math.isclose(compoundInterest(1000, 0.0025,  0), 1000))
    assert(math.isclose(compoundInterest(20000, 0.0453, 5), 24959.43485796928))
    print("... done!")

def testFactorial():
    print("Testing factorial()...", end="")
    assert(factorial(1) == 1)
    assert(factorial(2) == 2)
    assert(factorial(3) == 6)
    assert(factorial(4) == 24)
    assert(factorial(5) == 120)
    assert(factorial(6) == 720)
    assert(factorial(10) == 3628800)
    assert(factorial(0) == 1)
    print("... done!")

def testCountSentences():
    print("Testing countSentences()...", end="")
    assert(countSentences("One.") == 1)
    assert(countSentences("One. One two! One two three? One two three four.") == 4)
    assert(countSentences("You've got to ask yourself a question. Do I feel lucky? Well, do ya, punk?!") == 3)
    assert(countSentences("This.!.?. Is a very!!!??? Improper sentence.") == 3)
    assert(countSentences("Don't worry, we'll make sure every sentence ends with punctuation.") == 1)
    print("... done!")

def testPrintTriangle():
    print("Testing printTriangle()...")
    printTriangle(1)
    print("---")
    printTriangle(3)
    print("---")
    printTriangle(5)
    print("---")
    printTriangle(7)
    print("---")
    printTriangle(9)
    print("... check your output to see if it looks correct!")

def testDecodeFile():
    print("Testing decodeFile(), make sure you've downloaded the test files...", end="")
    assert(decodeFile("test1.txt").strip() == "Hello World!")
    assert(decodeFile("test2.txt").strip() == "I say, this is far '2' much.")
    print("... done!")

def testPrintPrimeFactors():
    print("Testing printPrimeFactors()...")
    printPrimeFactors(70) # 2, 5, 7
    print("---")
    printPrimeFactors(12) # 2, 2, 3
    print("---")
    printPrimeFactors(16) # 2, 2, 2, 2
    print("---")
    printPrimeFactors(36) # 2, 2, 3, 3
    print("---")
    printPrimeFactors(3289) # 11, 13, 23
    print("... check your output to see if it looks correct!")

def testAll():
    testPythagoreanChecker()
    testCompoundInterest()
    testFactorial()
    testCountSentences()
    testPrintTriangle()
    testDecodeFile()
    testPrintPrimeFactors()

testAll()
