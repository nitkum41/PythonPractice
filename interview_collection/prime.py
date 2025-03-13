def prime_checker(num):
    # Return False for non-prime cases
    if num <= 1:
        return False
    # Return True for prime numbers 2 and 3
    elif num <= 3:
        return True
    # Eliminate even numbers greater than 2 and multiples of 3
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        # Check from 5 up to the square root of num
        """
        If 'num' is divisible by any number larger than its square root, 
        it must also be divisible by some number smaller than its square root
        or 
        use 6n ± 1 method for a more optimized approach.
        """
        for i in range(5, int(num**0.5) + 1, 2):  # Only check odd numbers
            if num % i == 0:
                return False
        return True

# Example usage:
num_to_check = 30
print(f"Is {num_to_check} a prime number? {prime_checker(num_to_check)}")