#coding:utf8
def is_stressful(subj):
    """
        recoognise stressful subject
    """
    import re
    pattern1 = "h\S?e\S?l\S?p"
    pattern2 = "a\S?s\S?a\S?p"
    pattern3 = "u\S?r\S?g\S?e\S{0,}n\S?t"
    pattern4 = "!{3,}$"
    pattern5 = "[a-z]"


    strs = subj.lower()
    if(re.search(pattern1,strs) or re.search(pattern2,strs) or re.search(pattern3,strs) or re.search(pattern4,strs)):
        return True
    else:
        if (re.search(pattern5, subj)):
            return False
        else:
            return True

def is_stressful_other(subj):
    """
        recoognise stressful subject
    """
    from itertools import groupby
    import string
    if subj.endswith('!!!'):
        return True

    simple_subj = ''.join(c for c in subj if str.isalpha(c) or c == ' ')

    if 0 == [word.isupper() for word in simple_subj.split()].count(False):
        return True

    red_words = ['help','asap','urgent']

    for w in simple_subj.split():
        v = ''.join(k for k, _ in groupby(w.lower()))
        if v in red_words:
            return True
    return False


def is_stressful_best(subj):
    return subj.endswith('!!!') or \
           subj.isupper() or \
           any(__import__('re').search('+[.!-]*'.join(w), subj.lower()) for w in ["help", "asap", "urgent"])


def test():
    print ['+[.!-]*'.join(w) for w in ['help','asap','urgent']]


if __name__ == '__main__':
    print is_stressful("HI HOW ARE YOUe")
    print is_stressful_best("HI HOW ARE YOU")
    print test()
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert is_stressful("Hi") == False, "First"
    # assert is_stressful("I neeed HELP") == True, "Second"
