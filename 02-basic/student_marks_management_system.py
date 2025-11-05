# -------------------- STUDENT MARKS MANAGEMENT SYSTEM --------------------

# A program to store student marks by roll number using dictionary

print("🎓 Welcome to the Student Marks Management System 🎓")
print("-" * 55)

# Dictionary to store data: {roll_number: [marks]}
students_data = {}

# Ask how many students you want to add
num_students = int(input("Enter total number of students: "))

# -------------------- INPUT SECTION --------------------
for i in range(num_students):
    print(f"\nEntering data for Student {i+1}")
    roll_no = input("Enter Roll Number: ")

    # Ask how many subjects
    num_subjects = int(input("Enter number of subjects: "))

    marks = []  # list to store subject marks
    for j in range(num_subjects):
        mark = float(input(f"Enter marks for subject {j+1}: "))
        marks.append(mark)

    # Store in dictionary
    students_data[roll_no] = marks

print("\nData entry completed successfully!\n")

# -------------------- DISPLAY SECTION --------------------
print("All Student Records:")
print("-" * 55)
for roll, marks in students_data.items():
    print(f"Roll No: {roll} → Marks: {marks}")

# -------------------- OPERATIONS SECTION --------------------

# 1 Calculate total and average marks for each student
print("\n📊 Student Performance Summary:")
for roll, marks in students_data.items():
    total = sum(marks)
    avg = total / len(marks)
    print(f"Roll No: {roll} | Total: {total} | Average: {avg:.2f}")

# 2 Find the student with the highest total marks
highest_total = 0
topper_roll = None

for roll, marks in students_data.items():
    total = sum(marks)
    if total > highest_total:
        highest_total = total
        topper_roll = roll

print(f"\n🏆 Topper Student → Roll No: {topper_roll} | Total Marks: {highest_total}")

# 3 Display all students sorted by average marks (highest first)
sorted_students = sorted(
    students_data.items(),
    key=lambda item: sum(item[1]) / len(item[1]),
    reverse=True
)

print("\n📈 Students Sorted by Average Marks:")
for roll, marks in sorted_students:
    avg = sum(marks) / len(marks)
    print(f"Roll No: {roll} | Average: {avg:.2f}")

# 4 Display total number of students
print("\n👥 Total Students:", len(students_data))

# 5 (Optional) Allow user to search for a student by roll number
search_roll = input("\n🔍 Enter a Roll Number to search: ")
if search_roll in students_data:
    print(f"Record Found → Roll No: {search_roll}, Marks: {students_data[search_roll]}")
    print(f"Total = {sum(students_data[search_roll])}, Average = {sum(students_data[search_roll]) / len(students_data[search_roll]):.2f}")
else:
    print("❌ No record found for that roll number.")

print("\n🎯 Program Completed Successfully!")
