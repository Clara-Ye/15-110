'''
HW5 Checkin
Name: Clara Ye
Andrew ID: zixuany

'''

'''
file_to_count(filename) should take as input a filename, open the file and count
all of the words in the file. The file contains one line for each word. The function 
should return the total number of words in the file.

For example, a file containing:
Fifteen
One
Ten
Is
Awesome

would return 5
'''
def file_to_count(filename):
    f = open(filename,"r")
    text = f.read()
    f.close()
    count = 0
    for line in text.split("\n"):
        if len(line) != 0:
            count += 1
    return count


'''
combine_counts(count_list) should take as input the list of all of the counts
returned by file_to_count, and return the sum of those counts.

For example: combine_counts([5,6,2,3,1,7]) should return 24
'''
def combine_counts(count_list):
    sum = 0
    for count in count_list:
        sum += count
    return sum

'''
file_to_search(filename,word) should take as input a filename and a word to
search for. It should open the file and search for the exact given word.
The file contains one line for each word. Note that the words in the file are
in alphbetical order and you can choose to use that information if you would
like to speed up your search.

The function should return a boolean of whether the file contains the word.

For example, given a file containing:
Fifteen
One
Ten
Is
Awesome

file_to_search(filename,"One") = True
file_to_search(filename,"Two") = False
file_to_search(filename,"we") = False
'''
def file_to_search(filename,word):
    f = open(filename, "r")
    text = f.read()
    f.close()
    for line in text.split("\n"):
        if line == word:
            return True
    return False


'''
combine_search(search_results) should take as input a list of booleans
and return the first index of True or -1 if none of the values are True.

For example: combine_search([False, False, True]) should return 2
            combine_search([False, False, False]) should return -1
'''
def combine_search(search_results):
    for i in range(len(search_results)):
        if search_results[i]:
            return i
    return -1

'''
file_to_subsearch(filename,substring) should take as input a filename and a
substring to search for. It should open the file and search for the substring
in each word. The file contains one line for each word.

The function should return a list of all words that contain that substring in
the file. Make sure to remove the \n from each word for readability.

For example, given a file containing:
Fifteen
One
Ten
Is
Awesome

file_to_search(filename,"en") = ["Fifteen","Ten"]
'''
def file_to_subsearch(filename,substring):
    f = open(filename, "r")
    text = f.read()
    f.close()
    l = []
    for line in text.split("\n"):
        if substring in line:
            l.append(line)
    return l


'''
combine_lists(search_result_lists) should take as input a list of lists and 
return the merged list of all words together.

For example: combine_lists([["cat","cats"],["catastrophe","certificate"]])
 should return ["cat","cats","catastrophe","certificate"]
'''
def combine_lists(search_result_lists):
    l = []
    for list in search_result_lists:
        l += list
    return l


##############################################################################

def test_filetocount():
    assert(file_to_count("wordlist1.txt") == 1000)
    assert(file_to_count("wordlist2.txt") == 1000)
    assert(file_to_count("wordlist3.txt") == 1000)
    assert(file_to_count("wordlist4.txt") == 1000)
    assert(file_to_count("allwords.txt") == 10000)

def test_combinecount():
    assert(combine_counts([1000,1000]) == 2000)
    assert(combine_counts([1000,1000,1000]) == 3000)
    assert(combine_counts([1000,1000,1000,1000]) == 4000)

def test_filetosearch():
    assert(file_to_search("wordlist1.txt","dog") == False)
    assert(file_to_search("wordlist2.txt","dog") == False)
    assert(file_to_search("wordlist3.txt","dog") == True)
    assert(file_to_search("wordlist4.txt","dog") == False)
    assert(file_to_search("allwords.txt","dog") == True)

def test_combinesearch():
    assert(combine_search([False, False, True])==2)
    assert(combine_search([False, False, False]) ==-1)
    assert(combine_search([True, False, True]) == 0)


def test_filetosubsearch():
    assert(file_to_subsearch("wordlist1.txt","dog") == [])
    lst = file_to_subsearch("wordlist3.txt","dog")
    assert(len(lst) == len(["dog","dogs"]))
    for item in ["dog","dogs"]:
        assert(item in lst)
    lst = file_to_subsearch("allwords.txt","dog")
    assert(len(lst) == len(["dog","dogs"]))
    for item in ["dog","dogs"]:
        assert(item in lst)

def test_combinelists():
    lst=  combine_lists([["cat","cats"],["catastrophe","certificate"]])
    answer = ["cat","cats","catastrophe","certificate"]
    assert(len(lst) == len(answer))
    for item in answer:
        assert(item in lst)
    lst = combine_lists([[],["mouse"]])
    answer = ["mouse"]
    assert(len(lst) == len(answer))
    for item in answer:
        assert(item in lst)


def testAll():
    test_filetocount()
    test_combinecount()
    test_filetosearch()
    test_combinesearch()
    test_filetosubsearch()
    test_combinelists()

if __name__ == '__main__':
    testAll()