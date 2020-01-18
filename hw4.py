'''
15-110 Homework 4
Name: Clara Ye
Andrew ID: zixuany
'''

################################################################################

''' #1 - createAuthorMap(bookMap) - 10pts
Write the function createAuthorMap which takes bookMap, a dictionary that maps 
book titles (strings) to their authors (also strings), and returns a new dictionary
that maps authors to lists of all the books they've written. Make sure not to
destructively modify bookMap as you generate the new dictionary!
'''

def createAuthorMap(bookMap):
    authorMap = {}
    for book in bookMap:
        if bookMap[book] not in authorMap:
            authorMap[bookMap[book]] = [book]
        else:
            authorMap[bookMap[book]] += [book]
    return authorMap


''' #2 - findFile(t, name) - 10pts
We can represent a filesystem as a tree by making each folder a node with 
children, where the children are the items in the folder. Files are then nodes 
with no children. We'll use the general dictionary tree structure we demonstrated 
in class for this problem, which maps the key "children" to a list of 
dictionaries (child nodes).

Given a tree t that represents a file system and a filename name (a string), 
write the function findFile(t, name) which returns True if that filename exists 
in the file system, and False otherwise. Note that the filenames will be in the 
values of the nodes.

Solving this problem for a tree with no children (a file) should be easy. To 
solve the problem for a tree with children (a folder), consider this: if you can 
find the filename in any of the child trees, then you can return True right away! 
On the other hand, if you search all the children and the file is in none of them, 
you can return False.
'''

def findFile(t, name):
    if t["value"] == name:
        return True
    else:
        for child in t["children"]:
            if findFile(child, name):
                return True
        return False


''' #3 - nearestNeighbor(nodeList, edgeMatrix, node) - 10pts
We can represent cities in the United States as nodes in a graph, and use edges 
to connect the cities that offer flights from one to the other. We can also give 
those edges values- the distance from one city to another.

Write the function nearestNeighbor(nodeList, edgeMatrix, node) which takes a 
graph in adjacency matrix format (nodeList and edgeMatrix) and a string, 
node (a city name), and returns the closest neighbor to node. For example, in 
the graph shown in the write-up, Pittsburgh's nearest neighbor would be Washington DC.

Recall that in adjacency matrix format, a graph's node list is a 1D list that 
maps each index to a node value (in this case, the name of a city), and an edge 
matrix is a 2D list, where matrix[i][j] represents the value of the edge between 
nodeList[i] and nodeList[j], or None if they are not connected.

To write this function, you will need to take the following steps:
 - Identify the index in nodeList of the given city, node.
 - Keep track of two data values - the current closest city and the current
   shortest distance. These can start as None and a very large number, like 1000.
 - Iterate over each city index in the edge matrix.
   -- If there exists an edge between that city index and our node city, 
      compare the distance between the two to the current shortest distance.
   -- If the edge distance is smaller, update the current closest city and 
      current shortest distance.
 - Once you have checked all the cities, return the current closest city.
'''

def nearestNeighbor(nodeList, edgeMatrix, node):
    for index in range(len(nodeList)):
        if nodeList[index] == node:
            i = index
    closestCity = None
    minDistance = 9999
    for j in range(len(nodeList)):
        if edgeMatrix[i][j] != None and edgeMatrix[i][j] < minDistance:
            minDistance = edgeMatrix[i][j]
            closestCity = nodeList[j]
    return closestCity
    

''' #4 - getAllFollowers(network, name) - 15pts
It's easy to determine the number of followers you have on a social media platform
like Twitter, but the displayed number does not account for people who follow your
followers, but do not (yet) follow you. We want to determine how many 
eventual-followers a person has.

An eventual-follower of X is either 
a) someone who follows X, or 
b) someone other than X who is a follower of another person, Y, who is an 
   eventual-follower of X.

View the written starter file for an in-depth example of how eventual-followers work.

Write the function getAllFollowers(network, name) which takes a graph in the
dictionary format, network, and a string, name, and returns a list of all 
eventual-followers of name. 

Major Hint: This problem is a variant on the idea of searching a graph! Instead of 
searching for an item, it's just searching for ALL the nodes connected to the start.

If you're lost, try starting with the breadth-first search or depth-first search 
from the class notes, then modify it to return a list of followers instead of 
True or False. You'll need to change two parts of the function: the part that 
actually checks if an item has been found, and the value that is returned at the end.
'''

def getAllFollowers(network, name):
    eventual = []
    potential = [name]
    while potential != []:
        person = potential[0]
        potential.pop(0)
        if person not in eventual:
            followers = network[person]
            potential = followers + potential
            eventual.append(person)
    if name in eventual:
        eventual.remove(name)
    return eventual


################################################################################

''' To check your work, click 'Run File as Script' to run the test function
shown below. You should also check the autograder results on Gradescope! '''

def testCreateAuthorMap():
    print("Testing createAuthorMap()...")
    assert(createAuthorMap({ "Test" : "Test" }) != None)
    print("Check that " + str(createAuthorMap({ "The Hobbit" : "JRR Tolkein", "Harry Potter" : "JK Rowling", "Lord of the Rings" : "JRR Tolkein", "Casual Vacancy" : "JK Rowling", "A Game of Thrones" : "George RR Martin", "A Storm of Swords" : "George RR Martin" })) + " returns " + str({ "JRR Tolkein" : ["The Hobbit", "Lord of the Rings"], "JK Rowling" : ["Harry Potter", "Casual Vacancy"], "George RR Martin" : ["A Game of Thrones", "A Storm of Swords"] }))
    print("Check that " + str(createAuthorMap({ "A Wrinkle in Time" : "Madeline L'Engle", "The Golden Compass" : "Phillip Pullman", "The Subtle Knife" : "Phillip Pullman", "The Amber Spyglass" : "Phillip Pullman" })) + " returns " + str({ "Madeline L'Engle" : ["A Wrinkle in Time"], "Phillip Pullman" : ["The Golden Compass", "The Subtle Knife", "The Amber Spyglass"]}))
    print("Check that " + str(createAuthorMap({ "A Natural History of Dragons" : "Marie Brennan"})) + " returns " + str({ "Marie Brennan" : ["A Natural History of Dragons"] }))
    print("Check that " + str(createAuthorMap({ })) + " returns " + str({ }))
    print("... done!")

