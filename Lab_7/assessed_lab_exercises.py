def calculator(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
        print(f"The result is: {result}")
    elif operator == "-":
        result = num1 - num2

    # Function implementation here ...
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = "Zero division error"
    
    elif operator == "%":
        try:
            result = num1 % num2
        except ZeroDivisionError:
            result = "Zero division error"

    elif operator == ">":
        if num1 > num2:
            result = True
        else:
            result = False

    elif operator == ">=":
        if num1 >= num2:
            result = True
        else:
            result = False

    elif operator == "<":
        if num1 < num2:
            result = True
        else:
            result = False

    elif operator == "<=":
        if num1 <= num2:
            result = True
        else:
            result = False
    else:
        result = "Invalid Operator."
    return result

def max_of_three(num1, num2, num3):
    """
    This function takes three integers as input and returns the maximum of the three given numbers.

    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.
    num3 (int): The third number.

    Returns:
    int: The maximum of the three numbers.
    """
    # Hint: you are required to make use of maximum variable that is returned by the function below.
    # Complete your code implementation here...
    maximum = max(num1, num2, num3)
    return maximum

def winning_numbers(user_list, winning_list):
    # Function implementation here ...
    a = set(user_list)
    user_list = list(a)
    score = 0
    if user_list[0] in winning_list:
        print(f"Index 1 is in")
        score += 1

    if user_list[1] in winning_list:
        print(f"Index 1 is in")
        score += 1

    if user_list[2] in winning_list:
        print(f"Index 3 is in")
        score += 1

    if score == 3:
        prize = "First"
    elif score == 2:
        prize = "Second"
    elif score == 1:
        prize = "Third"
    else:
        prize = "No"
        
 
    return prize

def sum_of_evens(min_value, max_value):
    # Function implementation here ...
    flag = False
    total = 0
    if type(min_value) != int or type(max_value) != int:
        flag = True
        total = "Incorrect input"
        

    if flag == False:
        for i in range(min_value, max_value + 1):
            if i % 2 == 0:
                total += i
    return total

def are_anagrams(str1, str2):
    # Function implementation here ...
    flag = False
    if type(str1) != str or type(str2) != str:
        flag = True
        total = "Incorrect input"
    if flag == False:
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

def is_prime(num):
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

def calculate_average(numbers):
    
    # Function implementation here ...
    nums = 0
    for i in numbers:
        nums += i
        print(nums)
    average = nums / len(numbers)


    return average

def calculate_weekly_pay(hours_worked):
    regular_rate = 12  # £12 per hour for up to 35 hours
    overtime_rate = 18  # £18 per hour for hours worked beyond 35 hours
    standard_hours = 35  # Threshold for regular pay



    # Function implementation here ...
    if hours_worked <= standard_hours:
        total_pay = hours_worked * regular_rate

    elif hours_worked >= standard_hours:
        over_worked = hours_worked - 35
        over_pay = over_worked * overtime_rate
        normal_pay = 35 * regular_rate
        total_pay = over_pay + normal_pay

    return total_pay

def celsius_to_fahrenheit(celsius):
   # complete your function implementation... 
   output = celsius * (9/5) + 32
   return output

def annual_net_income(gross_salary):
    # complete your function implementation here...
    if gross_salary >= 45000:
        tax_rate = 0.5
    elif gross_salary >= 30000 and gross_salary < 45000:
        tax_rate = 0.3
    elif gross_salary < 30000:
        tax_rate = 0.15
    
    net_salary = gross_salary - (gross_salary * tax_rate)

    return net_salary

def letter_occurrence(input_string):
    # complete function implementation...
    count = 0
    for i in (input_string):
        if i == "a" or i == "A":
            count +=1
    return count

def km_to_miles(kilometers):
    # complete function implementation here...
    miles = kilometers * 0.62
    rounded_miles = round(miles, 3)
    return rounded_miles

def fuel_cost(distance_miles):
    # Constants
    MPG = 50  # Miles per gallon
    LITERS_PER_GALLON = 4.5
    PRICE_PER_LITER = 1.49  # Price in pounds per liter
#     continue function implementation here...
    #How many gallons of fuel used
    gallons = distance_miles / MPG  
    #How many litres of fuel used 
    litres = gallons * LITERS_PER_GALLON
    #Price of litres of fuel used
    total_cost = litres * PRICE_PER_LITER   
    return total_cost

def decrypt_cypher_text(encrypted_text, key):
    #function implementation here...
    decrypted_text = ""
    for i in encrypted_text:
        encrypted_text_ord = ord(i)
        diff = encrypted_text_ord - key
        remainder = diff % 256
        decrypted_text += (chr(remainder))

    return decrypted_text

def is_golden_number(n):
#   function implementation ...
    boolean = False
    for i in range(n):
        for k in range(n):
            if i + k == n:
                if i*k % 1000 == 0:
                    boolean = True
                    print(f"K: {k}")
                    print(f"i: {i}")
                    break
    return boolean

def find_maximum_difference(a, b):
#   #code implementation here...
    maximum = 0
    for i in a:
        for k in b:
            diff = i - k
            diff_2 = k - i
            #print(diff)
            ##=print(diff_2)
            diff_3 = max(diff, diff_2)
            print(F"DIFF_3: {diff_3}")
            if maximum <= diff_3:
                maximum = diff_3    
            print(f"MAX: {maximum}")
    
    
    return maximum