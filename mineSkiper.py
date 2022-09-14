data =[]
field =[]

def display(data):
    for index, lists in enumerate(data):
        print("\nField #{}".format(index+1))
        for cols in lists:
            print (''.join(cols))

def updateField(x,y):
    rowMin = x - 1
    rowMax = x + 1
    colMin = y - 1
    colMax = y + 1


def solveMine(field):
    for i,c in enumerate(field):
        for j,r in enumerate(c):
            if r =="*":
                updateField(i,j)


def splitInput(data):
    for lists in (data):
        solvedList= solveMine(lists)

while 1 == 1:
    try:
        cols =[]
        n, m = map(int, input().split())
        if m == 0 or n == 0:
            break
        else:
            for i in range(n):
                while 2 == 2:
                    inp = str(input())
                    rows =[]
                    if len(inp) == m:
                        rows.extend(inp)
                        cols.append(rows)
                        break
                    else:
                        print("Wrong input.")
                
            data.append(cols)
    except:
        print("Please enter a number or (0 0) to exit")

splitInput(data)
