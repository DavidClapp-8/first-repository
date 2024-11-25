def letter_occurrence(input_string):
    # complete function implementation...
    count = 0
    for i in (input_string):
        if i == "a" or i == "A":
            count +=1
    return count
print(letter_occurrence("Always aim ambitiously"))