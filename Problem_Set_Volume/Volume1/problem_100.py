# Memoization dictionary to store the cycle length for each number. With memoization, the cycle length for a number is calculated only once, and subsequent occurrences of the number use the stored result. This greatly reduces the number of computations, especially for large ranges of numbers
memo = {}

# Calculate the cycle length of a number, using memoization


def cycle_length(x):
    original_x = x
    count = 1
    while x != 1:
        if x in memo:
            # If the cycle length of x is already calculated, use the memoized value
            count += memo[x] - 1
            break
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        count += 1
    # Store the cycle length in the memo dictionary
    memo[original_x] = count
    return count


# Create a loop for iterating input.
while True:
    try:
        # Prompt user for input
        pairs = input().strip()

        # Convert the string into integer and store them into different variables
        i, j = map(int, pairs.split())

        max_count = 0
        # Evaluating the condition of input range
        for n in range(min(i, j), max(i, j) + 1):
            count = cycle_length(n)
            max_count = max(max_count, count)

        # Output the results
        print(i, j, max_count)

    except EOFError:
        # Break the loop when EOF (Ctrl+D) is encountered
        break

    except ValueError:
        # Handle invalid input
        print("Invalid input. Please insert two integer numbers.")
