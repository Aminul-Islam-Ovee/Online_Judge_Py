import sys
import functools


@functools.lru_cache(None)
def cycle(n):
    count = 1
    while n != 1:
        count += 1
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2
        print(n)

    return count


@functools.lru_cache(None)
def max_cycle(x, y):
    x, y = min(x, y), max(x, y)
    return max(cycle(n) for n in range(x, y + 1))


if __name__ == '__main__':
    for line in sys.stdin:        
        x, y = map(int, line.split()[:2])
        print(x, y, max_cycle(x, y))