#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    # Exclude the script name and convert each argument to an integer
    args_as_int = [int(arg) for arg in argv[1:]]

    # Calculate the sum of all integers in the arguments
    result = sum(args_as_int)

    # Print the result followed by a new line
    print(result)
