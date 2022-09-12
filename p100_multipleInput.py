list = []
while 1 == 1:
    subList = []
    try:
        x,y = map(int, input().split())
        subList.append(x)
        subList.append(y)
        list.append(subList)
    except:
        break

def Cycle(inp1, inp2):
    maxCount = 0
    mn, mx = min(inp1, inp2), max(inp1, inp2)
    for x in range(mn, mx+1):
        count = 1
        while x != 1:
            if x % 2 == 0:
                x/=2
            else:
                x = 3*x+1
            count +=1
        if count > maxCount:
            maxCount = count
    return maxCount

for pair in list:
    inp1, inp2 = pair
    if 0<inp1<10000 and 0<inp2<10000:
        x = Cycle(inp1, inp2)
        print (inp1, inp2, x)
    else:
        print(inp1, inp2, "Invalid input")
        

