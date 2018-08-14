#coding:utf8
def checkio(*args):
   arr = [e for e in args]
   arr.sort()
   if len(arr)==0:
       return 0
   else:
       return arr[-1]-arr[0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print checkio(1,2,3)
    # def almost_equal(checked, correct, significant_digits):
    #     precision = 0.1 ** significant_digits
    #     return correct - precision < checked < correct + precision
    #
    # assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    # assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
    # assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    # assert almost_equal(checkio(), 0, 3), "Empty"
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")