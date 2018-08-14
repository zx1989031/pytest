#coding:utf8
def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    max=0
    num=0
    for key in range(0,len(line)):
        if(key==0):
            num=1
        else:
            if(line[key]==line[key-1]):
                num +=1
            else:
                num=1
            if(max<num):
                max=num
    return max


if __name__ == '__main__':
    print long_repeat('sssdsdsdadsb')
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert long_repeat('sdsffffse') == 4, "First"
    # assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    # assert long_repeat('abababaab') == 2, "Third"
    # assert long_repeat('') == 0, "Empty"
