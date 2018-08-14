#coding:utf8
#/usr/bin/python
#fileName:patten2.py
def popular_words(text,words):
    # your code here
    arr = text.split()
    testStr = {}
    for x in words:
        testStr[x.lower()] = 0
        for z in arr:
            if (z.lower() == x.lower()):
                if (x.lower() in testStr):
                    testStr[x.lower()] = testStr[x.lower()] + 1
                else:
                    testStr[x.lower()] = 1

    return testStr


def popular_words_other(text, words):
    text_parsed = text.lower().replace('\n', ' ').split(' ')

    return {word: text_parsed.count(word) for word in words}

if __name__ == '__main__':
    print popular_words('''
        When I was One
        I had just begun
        When I was Two
        I was nearly new
''', ['i', 'was', 'Two', 'near'])

    # print("Example:")
#     print(popular_words('''
# When I was One
# I had just begun
# When I was Two
# I was nearly new
# ''', ['i', 'was', 'three', 'near']))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert popular_words('''
# When I was One
# I had just begun
# When I was Two
# I was nearly new
# ''', ['i', 'was', 'three', 'near']) == {
#         'i': 4,
#         'was': 3,
#         'three': 0,
#         'near': 0
#     }
#     print("Coding complete? Click 'Check' to earn cool rewards!")
