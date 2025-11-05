# -------------------- LISTS IN PYTHON --------------------
# A list is a collection of items that are ordered, changeable, and allow duplicate values.
# Lists are written using square brackets [].

# Example: Creating a list
colors = ['orange', 'yellow', 'green', 'blue', 'violet']

# -------------------- ACCESSING LIST ELEMENTS --------------------
# Lists are zero-indexed. The first element has index 0.

print(colors[0])  # Prints the first element → orange
print(colors[1])  # Prints the second element → yellow
print(colors[2])  # Prints the third element → green

# -------------------- LENGTH OF A LIST --------------------
# Use len() function to find the number of items in a list
list_size = len(colors)
print(f"The size of the colors list is: {list_size}")

# -------------------- BUILT-IN LIST METHODS --------------------
# Let's create two lists

students_names = ['Naeem', 'Faheem', 'Nadeem', 'Mujeeb', 'Najeeb']
student_father_names = ['Abdul Rehman', 'Raheem Khan', 'Muhammad', 'Ali', 'Sikander']

# 1 append() → Adds an element to the end of the list
students_names.append('Abu Bakar')
student_father_names.append('Usman')
print("After append:", students_names)

# 2 insert() → Adds an element at a specific position (index)
students_names.insert(0, 'Najeebullah')  # Add at index 0
students_names.insert(0, 'Waheed Ali')   # Add another element at the beginning
print("After insert:", students_names)

# 3 extend() → Combines two lists
students_names.extend(student_father_names)
print("After extend:", students_names)

# 4 index() → Returns the index of a specific element
abu_bakar_index = students_names.index('Abu Bakar')
print(f"Index of 'Abu Bakar': {abu_bakar_index}")

# 5 remove() → Removes a specific element
students_names.remove('Abu Bakar')
print("After remove:", students_names)

# 6 sort() → Sorts the list alphabetically (ascending order)
students_names.sort()
print("Sorted list:", students_names)

# 7 reverse() → Reverses the list order
students_names.reverse()
print("Reversed list:", students_names)

# 8 pop() → Removes and returns an element at the given index
removed_item = students_names.pop(0)  # Removes first element
print(f"Removed '{removed_item}' using pop():", students_names)

# -------------------- BUILT-IN LIST FUNCTIONS --------------------
# These are Python functions that can work with lists (not methods)

# 1 len() → Returns total number of elements in a list
print("Length of list:", len(students_names))

# 2 max() → Returns the maximum element (alphabetically for strings)
print("Maximum (alphabetically):", max(students_names))

# 3 min() → Returns the minimum element
print("Minimum (alphabetically):", min(students_names))

# 4 sum() → Works only for numeric lists
numbers = [10, 20, 30, 40, 50]
print("Sum of numbers:", sum(numbers))

# 5 sorted() → Returns a new sorted list (without changing the original)
unsorted_list = ['b', 'a', 'd', 'c']
sorted_list = sorted(unsorted_list)
print("Original:", unsorted_list)
print("Sorted:", sorted_list)

# -------------------- LIST SLICING --------------------
# Slicing is used to access a range of elements in a list

colors = ['orange', 'yellow', 'green', 'blue', 'violet', 'red']

print(colors[0:3])   # Returns first three elements → ['orange', 'yellow', 'green']
print(colors[2:5])   # Returns elements from index 2 to 4
print(colors[:4])    # Returns elements from start up to index 3
print(colors[3:])    # Returns elements from index 3 to the end
print(colors[-2:])   # Returns last two elements
print(colors[::-1])  # Returns the list in reverse order (slicing trick)

# -------------------- SUMMARY --------------------
# append() → Add single item at end
# extend() → Add multiple items from another list
# insert() → Add item at a specific index
# remove() → Delete a specific item
# pop() → Delete item at index (default last)
# sort() → Sort list ascending
# reverse() → Reverse the list
# index() → Find position of an item
# len(), max(), min(), sum(), sorted() → Built-in functions for lists
# slicing [start:end:step] → Extracts parts of a list
