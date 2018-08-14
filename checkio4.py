#coding:utf8
def checkio(words):
    import re
    # pattern = "([a-z]+\s{1})([a-z]+\s{1})"
    pattern = "[a-zA-Z]+\s{1}[a-zA-Z]+\s{1}[a-zA-Z]+"
    print re.search(pattern, words).group()

    return True if re.search(pattern, words) else False



def checkio_other(words):
    a = 0
    for x in words.split():
        if x.isalpha():
            a += 1
            if a > 2:
                break
        else:
            a = 0
    return True if a > 2 else False

def checkio_ohters(words):
    words_list = words.split(' ')
    length = len(words_list)
    # print(words_list)
    i = 0
    if length >= 3:
        while i + 3 <= length:
            if ''.join(words_list[i:i + 3]).isalpha():
                return True
            i += 1
    return False
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio('Hello World hello'))

    # assert checkio("Hello World hello") == True, "Hello"
    # assert checkio("He is 123 man") == False, "123 man"
    # assert checkio("1 2 3 4") == False, "Digits"
    # assert checkio("bla bla bla bla") == True, "Bla Bla"
    # assert checkio("Hi") == False, "Hi"
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
