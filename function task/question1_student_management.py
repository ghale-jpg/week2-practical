students = {}

def get_integer(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print("Value is too small.")
            elif maximum is not None and value > maximum:
                print("Value is too large.")
            else:
                return value
        except ValueError:
            print("Please enter a valid whole number.")

def get_marks():
    marks = []
    for subject in range(1, 6):
        mark = get_integer(f"Enter mark for subject {subject} (0-100): ", 0, 100)
        marks.append(mark)
    return tuple(marks)

def register_student():
    student_id = input("Enter student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return
    if student_id in students:
        print("This student ID already exists.")
        return
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    age = get_integer("Enter age: ", 1, 120)
    marks = get_marks()
    students[student_id] = {"name": name, "age": age, "marks": marks}
    print("Student registered successfully.")

def display_students():
    if not students:
        print("No students are registered.")
        return
    for student_id, details in students.items():
        print(f"\nID: {student_id}")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Marks: {details['marks']}")

def search_student():
    student_id = input("Enter student ID to search: ").strip()
    student = students.get(student_id)
    if student is None:
        print("Student not found.")
    else:
        print(f"ID: {student_id} | Name: {student['name']} | Age: {student['age']} | Marks: {student['marks']}")

def update_marks():
    student_id = input("Enter student ID: ").strip()
    if student_id not in students:
        print("Student not found.")
        return
    print("Enter the five updated marks.")
    students[student_id]["marks"] = get_marks()
    print("Marks updated successfully.")

def remove_student():
    student_id = input("Enter student ID to remove: ").strip()
    if student_id in students:
        del students[student_id]
        print("Student removed successfully.")
    else:
        print("Student not found.")

def display_age_range():
    if not students:
        print("No students are registered.")
        return
    lower = get_integer("Enter minimum age: ", 1, 120)
    upper = get_integer("Enter maximum age: ", lower, 120)
    found = False
    for student_id, details in students.items():
        if lower <= details["age"] <= upper:
            print(f"{student_id}: {details['name']} ({details['age']} years)")
            found = True
    if not found:
        print("No students were found in this age range.")

def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Register student")
        print("2. Display all students")
        print("3. Search student by ID")
        print("4. Update student marks")
        print("5. Remove student")
        print("6. Display students by age range")
        print("7. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            register_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            remove_student()
        elif choice == "6":
            display_age_range()
        elif choice == "7":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Please select 1-7.")

if __name__ == "__main__":
    main()
