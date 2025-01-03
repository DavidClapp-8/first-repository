def winning_numbers(user_list, winning_list):
    """
    This function checks if the user's numbers match the predefined winning numbers.

    Parameters:
    user_list (list): A list of three integers representing the user's chosen numbers.
    winning_list (list): A list of integers representing the winning numbers.

    Returns:
    str: A string indicating the prize won:
        - "First" if all three numbers match the winning numbers.
        - "Second" if two numbers match the winning numbers.
        - "Third" if one number matches the winning numbers.
        - "No" if none of the numbers match the winning numbers.

    Example:
    --------
    winning_list = [5, 14, 17]
    user_list = [3, 5, 10]
    result = winning_numbers(user_list, winning_list)
    # Output: "Third" (since one number, 5, matches the winning numbers)

    user_list = [14, 5, 10]
    result = winning_numbers(user_list, winning_list)
    # Output: "Third" (since two numbers, 14 and 5, match the winning numbers)

    The function also prints a message indicating the prize won.
    """

    # Function implementation here ...
    x = 0
    score = 0
    for i in range (3):
        if user_list[x] in winning_list:
            print(f"X is {x}")
            score += 1
        #print(f"Score is {score}")
        x += 1
    if score == 3:
        prize = "First"
    elif score == 2:
        prize = "Second"
    elif score == 1:
        prize = "Third"
    else:
        prize = "No"
        
    print(prize)

    # Print the result
    print(f"Congratulations, you won {prize} prize!")
    return prize



user_list = [21, 25, 56]
winning_list = [1, 2, 3]
winning_numbers(user_list, winning_list)

#Dont upload this one!!!!!!!!