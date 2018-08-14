#coding:utf8
def sun_angle(time):
    import time as nowtime
    #replace this for solution
    starttime= nowtime.strftime("%Y-%m-%d", nowtime.localtime())+" "+"06:00"
    endtime= nowtime.strftime("%Y-%m-%d", nowtime.localtime())+" "+"18:00"

    strtime = nowtime.strftime("%Y-%m-%d", nowtime.localtime())+" "+time

    numtime  = nowtime.mktime(nowtime.strptime(strtime,"%Y-%m-%d %H:%M"))
    numtimestart  = nowtime.mktime(nowtime.strptime(starttime,"%Y-%m-%d %H:%M"))
    numtimeend  = nowtime.mktime(nowtime.strptime(endtime,"%Y-%m-%d %H:%M"))

    if(numtimeend <numtime or numtime<numtimestart):
        return "I don't see the sun!"
    else:
        return (numtime-numtimestart)/60*0.25

def sun_angle_other(time):
    hh, mm = int(time[:2]), int(time[3:])
    hhmm = int(time.replace(':', ''))
    if not 600 <= hhmm <= 1800:
        return "I don't see the sun!"
    else:
        return ((hh - 6) * 60 + mm) * 0.25
if __name__ == '__main__':
    print sun_angle("02:00")
    print sun_angle_other("02:00")
    # print("Example:")
    # print(sun_angle("07:00"))
    #
    # #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert sun_angle("07:00") == 15
    # assert sun_angle("01:23") == "I don't see the sun!"
