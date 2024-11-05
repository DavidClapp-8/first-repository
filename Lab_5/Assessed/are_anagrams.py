def are_anagrams(str1, str2):
    """
    This function checks if two strings are anagrams of each other.

    Parameters:
    ----------
    str1 : str
        The first string to be compared.
    str2 : str
        The second string to be compared.

    Returns:
    -------
    bool:
        Returns True if the two strings are anagrams, otherwise False.

    Example:
    --------
    are_anagrams("listen", "silent")  # Output: True
    are_anagrams("hello", "world")    # Output: False
    """

    # Function implementation here ...
    list_1 = list(str1)
    list_2 = list(str2)
    del_1 = list(str1)
    del_2 = list(str2)
    for x in list_1:
        for y in list_2:
            if x == y:
                try:
                    del_1.remove(x)
                    del_2.remove(y)
                except ValueError:
                    continue
            else:
                continue

    if del_1 == del_2:
        result = True
    else:
        result = False

    return result
## Example 
print(are_anagrams("listen", "silent"))  # Expected output: True
print(are_anagrams("hello", "world"))    # Expected output: False
