import sys
from bisect import bisect_right

MAX_N = 100000
LOG_MAX = 18

def main():
    n = int(input())
    destinations = [0] + list(map(int, input().split()))
    rangeLimit = int(input())
    queries = int(input())
    jump = [[0] * LOG_MAX for _ in range(MAX_N + 1)]
    maxReach = [0] * (n + 1)

    for startPos in range(1, n + 1):
        maxReach[startPos] = bisect_right(destinations, destinations[startPos] + rangeLimit) - 1
        jump[startPos][0] = maxReach[startPos]

    for power in range(1, LOG_MAX):
        for pos in range(1, n + 1):
            jump[pos][power] = jump[jump[pos][power - 1]][power - 1]

    for _ in range(queries):
        from_, to = map(int, input().split())
        if from_ > to:
            from_, to = to, from_

        daysNeeded = 0
        for power in range(LOG_MAX - 1, -1, -1):
            if jump[from_][power] < to:
                from_ = jump[from_][power]
                daysNeeded += (1 << power)
        print(daysNeeded + 1)

sys.setrecursionlimit(10 ** 6)
main()