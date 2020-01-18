'''
15-110 Homework 3 Check-in 2
Name: Clara Ye
Andrew ID: zixuany
Enter your code below the comments
'''

'''
Question 1: write a function reverse(L) that inputs a list
and returns a new list which reverses the elements in the original.
e.g., [1,2,3] becomes [3,2,1]
Return the new list.
'''
def reverse(L):
    for i in range(len(L) // 2):
        temp = L[i]
        L[i] = L[len(L) - 1 - i]
        L[len(L) - i - 1] = temp
    return L

'''
Question 2: write a function merge(L1,L2) which takes two lists
and interleaves the elements in the following way: L1[0], L2[0], L1[1], L2[1], ...
The length of the new list will be len(L1)+len(L2)
You may assume the lists are the same length.
Return the new list.
Note: do not destroy either list.
'''
def merge(L1,L2):
    L = []
    for i in range(len(L1)):
        L += [L1[i]]
        L += [L2[i]]
    return L

'''
Question 3: write a function removeDups(L) which takes a list and
returns a new list with the duplicate values removed.
Hint: think about when to add values to the new list rather than remove them.
[1,3,2,1,2,4,3,4] -> [1,3,2,4]
Return the new list.
'''
def removeDups(L):
    N = []
    for i in range(len(L)):
        if L.count(L[i]) == 1:
            N += [L[i]]
    return N

'''
Question 4: Edit the following code so that removing elements from L1 does not affect
L2's value. Do not modify the return line, it is correct.
'''
def removeVals(L):
    L1 = L
    L2 = L + []
    L1.remove(0)
    L1.remove(-1)
    L1.remove(1)
    return L1,L2


'''
Question 5: Edit the following code so that it modifies the original list
'''
def insertVals(L):
    for i in range(len(L)):
        L.append(i)
    return L



################################################################################

''' To check your work, click 'Run File as Script' to run the test function
shown below. You should also check the autograder results on Gradescope! '''
def testReverse():
    print("Testing reverse(L)...", end="")
    assert(reverse([3, 4, 5]) == [5,4,3])
    assert(reverse([4, 3, 5]) == [5,3,4])
    assert(reverse([1,2,3,4,5,6]) == [6,5,4,3,2,1])
    assert(reverse([1,5,3,7,9,23,45,67]) == [67,45,23,9,7,3,5,1])
    assert(reverse(["dog","cat","bird","bear"]) == ["bear","bird","cat","dog"])
    assert(reverse(["dog","bird","bird","bear"]) == ["bear","bird","bird","dog"])
    assert(reverse(["mouse","cat","dog","fox"]) == ["fox","dog","cat","mouse"])
    print("... done!")

def testMerge():
    print("Testing merge(L1,L2)...", end="")
    assert(merge([1],[2]) == [1,2])
    assert(merge([1,2,3],[1,2,3]) == [1,1,2,2,3,3])
    assert(merge([1,2,3],[4,5,6]) == [1,4,2,5,3,6])
    assert(merge([1,3,5],[2,4,6]) == [1,2,3,4,5,6])
    assert(merge([8,6,4,2],[7,5,3,1]) == [8,7,6,5,4,3,2,1])
    print("... done!")

def testRemoveDups():
    print("Testing removeDups(L)...")
    a = [1]
    print("Check if",a," changes to ",removeDups(a),"after duplicates are removed.")
    print("---")
    a = [1,1]
    print("Check if",a," changes to ",removeDups(a),"after duplicates are removed.")
    print("---")
    a = [1,2]
    print("Check if",a," changes to ",removeDups(a),"after duplicates are removed.")
    print("---")
    a = [1,1,2,3,4,4]
    print("Check if",a," changes to ",removeDups(a),"after duplicates are removed.")
    print("---")
    a = [1,2,3,4,5,6,6,5,4,3,2,1]
    print("Check if",a," changes to ",removeDups(a),"after duplicates are removed.")
    print("... done! Check to see if the output is correct")

def testRemoveVals():
    print("Testing removeVals(L)...", end="")
    lists = removeVals([-1,2,1,4,3,0,2])
    assert(lists[0] != lists[1])
    lists = removeVals([-1,6,-1,5,1,0,2])
    assert(lists[0] != lists[1])
    lists = removeVals([3,1,0,-1,1,2,7])
    assert(lists[0] != lists[1])
    print("... done!")

def testInsertVals():
    print("Testing insertVals(L)...", end="")
    L = [-1,2,1,4,3,0,2]
    A = insertVals(L)
    assert(id(L) == id(A))
    L = [-1,6,-1,5,1,0,2]
    A = insertVals(L)
    assert(id(L) == id(A))
    L = [3,1,0,-1,1,2,7]
    A = insertVals(L)
    assert(id(L) == id(A))
    print("... done!")


def testAll():
    testReverse()
    testMerge()
    testRemoveDups()
    testRemoveVals()
    testInsertVals()

testAll()

