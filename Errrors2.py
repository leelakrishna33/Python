
# NameError: Undefined variable
message = "Python is fun!"
print(msg)

# TypeError: Concatenating string and integer
age = 25
print("I am " + age + " years old")

# ValueError: Converting invalid string to int
invalid_number = "abc"
number = int(invalid_number)

# IndexError: Accessing index out of range
numbers = [1, 2, 3]
print(numbers[4])

# FileNotFoundError: Opening a non-existent file
file_path = "nonexistent.txt"
with open(file_path, 'r') as file:
    content = file.read()