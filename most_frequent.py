#coding:utf8
def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    strdic =  {word:"".join(data).count(word) for word in data}
    return sorted(strdic,key=lambda x:strdic[x])[-1]


def most_frequent1(data):
    strdic = {word: "".join(data).count(word) for word in data}
    return max(strdic, key=strdic.get)

def most_frequent_other(data):
    # print type([0,1,3])
    d={}
    for l in data:
        if l not in d:
            d[l]=1
        else:
            d[l]+=1
    return max(d,key=d.get)

if __name__ == '__main__':
    print (most_frequent(["b","b","c","a","b","a"]))
    print (most_frequent1(["b","b","c","a","b","a"]))
    print (most_frequent_other(["b","b","c","a","b","a"]))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # print('Example:')
    # print(most_frequent([
    #     'a', 'b', 'c',
    #     'a', 'b',
    #     'a'
    # ]))
    #
    # assert most_frequent([
    #     'a', 'b', 'c',
    #     'a', 'b',
    #     'a'
    # ]) == 'a'
    #
    # assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    # print('Done')