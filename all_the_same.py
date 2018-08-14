#coding:utf8
#from typing import List, Any
def all_the_same(elements):
    # your code here
    return  True if len(list(set(elements)))<2 else False


def all_the_same_other(elements):
    # your code here
    return all([elem==elements[0]for elem in elements])

if __name__ == '__main__':
    print all_the_same([1,2,3])
    print all_the_same_other([1,2,3])
    # print("Example:")
    # print(all_the_same([1, 1, 1]))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert all_the_same([1, 1, 1]) == True
    # assert all_the_same([1, 2, 1]) == False
    # assert all_the_same(['a', 'a', 'a']) == True
    # assert all_the_same([]) == True
    # assert all_the_same([1]) == True
