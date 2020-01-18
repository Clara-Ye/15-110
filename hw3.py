'''
15-110 Homework 3
Name: Clara Ye
Andrew ID: zixuany
Enter your code below the comments
'''

'''
Question 1: write a function countFirstLetter(L,letter) that counts and returns
the number of elements who's first letter is the one given.
e.g., countFirstLetter(["dog","daisy","dandilion"],"d") returns 3
You may assume the list elements are strings.
Return the count.
'''
def countFirstLetter(L,letter):
    count = 0
    for element in L:
        if element[0] == letter:
            count += 1
    return count

'''
Question 2: write a function middleAppend(L,item) which finds the middle of the list
(use integer division) and inserts a new value at that location in the list.
e.g., middleAppend([1,2,3],4) modifies the list to be [1,4,2,3]
Return the list.
'''
def middleAppend(L,item):
    location = len(L) // 2
    L.insert(location,item)
    return L

'''
Question 3: write a function odds(L) that returns a list of only the odd indexed
 items. Note: this is not the odd numbers, it is the odd index!
 e.g., [0,1,2,3,4,5] returns [1,3,5] and [1,2,3,4,5,6] returns [2,4,6]
Return the new list.
'''
def odds(L):
    N = []
    for i in range(len(L)):
        if i % 2 == 1:
            N += [L[i]]
    return N

'''
Question 4: write a function removeEvens(L) that removes the even indexed items
leaving a list of only the original odd indexed items remaining in L.
Note: this is tricky because L is changing, check for aliasing issues.
You can assume there is only one of each value in the list.
 e.g., [0,1,2,3,4,5] modifies the list to be [1,3,5]
 and [1,2,3,4,5,6] modifies the list to be [2,4,6]
Return None.
'''
def removeEvens(L):
    N = []
    for i in range(len(L)):
        if i % 2 == 0:
            N += [L[i]]
    for j in range(len(N)):
        L.remove(N[j])
    return None

'''
Question 5: write a function hiddenMessage(S) which takes a string splits it by
spaces, and returns a new string that is the n-th letter of the n-th word.
e.g., "I'm here" returns "Ie", and "Come to office hours" returns "Cofr"
Return the new string.
'''
def hiddenMessage(S):
    N = ""
    L = S.split(" ")
    for w in range(len(L)):
        N += L[w][w]
    return N

'''
Question 6: write a function onlyPositive(L) that inputs a list
and returns a new list that contains only the positive elements of the original
in the same order the original numbers occur.
You may assume the list has only numbers in it.
e.g., [1,2,3] returns [1,2,3], [0,1,2] returns [1,2], [-2,-1,0] returns []
Return the new list.
'''
def onlyPositive(L):
    N = []
    for i in range(len(L)):
        if L[i] > 0:
            N += [L[i]]
    return N

'''
Question 7: write a function reverseRecursive(L) that inputs a list
and recursively returns a new list which reverses the elements in the original.
e.g., [1,2,3] becomes [3,2,1]
Return the new list.
'''
def reverseRecursive(L):
    N = []
    if len(N) == len(L):
        return []
    N = reverseRecursive(L[1:]) + [L[0]]
    return N

'''
Question 8: write a function maxRecursive(L) that inputs a list
and recursively returns the maximum value in the list.
You may assume that len(L) >= 1.
e.g., maxRecursive([1,2,3]) = 3, maxRecursive([2,4,6,9,10,2,6]) = 10
Return the maximum value.
'''
def maxRecursive(L):
    if len(L) == 1:
        return L[0]
    return max(L[0], maxRecursive(L[1:]))

################################################################################

def testCountFirst():
    print("Testing countFirstLetter(L,letter)...", end="")
    assert(countFirstLetter(["dog","cat","bird","bear"],"d") == 1)
    assert(countFirstLetter(["dog","bird","bird","bear"],"e") == 0)
    assert(countFirstLetter(["mouse","cat","dog","fox"],"d") == 1)
    assert(countFirstLetter(["dog","cat","bird","bear"],"b") ==  2)
    assert(countFirstLetter(["dog","bird","bird","bear"],"b") == 3)
    assert(countFirstLetter(["mouse","cat","dog","fox"],"b") == 0)
    print("... done!")

