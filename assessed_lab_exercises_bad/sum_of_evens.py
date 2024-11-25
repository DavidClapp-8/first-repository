def sum_of_evens(min_value, max_value):
    
    """Find the sum of even numbers between two given numbers (inclusive).

    Args:
        min_value (int): Minimum number
        max_value (int): Maximum number

    Returns:
        total: sum of the even numbers between min_value and max_value

    Example:

    min_value = 10
    max_value = 13
    total = sum_of_evens(min_value, max_value)
    print(total) # total is 22.

    """



    # Function implementation here ...
    flag = False
    total = 0
    if type(min_value) != int or type(max_value) != int:
        flag = True
        total = "Incorrect input"
        


    if flag == False:
        for i in range(max_value + 1):
            print(i)
            if i % 2 == 0:
                total += i

    
    return total

# # # Run code example
min_value = 1
max_value = 10
print(sum_of_evens(min_value, max_value)) # returns 22

