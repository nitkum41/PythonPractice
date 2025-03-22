def find_missing_number(arr):
    """
    Finds the missing number in a natural number series.

    Args:
        arr: A list of natural numbers (1, 2, 3, ...).

    Returns:
        The missing number, or None if no missing number is found.
    """

    n = len(arr) + 1  # Calculate the expected length of the complete series
    expected_sum = (n * (n + 1)) // 2  # Use the formula for the sum of natural numbers
    actual_sum = sum(arr)

    missing_number = expected_sum - actual_sum

    if missing_number > 0 and missing_number <= n:
        return missing_number
    else:
        return None # Or raise an exception if you prefer

# Example usage
arr = [1, 2, 3, 5, 7]
missing = find_missing_number(arr)

if missing is not None:
    print(f"The missing number is: {missing}")
else:
    print("No missing number found or input is invalid")