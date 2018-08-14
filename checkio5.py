#coding:utf8
def index_power(array,n):
    """
        Find Nth power of the element with index N.
    """
    if len(array)>n:
        return pow(array[n-1],n)
    else:
        return -1


def index_power_other(array,n):
    return pow(array[n],n) if len(array)>n else -1

def index_power_other1(array,n ):
    """
        Find Nth power of the element with index N.
    """
    try:
        return array[n]**n
    except IndexError:
        return -1

if __name__ == '__main__':
    print index_power([1,2,3,4],2)
    print index_power_other([1,2,4],2)
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    # assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    # assert index_power([0, 1], 0) == 1, "Zero power"
    # assert index_power([1, 2], 3) == -1, "IndexError"
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
