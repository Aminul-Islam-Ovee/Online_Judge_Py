def maxCycle(x,y):
    maxCount = 0
    mn, mx = min(x,y), max(x,y)
    for i in range(mn, mx+1):
        count = 1
        while i != 1:
            if i % 2 == 0:
                i/=2
            else:
                i = 3*i+1
            count += 1
        if count > maxCount:
            maxCount = count
    return maxCount

while 1 == 1:
    try: 
        x, y = map(int, input().split())
        if 0<x<10000 and 0<y<10000:
            print(x, y, maxCycle(x,y))
        else:
            print("Invalid Input. Try again")
    except:
        break