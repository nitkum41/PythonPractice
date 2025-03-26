def find_missing_numbers(arr, n):
    """
    Finds and prints missing numbers in a natural number series.

    Args:
        arr: A list/array of integers representing the series.
        n: The expected length of the complete natural number series.
    """
    # Create a set for efficient lookup of present numbers.
    present_numbers = set(arr)

    # Iterate through the expected numbers and check for missing ones.
    for i in range(1, n + 1):
        if i not in present_numbers:
            print(i, end=" ")  # Print missing numbers separated by spaces
    print()  # Add a newline for better readability

# Example usage:
arr = [1, 2, 4, 7]
n = len(arr) + 2  # Calculate expected length (n=4, so expected length is 6)
find_missing_numbers(arr, n)  # Output: 3 5