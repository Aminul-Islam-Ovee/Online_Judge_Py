# calculate the cycle length of a number
def cycle_Length(x):
    count = 1
    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3*x + 1
        count += 1
    return count


# Create a loop for iterating input.
while True:
    try:
        # Receive two inputs and remove white space.
        pairs = input().strip()
        # Convert the string into integer and store them into different variables.
        i, j = map(int, pairs.split())
        max_count = 0
        # Evaluating the condition of input range
        for n in range(min(i, j), max(i, j)+1):
            # print(i, j, i+j)
            count = cycle_Length(n)
            max_count = max(max_count, count)
        print(i, j, max_count)
    except EOFError:
        break
    except ValueError:
        print("Invalid input. Please insert two integer numbers.")
