# -------------------- DICTIONARIES IN PYTHON --------------------
# A dictionary is a collection of key-value pairs.
# Each key must be unique and immutable (e.g., strings, numbers, tuples).
# Dictionaries are written using curly braces {}.

# Example: Creating a dictionary
student = {
    'name': 'Ali',
    'age': 21,
    'degree': 'BSCS',
    'city': 'Karachi'
}

# -------------------- ACCESSING DICTIONARY ELEMENTS --------------------
# You can access dictionary values using their keys.

print(student['name'])     # Access using key → Ali
print(student.get('age'))  # Access safely using get() → 21

# If key does not exist:
print(student.get('roll_no'))  # Returns None (instead of error)

# -------------------- MODIFYING DICTIONARY ELEMENTS --------------------
# You can add or update key-value pairs.

student['age'] = 22           # Update existing key
student['university'] = 'FAST'  # Add new key-value pair
print("Updated dictionary:", student)

# -------------------- REMOVING ELEMENTS --------------------
# 1 pop() → Removes a specific key and returns its value
removed_value = student.pop('city')
print("Removed city:", removed_value)
print("After pop:", student)

# 2 popitem() → Removes the last inserted key-value pair
student.popitem()
print("After popitem:", student)

# 3 del → Deletes a specific key or entire dictionary
del student['degree']     # Delete specific key
print("After del key:", student)

# 4 clear() → Removes all elements from dictionary
# student.clear()
# print("After clear:", student)

# -------------------- LOOPING THROUGH DICTIONARY --------------------
# You can loop through keys, values, or both.

student = {'name': 'Ali', 'age': 22, 'degree': 'BSCS', 'university': 'FAST'}

# Loop through keys
for key in student:
    print("Key:", key)

# Loop through values
for value in student.values():
    print("Value:", value)

# Loop through both keys and values
for key, value in student.items():
    print(f"{key} → {value}")

# -------------------- CHECKING MEMBERSHIP --------------------
# Check if a key exists in a dictionary
print('name' in student)   # True
print('roll_no' not in student)  # True

# -------------------- NESTED DICTIONARIES --------------------
# A dictionary can contain another dictionary

students = {
    'student1': {'name': 'Ali', 'age': 21},
    'student2': {'name': 'Ahsan', 'age': 22},
    'student3': {'name': 'Ahmed', 'age': 20}
}

print("Nested Dictionary:", students)
print("Access nested element:", students['student2']['name'])  # Ahsan

# -------------------- BUILT-IN DICTIONARY METHODS --------------------
# Let’s explore commonly used dictionary methods

info = {'name': 'Faheem', 'age': 23, 'city': 'Lahore'}

# 1 keys() → Returns all keys
print("Keys:", info.keys())

# 2 values() → Returns all values
print("Values:", info.values())

# 3 items() → Returns all key-value pairs
print("Items:", info.items())

# 4 get() → Returns value for key (returns None if key not found)
print("Get 'name':", info.get('name'))
print("Get 'roll_no':", info.get('roll_no', 'Not Found'))

# 5 pop() → Removes key and returns its value
info.pop('age')
print("After pop:", info)

# 6 popitem() → Removes last inserted pair
info.popitem()
print("After popitem:", info)

# 7 update() → Adds or updates multiple key-value pairs
info.update({'country': 'Pakistan', 'age': 24})
print("After update:", info)

# 8 clear() → Removes all items
# info.clear()

# 9 copy() → Returns a shallow copy of the dictionary
copy_dict = info.copy()
print("Copied dictionary:", copy_dict)

# -------------------- BUILT-IN FUNCTIONS THAT WORK ON DICTIONARIES --------------------
student = {'Ali': 21, 'Faheem': 23, 'Naeem': 25}

# 1 len() → Total number of key-value pairs
print("Length:", len(student))

# 2 sorted() → Returns sorted list of keys
print("Sorted keys:", sorted(student))

# 3 any() → Returns True if at least one key is True (non-empty)
print("Any:", any(student))

# 4 all() → Returns True if all keys are True
print("All:", all(student))

# 5 str() → Converts dictionary into string
print("String representation:", str(student))

# -------------------- COPYING AND MERGING DICTIONARIES --------------------
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge two dictionaries using update()
dict1.update(dict2)
print("Merged dictionary (update):", dict1)

# Merge (Python 3.9+): Using '|' operator
merged = {'x': 10, 'y': 20} | {'y': 30, 'z': 40}
print("Merged using | :", merged)

# -------------------- DICTIONARY COMPREHENSION --------------------
# Similar to list comprehension, but for key-value pairs

squares = {x: x**2 for x in range(1, 6)}
print("Squares dictionary:", squares)

# -------------------- SUMMARY --------------------
# Dictionary Properties:
# - Unordered (in older versions), Key-Value pairs
# - Mutable (can change)
# - Keys must be unique and immutable
# - Values can be of any type

# Common Methods:
# get(), keys(), values(), items(), pop(), popitem(), update(), clear(), copy()

# Common Functions:
# len(), sorted(), any(), all(), str()

# Advanced:
# - Nested dictionaries
# - Merging with update() or |
# - Dictionary comprehension