def testMiddleAppend():
    print("Testing middleAppend(L,item)...", end="")
    assert(middleAppend([3, 4, 5],2) == [3,2,4,5])
    assert(middleAppend([4, 3, 5,7],6) == [4,3,6,5,7])
    assert(middleAppend([1,2,3,4,5,6],0) == [1,2,3,0,4,5,6])
    assert(middleAppend([1,5,3,7,9,23,45,67],100) == [1,5,3,7,100,9,23,45,67])
    assert(middleAppend(["dog","cat","bird","bear"],"mouse") == ["dog","cat","mouse","bird","bear"])
    print("... done!")

def testOdds():
    print("Testing odds(L)...", end="")
    L = [3,4,5]
    assert(odds([3,4,5]) == [4])
    assert(id(odds(L)) != id(L))
    assert(odds([4, 3, 5]) == [3])
    assert(odds([1,2,3,4,5,6]) == [2,4,6])
    assert(odds([1,5,3,7,9,23,45,67]) == [5,7,23,67])
    assert(odds(["dog","cat","bird","bear"]) == ["cat","bear"])
    assert(odds(["dog","bird","bird","bear"]) == ["bird", "bear"])
    assert(odds(["mouse","cat","dog","fox"]) == ["cat","fox"])
    print("... done!")

def testRemoveEvens():
    print("Testing removeEvens(L)...",)
    L = [3,4,5]
    removeEvens(L)
    print("Check if ",L," == ",[4])
    L = [4, 3, 5]
    removeEvens(L)
    print("Check if ",L,"==",[3])
    L = [1,2,3,4,5,6]
    removeEvens(L)
    print("Check if ",L," == ",[2,4,6])
    L = [1,5,3,7,9,23,45,67]
    removeEvens(L)
    print("Check if ",L," == ",[5,7,23,67])
    L = ["dog","cat","bird","bear"]
    removeEvens(L)
    print("Check if ",L," == ",["cat","bear"])
    L = ["dog","bird","bird","bear"]
    removeEvens(L)
    print("Check if ",L," == ",["bird", "bear"])
    L = ["mouse","cat","dog","fox"]
    removeEvens(L)
    print("Check if ",L," == ",["cat","fox"])
    assert(removeEvens([3,4,5]) == None)
    print("... done!")

def testHiddenMessage():
    print("Testing hiddenMessage(S)...", end="")
    assert(hiddenMessage("I") == "I")
    assert(hiddenMessage("See May Day") == "Say")
    assert(hiddenMessage("Happy Very Yelp Call Yellow") == "Hello")
    assert(hiddenMessage("Hear Monday Now Paid Money") == "Howdy")
    print("... done!")

def testOnlyPositive():
    print("Testing onlyPositive(L)...", end="")
    assert(onlyPositive([3, 4, 5]) == [3,4,5])
    assert(onlyPositive([-4, 3, 5]) == [3,5])
    assert(onlyPositive([-1,2,-3,4,-5,6]) == [2,4,6])
    assert(onlyPositive([1,5,-3,7,9,-23,-45,67]) == [1,5,7,9,67])
    assert(onlyPositive([-5,-4,-3,-2,-1]) == [])
    print("... done!")


def testReverse():
    print("Testing reverseRecursive(L)...", end="")
    assert(reverseRecursive([3, 4, 5]) == [5,4,3])
    assert(reverseRecursive([4, 3, 5]) == [5,3,4])
    assert(reverseRecursive([1,2,3,4,5,6]) == [6,5,4,3,2,1])
    assert(reverseRecursive([1,5,3,7,9,23,45,67]) == [67,45,23,9,7,3,5,1])
    assert(reverseRecursive(["dog","cat","bird","bear"]) == ["bear","bird","cat","dog"])
    assert(reverseRecursive(["dog","bird","bird","bear"]) == ["bear","bird","bird","dog"])
    assert(reverseRecursive(["mouse","cat","dog","fox"]) == ["fox","dog","cat","mouse"])
    print("... done!")

def testMax():
    print("Testing maxRecursive(L)...", end="")
    assert(maxRecursive([3, 4, 5]) == 5)
    assert(maxRecursive([4, 5, 1]) == 5)
    assert(maxRecursive([1,2,3,6,5,1]) == 6)
    assert(maxRecursive([67,5,3,7,9,23,45,0]) == 67)
    assert(maxRecursive(["dog","cat","bird","bear"]) == "dog")
    assert(maxRecursive(["dog","bird","elephant","bear"]) == "elephant")
    assert(maxRecursive(["mouse","cat","dog","fox"]) == "mouse")
    print("... done!")


def testAll():
    testCountFirst()
    testMiddleAppend()
    testOdds()
    testRemoveEvens()
    testHiddenMessage()
    testOnlyPositive()
    testReverse()
    testMax()

testAll()