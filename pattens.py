#codinf:utf8
#/usr/bin/python
#fileName:pattens.py


def between_markers(text,begin,end):
    import re
    str1 = ''
    for i in begin:
        if(64<ord(i.upper())<91):
            str1=str1+i
        else:
            str1=str1+'\\'+i
    str2=''
    for i in end:
        if(64<ord(i.upper())<91):
            str2=str2+i
        else:
            str2=str2+'\\'+i

    if (str(re.search(str1, text)) == 'None' and str(re.search(str2, text)) == 'None'):
        pattern = "(.*)"
    elif (str(re.search(str1, text)) == 'None'):
        pattern = "(.*)" + str2
    elif (str(re.search(str2, text)) == 'None'):
        pattern = str1 + "(.*)"
    else:
        pattern = str1 + "(.*)" +str2

    if (str(re.search(pattern, text)) == 'None'):
        print None
    else:
        print re.search(pattern, text).group(1)
    # return re.search(patten,text).group()


def text_len(text,begin,end):
    start = text.find(begin)+len(begin) if begin in text else 0
    stop = text.find(end) if end in text else len(text)

    print text[start:stop]



def __max__():
    pass

if __name__ == '__main__':
    # between_markers('No[/b] hi', '[b]', '[/b]')

    text_len('[b]No<hi>', '[b]', '[/b]')
    #print('Example:')
    #print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    # assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    # assert between_markers("<head><title>My new site</title></head>",
    #                        "<title>", "</title>") == "My new site", "HTML"
    # assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    # assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    # assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    # assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    # print('Wow, you are doing pretty good. Time to check it!')

# betwwen_markers("<b>my name is zs","<b>","</b>")

