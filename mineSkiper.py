data =[]

def display(data):
    for index, lists in enumerate(data):
        print("\nField #{}".format(index+1))
        for cols in lists:
            print (''.join(str(i) for i in cols))

def updateField(field,rs,rb,cs,cb):
    for i in range(rs, rb+1):
        for j in range(cs,cb+1):
            if field[i][j] != "*":
                field[i][j]+=1
    
    return field

def solveMine(fld):
    field = fld.copy()
    for x,r in enumerate(fld):
        for y,c in enumerate(r):
            if c =="*":
                rowMin= x - 1 if x > 0 else x
                rowMax= x + 1 if x < len(fld)-1 else x
                colMin= y - 1 if y > 0 else y
                colMax= y + 1 if y < len(r)-1 else y
                field = updateField(field,rowMin,rowMax,colMin,colMax)
    return field

def splitInput(data):
    for i,lists in enumerate(data):
        data[i]= solveMine(lists)
    display(data)

def replaceDots(data):
    for lists in data:
        for col in lists:
            for i,value in enumerate(col):
                if value ==".":
                    col[i]=int(0)
    splitInput(data)

while 1 == 1:
    try:
        cols =[]
        n, m = map(int, input().split())
        if m == 0 or n == 0:
            break
        else:
            for i in range(n):
                while 2 == 2:
                    inp = input()
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

replaceDots(data)
