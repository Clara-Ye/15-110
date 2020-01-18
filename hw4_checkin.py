'''
15-110 Homework 4 Check-in
Name: Clara Ye
Andrew ID: zixuany
'''

################################################################################

''' #1 - createPhonebook(nameList, numberList) - 20pts
Write the function createPhonebook that takes two lists, a list of names and a 
list of phone numbers (both strings), and returns a dictionary mapping names to 
phone numbers. You may assume that each person is in the same index as their phone number.

If a person occurs in the nameList multiple times (in other words, if they have 
multiple phone numbers), you should map their name to the first phone number 
they were paired with. For example, given the list of names 
["Kelly", "Stephanie", "Kelly"] and the list of numbers ["0000", "1234", "9876"], 
the function would return the dictionary { "Kelly" : "0000", "Stephanie" : "1234" }.

'''

def createPhonebook(nameList, numberList):
    phoneBook = {}
    for i in range(len(nameList)):
        if nameList[i] not in phoneBook:
            phoneBook[nameList[i]] = numberList[i]
    return phoneBook


''' #2 - sumTree(t) - 20pts
Write the function sumTree(t) that takes a binary tree and returns the sum of all 
the values in the tree. Remember that you'll have to use recursion to iterate 
over all the elements of the tree!

The tree will be in the dictionary structure discussed in class: each node is a 
dictionary with three keys; "value", "left", and "right". If the left or right 
sub-tree doesn't exist, that key maps to None.
'''

def sumTree(t):
    sum = t["value"]
    if t["left"] != None:
        sum += sumTree(t["left"])
    if t["right"] != None:
        sum += sumTree(t["right"])
    return sum
    
# a clearer way:

def sumTree(t):
    if t["left"] == None and t["right"] == None:
        return t["value"]
    elif t["left"] != None and t["right"] == None:
        return t["value"] + sumTree(t["left"])
    elif t["left"] == None and t["right"] != None:
        return t["value"] + sumTree(t["right"])
    else:
        return t["value"] + sumTree(t["left"]) + sumTree(t["right"])

################################################################################

''' To check your work, click 'Run File as Script' to run the test function
shown below. You should also check the autograder results on Gradescope! '''

def testCreatePhonebook():
    print("Testing createPhonebook()...", end="")
    assert(createPhonebook(["Rebecca", "Ellie", "Gayatri", "Rishab"], ["5", "3", "7", "1"]) == { "Rebecca" : "5", "Ellie" : "3", "Gayatri" : "7", "Rishab" : "1" })
    assert(createPhonebook(["Kelly", "Stephanie", "Kelly"], ["0000", "1234", "9876"]) == { "Kelly" : "0000", "Stephanie" : "1234" })
    assert(createPhonebook(["Stella", "Stella", "Stella"], ["1234", "5678", "9"]) == { "Stella" : "1234" })
    assert(createPhonebook(["CMU"], ["412-268-2000"]) == { "CMU" : "412-268-2000" })
    assert(createPhonebook([ ], [ ]) == { })
    print("... done!")

def testSumTree():
    print("Testing sumTree()...", end="")
    t1 = {  "value" : 5,
            "left"  :   { "value" : 2,
                          "left"  : None,
                          "right" : None 
                        },
            "right" :   { "value" : 8,
                          "left"  : None,
                          "right" : None 
                        } 
         }
    assert(sumTree(t1) == 15)
    t2 = {  "value" : 5,
            "left"  :   { "value" : 2,
                          "left"  : { "value" : 1,
                                      "left"  : None,
                                      "right" : None
                                    },
                          "right" : { "value" : 4,
                                      "left"  : None,
                                      "right" : None
                                    }
                        },
            "right" :   { "value" : 8,
                          "left"  : { "value" : 6,
                                      "left"  : None,
                                      "right" : None
                                    },
                          "right" : { "value" : 10,
                                      "left"  : None,
                                      "right" : None
                                    }
                        } 
         }
    assert(sumTree(t2) == 36)
    t3 = {  "value" : 5,
            "left"  : None,
            "right" : None
         }
    assert(sumTree(t3) == 5)
    t4 = {  "value" : 5,
            "left"  :   { "value" : 4,
                          "left"  : { "value" : 3,
                                      "left"  : { "value" : 1,
                                                  "left"  : None,
                                                  "right" : { "value" : 2,
                                                              "left"  : None,
                                                              "right" : None
                                                            }
                                                },
                                      "right" : None
                                    },
                          "right" : None
                        },
            "right" : None
         }
    assert(sumTree(t4) == 15)
    t5 = {  "value" : 10,
            "left"  :   { "value" : 7,
                          "left"  : None,
                          "right" : { "value" : 9,
                                      "left"  : None,
                                      "right" : None
                                    }
                        },
            "right" :   { "value" : 14,
                          "left"  : { "value" : 12,
                                      "left"  : None,
                                      "right" : None
                                    },
                          "right" : { "value" : 15,
                                      "left"  : None,
                                      "right" : None
                                    }
                        } 
         }
    assert(sumTree(t5) == 67)
    print("... done!")

def testAll():
    testCreatePhonebook()
    testSumTree()

testAll()