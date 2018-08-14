#coding:utf8
def to_encrypt(text, delta):
    #replace this for solution
    print (ord('a'))
    str = ''
    for val in text:
        if delta>0:
            num = delta
        else:
            num = delta+26
        if (96 < ord(val) < 123):
            if(ord(val)+num>122):
                str += chr(ord('a')+ord(val)+num-122-1)
            elif(ord(val)+num<97):
                str += chr(ord('z')-ord(val)+num-96-1)
            else:
                str += chr(ord(val)+num)
        else:
            str += val
    return str

if __name__ == '__main__':
    print (to_encrypt('t',10))
    # print("Example:")
    # print(to_encrypt('abc', 10))
    #
    # #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert to_encrypt("a b c", 3) == "d e f"
    # assert to_encrypt("a b c", -3) == "x y z"
    # assert to_encrypt("simple text", 16) == "iycfbu junj"
    # assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    # assert to_encrypt("state secret", -13) == "fgngr frperg"
