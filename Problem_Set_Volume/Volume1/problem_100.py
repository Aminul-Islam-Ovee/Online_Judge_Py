# Create a loop for iterating input.
while True:
    try:
        # Receive two inputs and remove white space.
        pairs = input().strip()
        # Convert the string into integer and store them into different variables.
        i, j = map(int, pairs.split())

        # Evaluating the condition of input range
        if 0 < i < 1000000 and 0 < j < 1000000:

            print(i, j, i+j)
        else:
            print("Please enter two numbers between 0 and 1000000")

    except EOFError:
        break

    except ValueError:
        print("Invalid input. Please insert two integer numbers.")
