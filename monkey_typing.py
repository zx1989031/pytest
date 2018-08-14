#coding:utf8
def count_words(text, words):
    g=lambda g:text.lower().count(g.lower())

    if(sum([g(word) for word in words])<len(words)):
        return sum([g(word) for word in words])
    else:
        return len(words)



if __name__ == '__main__':
    print count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"})
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    # assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    # assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
    #                    {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
