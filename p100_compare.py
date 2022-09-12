
call = True
inp = []
#receive input with looping
while call == True:
    pair = []
    try:
        x,y = input().split()
        x=int(x)
        y=int(y)
        if 0<x<100000 and 0<y<1000000:
            pair.append(x)
            pair.append(y)
            inp.append(pair)
            pair=[]
        else:
            print("Invalid input")
    except:
        break
    
#calculate cycle
def calculate(list):
    final =[]
    result =[]
    cycle = []
    maxCycle = 0

    for pairs in list:
        for data in pairs:
            result.append(data)
            while data > 0 and data != 1:
                cycle.append(data)
                if data % 2 == 0:
                    data /= 2 
                else:
                    data = (data*3) + 1
            #Calculate the cycle length and update
            if maxCycle < len(cycle) + 1:
                maxCycle = len(cycle) + 1
            #empty the cycle for another input
            #print("Cycle:",cycle)
            cycle = []
        result.append(maxCycle)
        maxCycle = 0
        final.append(result)
        result =[]
        
    return final

if inp == []:
    print("No data found. Try again.")
else:
    # print("Input : ", inp)
    output = calculate(inp)
    for x in range(len(output)):
        print(*output[x]) 