def testFindFile():
    print("Testing findFile()...", end="")
    t1 = { "value" : "FolderA", "children" :
            [ { "value" : "FolderB", "children" :
                [ { "value" : "File1", "children" : [ ] },
                  { "value" : "File2", "children" : [ ] }
                ]
              },
              { "value" : "File3", "children" : [ ] }
            ]
        }
    assert(findFile(t1, "File1") == True)
    assert(findFile(t1, "File2") == True)
    assert(findFile(t1, "File3") == True)
    assert(findFile(t1, "File4") == False)
    t2 = { "value" : "FolderJ", "children" :
            [ 
              { "value" : "FolderK", "children" :
                [ 
                  { "value" : "FolderM", "children" : 
                    [ 
                      { "value" : "Folder0", "children" :
                        [ 
                          { "value" : "File12", "children" : [ ] }
                        ] 
                      }
                    ] 
                  },
                  { "value" : "File2", "children" : [ ] }
                ]
              },
              { "value" : "File10", "children" : [ ] },
              { "value" : "File11", "children" : [ ] },
              { "value" : "FolderN", "children" : 
                [ 
                  { "value" : "File13", "children" : [ ] },
                  { "value" : "File14", "children" : [ ] }
                ]
              },
              { "value" : "FolderL", "children" :
                [ 
                  { "value" : "Foobar", "children" : [ ] }
                ]
              }
            ]
        }
    assert(findFile(t2, "File10") == True)
    assert(findFile(t2, "File12") == True)
    assert(findFile(t2, "File14") == True)
    assert(findFile(t2, "Foobar") == True)
    assert(findFile(t2, "File9") == False)
    assert(findFile(t2, "Secret") == False)
    t3 = { "value" : "File1", "children" : [ ] }
    assert(findFile(t3, "File1") == True)
    assert(findFile(t3, "File2") == False)
    print("... done!")

def testNearestNeighbor():
    print("Testing nearestNeighbor()...", end="")
    nodeList = ["Detroit", "New York City", "Pittsburgh", "Philadelphia", "Baltimore", "Washington DC"]
    matrix = [
                [ None,  587,  277, None, None,  499 ],
                [  587, None, None,   88, None, None ],
                [  277, None, None,  289,  224,  223 ],
                [ None,   88,  289, None,   99, None ],
                [ None, None,  224,   99, None,   36 ],
                [  499, None,  223, None,   36, None ]
             ]
    assert(nearestNeighbor(nodeList, matrix, "Pittsburgh") == "Washington DC")
    assert(nearestNeighbor(nodeList, matrix, "Detroit") == "Pittsburgh")
    assert(nearestNeighbor(nodeList, matrix, "Washington DC") == "Baltimore")
    assert(nearestNeighbor(nodeList, matrix, "Baltimore") == "Washington DC")
    assert(nearestNeighbor(nodeList, matrix, "New York City") == "Philadelphia")
    assert(nearestNeighbor(nodeList, matrix, "Philadelphia") == "New York City")
    print("... done!")

def testGetAllFollowers():
    print("Testing getAllFollowers()...", end="")
    d1 = { "Jasnah" : [ "Shallan", "Dalinar" ], 
           "Dalinar" : [ "Shallan", "Adolin", "Kaladin" ],
           "Kaladin" : [ "Adolin" ], "Adolin" : [ "Shallan" ], 
           "Shallan" : [ "Adolin", "Veil", "Radiant" ],
           "Veil" : [ "Shallan", "Radiant" ], "Radiant" : [ "Shallan", "Veil" ],
           "Sadaes" : [ ] }
    assert(getAllFollowers(d1, "Kaladin") != None)
    result1 = getAllFollowers(d1, "Jasnah")
    assert(sorted(result1) == [ "Adolin", "Dalinar", "Kaladin", "Radiant", "Shallan", "Veil" ])
    result2 = getAllFollowers(d1, "Dalinar")
    assert(sorted(result2) == [ "Adolin", "Kaladin", "Radiant", "Shallan", "Veil" ])
    result3 = getAllFollowers(d1, "Kaladin")
    assert(sorted(result3) == [ "Adolin", "Radiant", "Shallan", "Veil" ])
    result4 = getAllFollowers(d1, "Adolin")
    assert(sorted(result4) == [ "Radiant", "Shallan", "Veil" ])
    result5 = getAllFollowers(d1, "Shallan")
    assert(sorted(result5) == [ "Adolin", "Radiant", "Veil" ])
    result6 = getAllFollowers(d1, "Veil")
    assert(sorted(result6) == [ "Adolin", "Radiant", "Shallan" ])
    result7 = getAllFollowers(d1, "Radiant")
    assert(sorted(result7) == [ "Adolin", "Shallan", "Veil" ])
    assert(getAllFollowers(d1, "Sadaes") == [ ])
    print("... done!")

def testAll():
    testCreateAuthorMap()
    testFindFile()
    testNearestNeighbor()
    testGetAllFollowers()

testAll()