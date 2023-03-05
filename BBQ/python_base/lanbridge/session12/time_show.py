'''
格式化时间
'''


n = int(input())


def add_zero(time):
    if time < 10:
        time = '0' + str(time)
        return time
    return str(time)


# 因为有可能是很大的数字，并不是单纯的一天的时间，取个余就完了
def format_time(time):
    time = time % (365 * 24 * 60 * 60)
    if time > 24 * 3600000:
        time = time % (24 * 3600000)
    print(time)
    time_s = time // 1
    hh = time_s // 3600 % 24
    mm = (time_s // 60 - time_s // 3600 * 60) % 60
    ss = (time_s - time_s // 3600 * 3600) % 60
    h = add_zero(hh)
    m = add_zero(mm)
    s = add_zero(ss)

    time_format = h + ':' + m + ':' + s
    return time_format


print(format_time(n))
