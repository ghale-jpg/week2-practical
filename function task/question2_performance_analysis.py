students = {}

def get_mark(prompt):
    while True:
        try:
            mark = int(input(prompt))
            if 0 <= mark <= 100:
                return mark
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a whole number.")

def register_students():
    count = 0
    while True:
        try:
            count = int(input("How many students do you want to enter? "))
            if count >= 0:
                break
            print("Enter zero or a positive number.")
        except ValueError:
            print("Enter a valid whole number.")
    for number in range(count):
        print(f"\nStudent {number + 1}")
        student_id = input("Student ID: ").strip()
        if not student_id or student_id in students:
            print("ID is empty or already registered. This student was skipped.")
            continue
        name = input("Student name: ").strip()
        if not name:
            print("Name cannot be empty. This student was skipped.")
            continue
        marks = []
        for subject in range(1, 6):
            marks.append(get_mark(f"Subject {subject} mark: "))
        students[student_id] = {"name": name, "marks": tuple(marks)}
    print("Student entry completed.")

def calculate_total(marks):
    total = 0
    for mark in marks:
        total += mark
    return total

def calculate_average(marks):
    if not marks:
        return 0
    return calculate_total(marks) / len(marks)

def get_highest_lowest(marks):
    if not marks:
        return None, None
    highest = marks[0]
    lowest = marks[0]
    for mark in marks[1:]:
        if mark > highest:
            highest = mark
        if mark < lowest:
            lowest = mark
    return highest, lowest

def analyze_students():
    if not students:
        print("No students are registered. Please enter student data first.")
        return
    passed = []
    failed = []
    results = []
    class_total = 0
    mark_count = 0
    for student_id, details in students.items():
        marks = details["marks"]
        total = calculate_total(marks)
        average = calculate_average(marks)
        highest, lowest = get_highest_lowest(marks)
        class_total += total
        mark_count += len(marks)
        result = {"id": student_id, "name": details["name"], "total": total,
                  "average": average, "highest": highest, "lowest": lowest}
        results.append(result)
        if all(mark >= 40 for mark in marks):
            passed.append(details["name"])
        else:
            failed.append(details["name"])
    results.sort(key=lambda item: item["average"], reverse=True)
    print("\n========== STUDENT PERFORMANCE REPORT ==========")
    for rank, result in enumerate(results, start=1):
        print(f"\nRank: {rank}")
        print(f"Student: {result['name']} (ID: {result['id']})")
        print(f"Total: {result['total']}/500")
        print(f"Average: {result['average']:.2f}%")
        print(f"Highest mark: {result['highest']}")
        print(f"Lowest mark: {result['lowest']}")
    class_average = class_total / mark_count if mark_count else 0
    print("\nPassed all subjects:", ", ".join(passed) if passed else "None")
    print("Failed at least one subject:", ", ".join(failed) if failed else "None")
    print(f"Class average: {class_average:.2f}%")

def main():
    while True:
        print("\n===== STUDENT PERFORMANCE ANALYSIS =====")
        print("1. Enter student records")
        print("2. Display performance analysis")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            register_students()
        elif choice == "2":
            analyze_students()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select 1-3.")

if __name__ == "__main__":
    main()
