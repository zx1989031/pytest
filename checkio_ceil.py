#coding:utf8
def checkio(numbers_array):
    number_list = []
    lossenum = []
    for i in numbers_array:
        if i<0:
            number_list.append(-i)
            lossenum.append(-i)
        else:
            number_list.append(i)

    number_list.sort()

    res = []
    for i in  number_list:
        if(i in lossenum):
            res.append(-i)
        else:
            res.append(i)
    return res

def checkio1(numbers_array):
    numbers_list = [abs(x) for x in numbers_array]
    lose = [abs(x) for x in numbers_array if x<0]
    orden = sorted(numbers_list)

    for x in orden:
        if x in lose:
            orden[orden.index(x)] = -x
    return orden

def checkio_other(numbers_array):
    absol = [abs(x) for x in numbers_array]  # We loop the list and return the absolute value of each item
    orden = sorted(absol)  # We sort the list with absolute values
    for x in numbers_array:  # loop the array and...
        for y in orden:  # loop the ordered array to compare each item between the 2 lists
            if y + x == 0:  # if the sum is 0 is because one item in the given list is negative
                orden[orden.index(
                    y)] = y * -1  # assign in that position the value of multiplying the item in that position by -1
    return orden

    # return numbers_array
def check_others(numbers_array):
    return sorted(numbers_array, key=lambda x: abs(x))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print checkio((1,3,4,-5))
    print checkio1((1,3,4,-5))
    print checkio_other((1,3,4,-5))
    print check_others((1,3,4,-5))
    # def check_it(array):
    #     if not isinstance(array, (list, tuple)):
    #         raise TypeError("The result should be a list or tuple.")
    #     return list(array)
    #
    # assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    # assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    # assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
