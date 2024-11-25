def write_to_file(filename, content):
    # complete the function
    with open(filename, "w") as file:
        file.write(content)
write_to_file("txt_file.txt", "Hi there ")

def read_from_file(filename):
    # complete the function
    with open(filename, "r") as file:
        content = file.read()
        return content
print(read_from_file("txt_file.txt"))

def append_to_file(filename, content):
    # complete the function
    with open(filename, "a") as file:
        file.write(content)

append_to_file("txt_file.txt", "Appended append")

def remove_file(filename):
   # complete the function
   import os
   os.remove(filename)

remove_file("txt_file.txt")