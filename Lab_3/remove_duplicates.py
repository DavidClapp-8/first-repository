def remove_duplicates(numbers):
    """
    Removes duplicates from a list of numbers and returns a new list with unique elements.

    Parameters:
    ----------
    numbers : list
        A list of numbers which may contain duplicate values.

    Returns:
    -------
    list
        A new list with duplicate values removed.
    
    Example:
    --------
    remove_duplicates([1, 2, 2, 3, 4, 4, 5])  # Output: [1, 2, 3, 4, 5]
    """
    # Hint: Convert the list to a set to remove duplicates, then convert it back to a list
    # List --> Set (remove duplicates) --> List (return the list)
    # Write your code here...
    my_set = set(numbers)
    unique_numbers = list(my_set)

    return unique_numbers
my_list = [1,2,3,4,5,1,2,12.5,12.5]
print(my_list)
answer = remove_duplicates(my_list)
print(answer)