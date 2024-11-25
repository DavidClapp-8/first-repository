def is_prime(num):
    """Checks if a number is prime.

    Input:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:

    boolean = is_prime(5)   # returns True
    print(boolean)
    """
    # Function implementation here ...
    check = False

    for i in range(2, num):
        if num % i == 0:
            check = True
            break
    if num == 1 or num == 0:
        check = True
    if check:
        output = False
    else:
        output = True
    return output


# # # Run code example
print(is_prime(7))   # returns True
  