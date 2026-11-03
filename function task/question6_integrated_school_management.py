students = {}
teachers = {}
books = {}
borrowed_books = []

def get_integer(prompt, minimum=0, maximum=None):
    while True:
        try:
            value = int(input(prompt))
            if value < minimum or (maximum is not None and value > maximum):
                print("Please enter a number within the allowed range.")
            else:
                return value
        except ValueError:
            print("Please enter a valid whole number.")

def register_student():
    student_id = input("Student ID: ").strip()
    if not student_id or student_id in students:
        print("Student ID is empty or already exists.")
        return
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    age = get_integer("Age: ", 1, 120)
    marks = []
    for subject in range(1, 6):
        marks.append(get_integer(f"Subject {subject} mark (0-100): ", 0, 100))
    students[student_id] = {"name": name, "age": age, "marks": tuple(marks), "attendance": []}
    print("Student registered successfully.")

def record_student_marks():
    student_id = input("Student ID: ").strip()
    if student_id not in students:
        print("Student not found.")
        return
    marks = []
    for subject in range(1, 6):
        marks.append(get_integer(f"New mark for subject {subject} (0-100): ", 0, 100))
    students[student_id]["marks"] = tuple(marks)
    print("Marks updated successfully.")

def record_student_attendance():
    student_id = input("Student ID: ").strip()
    if student_id not in students:
        print("Student not found.")
        return
    date = input("Date (YYYY-MM-DD): ").strip()
    if not date:
        print("Date cannot be empty.")
        return
    records = students[student_id]["attendance"]
    for record in records:
        if record[0] == date:
            print("Attendance already exists for this date.")
            return
    status = input("Status (Present/Absent/Leave): ").strip().capitalize()
    if status not in ("Present", "Absent", "Leave"):
        print("Invalid attendance status.")
        return
    records.append((date, status))
    print("Attendance recorded successfully.")

def register_teacher():
    teacher_id = input("Teacher ID: ").strip()
    if not teacher_id or teacher_id in teachers:
        print("Teacher ID is empty or already exists.")
        return
    name = input("Teacher name: ").strip()
    subject = input("Assigned subject: ").strip()
    if not name or not subject:
        print("Name and subject cannot be empty.")
        return
    teachers[teacher_id] = {"name": name, "subject": subject}
    print("Teacher registered successfully.")

def display_teachers():
    if not teachers:
        print("No teachers are registered.")
        return
    for teacher_id, teacher in teachers.items():
        print(f"{teacher_id} | {teacher['name']} | Subject: {teacher['subject']}")

def add_book():
    book_id = input("Book ID: ").strip()
    if not book_id or book_id in books:
        print("Book ID is empty or already exists.")
        return
    title = input("Book title: ").strip()
    author = input("Author: ").strip()
    if not title or not author:
        print("Title and author cannot be empty.")
        return
    copies = get_integer("Number of copies: ", 0)
    books[book_id] = {"title": title, "author": author, "copies": copies}
    print("Book added successfully.")

def display_books():
    if not books:
        print("No books are registered.")
        return
    for book_id, book in books.items():
        print(f"{book_id} | {book['title']} | {book['author']} | Available copies: {book['copies']}")

def borrow_book():
    student_id = input("Student ID: ").strip()
    if student_id not in students:
        print("Student not found. Only registered students can borrow books.")
        return
    book_id = input("Book ID: ").strip()
    if book_id not in books:
        print("Book not found.")
        return
    if books[book_id]["copies"] <= 0:
        print("No copies are available.")
        return
    books[book_id]["copies"] -= 1
    borrowed_books.append((student_id, book_id))
    print("Book borrowed successfully.")

def return_book():
    student_id = input("Student ID: ").strip()
    book_id = input("Book ID: ").strip()
    record = (student_id, book_id)
    if record not in borrowed_books:
        print("No matching borrowing record was found.")
        return
    borrowed_books.remove(record)
    books[book_id]["copies"] += 1
    print("Book returned successfully.")

def calculate_total(marks):
    total = 0
    for mark in marks:
        total += mark
    return total

def get_attendance_percentage(records):
    if not records:
        return 0
    attended = 0
    for date, status in records:
        if status in ("Present", "Leave"):
            attended += 1
    return attended / len(records) * 100

def generate_student_report():
    if not students:
        print("No students are registered.")
        return
    results = []
    class_total = 0
    passed_count = 0
    failed_count = 0
    for student_id, student in students.items():
        total = calculate_total(student["marks"])
        average = total / len(student["marks"])
        passed = all(mark >= 40 for mark in student["marks"])
        if passed:
            passed_count += 1
            status = "PASS"
        else:
            failed_count += 1
            status = "FAIL"
        class_total += average
        results.append({"id": student_id, "name": student["name"], "total": total,
                        "average": average, "status": status,
                        "attendance": get_attendance_percentage(student["attendance"])})
    results.sort(key=lambda item: item["average"], reverse=True)
    print("\n================ STUDENT PERFORMANCE REPORT ================")
    for rank, result in enumerate(results, start=1):
        print(f"\nRank: {rank} | ID: {result['id']} | Name: {result['name']}")
        print(f"Total: {result['total']}/500 | Average: {result['average']:.2f}%")
        print(f"Result: {result['status']} | Attendance: {result['attendance']:.2f}%")
    class_average = class_total / len(students)
    print("\n================ CLASS STATISTICS ================")
    print(f"Class average: {class_average:.2f}%")
    print(f"Students passed: {passed_count}")
    print(f"Students failed: {failed_count}")

def display_student_attendance():
    student_id = input("Student ID: ").strip()
    if student_id not in students:
        print("Student not found.")
        return
    records = students[student_id]["attendance"]
    if not records:
        print("No attendance records are available.")
        return
    for date, status in records:
        print(f"{date}: {status}")
    print(f"Attendance percentage: {get_attendance_percentage(records):.2f}%")

def main():
    while True:
        print("\n========== INTEGRATED SCHOOL MANAGEMENT SYSTEM ==========")
        print("1. Register student")
        print("2. Update student marks")
        print("3. Record student attendance")
        print("4. Display student attendance")
        print("5. Register teacher")
        print("6. Display teachers")
        print("7. Add book")
        print("8. Display books")
        print("9. Borrow book")
        print("10. Return book")
        print("11. Generate student rankings and class report")
        print("12. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            register_student()
        elif choice == "2":
            record_student_marks()
        elif choice == "3":
            record_student_attendance()
        elif choice == "4":
            display_student_attendance()
        elif choice == "5":
            register_teacher()
        elif choice == "6":
            display_teachers()
        elif choice == "7":
            add_book()
        elif choice == "8":
            display_books()
        elif choice == "9":
            borrow_book()
        elif choice == "10":
            return_book()
        elif choice == "11":
            generate_student_report()
        elif choice == "12":
            print("School management system closed.")
            break
        else:
            print("Invalid choice. Please select 1-12.")

if __name__ == "__main__":
    main()
