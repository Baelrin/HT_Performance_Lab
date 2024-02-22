import sys


def circular_path(n, m):
    # Creating a circular array
    circular_array = [i % n + 1 for i in range(n)]

    # Forming the path
    path = []
    for i in range(n):
        # Defining the interval, considering transitions across the start of the array
        interval = circular_array[i:] + circular_array[:i]
        interval = interval[:m]
        # Adding the first element of the interval to the path
        path.append(str(interval[0]))

    return ''.join(path)


# Checking the number of arguments
if len(sys.argv) != 3:
    print("Usage: python master.py <n> <m>")
    sys.exit(1)

# Retrieving parameters from the command line
try:
    n, m = map(int, sys.argv[1:])
except ValueError:
    print("Error: Both <n> and <m> must be integers.")
    sys.exit(1)

# Outputting the path
print(circular_path(n, m))
