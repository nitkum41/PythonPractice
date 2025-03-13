def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        # Swap elements at start and end indices
        arr[start], arr[end] = arr[end], arr[start]
        # Move start pointer to the right and end pointer to the left
        start, end = start + 1, end - 1

# Example usage:
array_list = [12.55, 15, 6.6, 0.4, 52.5, 55.5,70]
reverse_array(array_list)
print("Reversed array:", array_list)