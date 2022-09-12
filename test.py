def CycleLen(num):
    # Start with one number, the one given.

    curr = num
    count = 1

    # Until you get to 1, increase count and calculate next.

    while curr > 1:
        count += 1
        curr = curr // 2 if curr% 2 == 0 else curr * 3 + 1

    return count

while True:
    # Reads a single line and splits into integers. Any problem, exit loop.

    try:
        inputInt = [int(item) for item in input().split()]
        if len(inputInt) != 2: break
    except:
        break

    # Find value in the range with the longest cycle then print it.

    maxCycle = 0
    for number in range(min(inputInt), max(inputInt) + 1):
        maxCycle = max(maxCycle, CycleLen(number))
    print(inputInt[0], inputInt[1], maxCycle)