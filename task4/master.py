import sys
import os


def min_moves(nums):
    # Find the minimum and maximum elements
    min_num = min(nums)
    max_num = max(nums)

    # Calculate the minimum number of moves
    return max_num - min_num


if __name__ == "__main__":
    # Check if the correct number of arguments are passed
    if len(sys.argv) != 2:
        print("Usage: python master.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"Error: File {file_path} not found.")
        sys.exit(1)

    try:
        # Read numbers from file and store them in a list
        with open(file_path, 'r') as file:
            nums = [int(line.strip()) for line in file]
    except PermissionError:
        # Handle the error if file is not accessible due to permissions
        print(f"Error: Insufficient permissions to read file {file_path}.")
        sys.exit(1)
    except Exception as e:
        # Handle any other exception while reading the file
        print(f"Error: {e}")
        sys.exit(1)

    # Call the function and print the minimum number of moves
    print(min_moves(nums))
