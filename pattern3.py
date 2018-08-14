#coding:utf8
#/usr/bin/python
#fileName:pattern3.py

def bigger_price(limit,data):
    """
        TOP most expensive goods
    """
    # your code here
    tmp =[]
    for x in data:
        tmp.append(x['price'])

    tmp.sort(reverse=True)
    res=[]
    for x in tmp[0:limit]:
        for y in data:
            if y['price']==x:
                res.append(y)

    return res
def bigger_price_other(limit, data):
    return sorted(data, key=lambda data: data["price"], reverse=True)[:limit]

def bigger_price_other1(limit, data):
    return sorted(data, key=lambda x: x["price"], reverse=True)[:limit]
if __name__ == '__main__':
    # print [0,100,20,40][-2:]

    print(bigger_price(2,[{"price":100,"name":"bread"},{"price":138,"name":"wine"},{"price":15,"name":"meat"},{"price":1,"name":"water"}]))
    print(bigger_price_other(2,[{"price":100,"name":"bread"},{"price":138,"name":"wine"},{"price":15,"name":"meat"},{"price":1,"name":"water"}]))
    print(bigger_price_other1(2,[{"price":100,"name":"bread"},{"price":138,"name":"wine"},{"price":15,"name":"meat"},{"price":1,"name":"water"}]))
    # from pprint import pprint
    # print('Example:')
    # pprint(bigger_price(2, [
    #     {"name": "bread", "price": 100},
    #     {"name": "wine", "price": 138},
    #     {"name": "meat", "price": 15},
    #     {"name": "water", "price": 1}
    # ]))
    #
    # # These "asserts" using for self-checking and not for auto-testing
    # assert bigger_price(2, [
    #     {"name": "bread", "price": 100},
    #     {"name": "wine", "price": 138},
    #     {"name": "meat", "price": 15},
    #     {"name": "water", "price": 1}
    # ]) == [
    #     {"name": "wine", "price": 138},
    #     {"name": "bread", "price": 100}
    # ], "First"
    #
    # assert bigger_price(1, [
    #     {"name": "pen", "price": 5},
    #     {"name": "whiteboard", "price": 170}
    # ]) == [{"name": "whiteboard", "price": 170}], "Second"
    #
    # print('Done! Looks like it is fine. Go and check it')
