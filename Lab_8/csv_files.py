import csv

def create_csv(filename, data):
  with open(filename, "w") as file:
     if type(data) == str:
       file.write(data)
     if type(data) == list:
        writer = csv.writer(file)
        writer.writerows(data)

def read_csv(filename):
   with open(filename, "r") as file:
    read_data = file.read()
    return read_data
   
def append_to_csv(filename, append):
   with open(filename, "a") as file:
    if type(append) == str:
        file.write(append)
    if  type(append) == list:
        writer = csv.writer(file)
        writer.writerow(append)

filename = "csv_file.csv"
data = [['Name', ' Age',' Grade'],
        ['Alice', 23, ' A'],
        ['Bob', 22, ' B'],
        ['Charlie', 24, ' A'],
        ['David', 22, ' C'],
        ['Eva', 23, ' B']]
append = ['Tom', 25, ' A']

create_csv(filename, data)

print(read_csv(filename))

append_to_csv(filename, append)