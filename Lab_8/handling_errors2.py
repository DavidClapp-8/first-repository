
def select_menu_option():
    while True:
        try:
            option = int(input("Select an option (1, 2, or 3): "))
            if option in [1, 2, 3]:
                print(f"You have selected option {option}.")
                break
            else:
                print("Invalid option. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

select_menu_option()


def read_file_content(filename):
    with open(filename, 'r') as file:
        content = file.read()
    print(content)

# Example usage
read_file_content('nonexistent_file.txt')




def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"The result is {result}")
    except:
        ZeroDivisionError
# Example usage
divide_numbers(10, 0)




def get_number():
    number = float(input("Enter a number: "))
    return number

get_number()