'''
格式化时间
46800999
13:00:00
1618708103123
01:08:23
'''


n = int(input()) // 1000


def add_zero(time):
    if time < 10:
        time = '0' + str(time)
        return time
    return str(time)


# 因为有可能是很大的数字，并不是单纯的一天的时间，取个余就完了，最后转换到一天的时间里面就可以计算了
def format_time(time):
    if time > 365 * 24 * 3600:
        time = time % 365 * 24 * 3600
    if time > 24 * 3600:
        time = time % 24 * 3600
    hh = time // 3600
    mm = (time - hh * 3600) // 60
    ss = time - hh * 3600 - mm * 60
    h = add_zero(hh)
    m = add_zero(mm)
    s = add_zero(ss)

    time_format = h + ':' + m + ':' + s
    return time_format


print(format_time(n))
