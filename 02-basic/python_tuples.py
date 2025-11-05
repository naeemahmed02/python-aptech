# -------------------- TUPLES IN PYTHON --------------------
# A tuple is a collection of items that are ordered and unchangeable (immutable).
# Tuples are written using parentheses ()

# Example: Creating a tuple
colors = ('orange', 'yellow', 'green', 'blue', 'violet')

# -------------------- ACCESSING TUPLE ELEMENTS --------------------
# Tuples are also zero-indexed, just like lists.

print(colors[0])  # Prints first element → orange
print(colors[1])  # Prints second element → yellow
print(colors[2])  # Prints third element → green

# -------------------- LENGTH OF A TUPLE --------------------
# Use len() function to find how many items are inside the tuple
tuple_size = len(colors)
print(f"The size of the colors tuple is: {tuple_size}")

# -------------------- TUPLES VS LISTS --------------------
# Tuples are immutable (cannot be changed after creation)
# Lists are mutable (can be changed)

# Example:
fruits_list = ['apple', 'banana', 'cherry']   # List
fruits_tuple = ('apple', 'banana', 'cherry')  # Tuple

# fruits_tuple[0] = 'mango'  # ERROR: Tuples cannot be modified
fruits_list[0] = 'mango'     # Lists can be modified
print("Modified list:", fruits_list)

# -------------------- SINGLE ELEMENT TUPLE --------------------
# You must add a comma after one element to make it a tuple
single_tuple = ('apple',)
print(type(single_tuple))  # <class 'tuple'>

not_a_tuple = ('apple')    # This is just a string, not a tuple
print(type(not_a_tuple))   # <class 'str'>

# -------------------- TUPLE UNPACKING --------------------
# You can unpack (extract) tuple values into variables easily

student = ('Ali', 21, 'BSCS')
name, age, degree = student

print("Name:", name)
print("Age:", age)
print("Degree:", degree)

# -------------------- NESTED TUPLE --------------------
# Tuples can contain other tuples

nested_tuple = ('Fruits', ('apple', 'banana', 'cherry'))
print("Nested tuple:", nested_tuple)
print("Access nested element:", nested_tuple[1][1])  # Access banana

# -------------------- LOOPING THROUGH A TUPLE --------------------
# You can loop through tuple items using a for loop

for color in colors:
    print("Color:", color)

# -------------------- BUILT-IN TUPLE METHODS --------------------
# Tuples have only two main methods: count() and index()

numbers = (1, 2, 3, 4, 2, 5, 2)

# 1 count() → Counts how many times a value appears
count_2 = numbers.count(2)
print("Number of times '2' appears:", count_2)

# 2 index() → Returns the index of the first occurrence of a value
index_4 = numbers.index(4)
print("Index of number 4:", index_4)

# -------------------- BUILT-IN FUNCTIONS THAT WORK ON TUPLES --------------------
# These functions work with tuples just like lists (but tuples cannot be changed)

print("Length of tuple:", len(numbers))      # len() → total elements
print("Maximum value:", max(numbers))        # max() → largest element
print("Minimum value:", min(numbers))        # min() → smallest element
print("Sum of elements:", sum(numbers))      # sum() → adds all numbers
print("Sorted tuple:", sorted(numbers))      # sorted() → returns a sorted list (not tuple)

# -------------------- TUPLE SLICING --------------------
# You can slice tuples just like lists

colors = ('orange', 'yellow', 'green', 'blue', 'violet', 'red')

print(colors[0:3])   # Returns first three elements → ('orange', 'yellow', 'green')
print(colors[2:5])   # Returns elements from index 2 to 4
print(colors[:4])    # Returns elements from start up to index 3
print(colors[3:])    # Returns elements from index 3 to end
print(colors[-2:])   # Returns last two elements
print(colors[::-1])  # Returns reversed tuple

# -------------------- TUPLE CONCATENATION --------------------
# You can combine tuples using the + operator

tuple1 = ('Ali', 'Ahmed')
tuple2 = ('Khan', 'Usman')
combined = tuple1 + tuple2
print("Combined Tuple:", combined)

# -------------------- CHECKING MEMBERSHIP --------------------
# Use 'in' or 'not in' to check if an element exists in a tuple

print('green' in colors)    # True
print('black' not in colors)  # True

# -------------------- SUMMARY --------------------
# Tuple Properties:
# - Ordered
# - Immutable (cannot change)
# - Can contain duplicates
# - Can contain different data types
#
# Common Operations:
# count(), index(), len(), max(), min(), sum(), sorted()
# Slicing [start:end:step], concatenation (+), and membership (in)
