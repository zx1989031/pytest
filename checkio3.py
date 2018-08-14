#coding:utf8
def find_message(text):
    """Find a secret message"""
    str = ''
    for word in text:
        if(64<ord(word)<91):
            str = str+word

    return str

def find_message_pattern(text):
    import re
    pattern = r"[A-Z]"
    print re.search(pattern,text).group()

def find_message_other(text):
    import re
    pattern = re.compile(r'[A-Z]')
    return ''.join(pattern.findall(text))

if __name__ == '__main__':
    print find_message("Hello World")
    print find_message_other("Hello World")
    print find_message_pattern("Hello World")

    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    # assert find_message("hello world!") == "", "Nothing"
    # assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
