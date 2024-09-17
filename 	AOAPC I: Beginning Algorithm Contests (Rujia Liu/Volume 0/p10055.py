while True:
    try:
        # Get input from the terminal and split it into two numbers
        line = input().strip()
        hashmat, opponent = map(int, line.split())

        # Print the absolute difference between the two armies
        print(abs(hashmat - opponent))

    except EOFError:
        # Stop input on End of File (Ctrl+D in terminal)
        break

    except ValueError:
        # Handle invalid input that can't be split into two integers
        print("Invalid input. Please enter two numbers.")
