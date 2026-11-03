employees = {}

def get_number(prompt, minimum=0):
    while True:
        try:
            value = float(input(prompt))
            if value >= minimum:
                return value
            print(f"Enter a value of at least {minimum}.")
        except ValueError:
            print("Enter a valid number.")

def register_employee():
    employee_id = input("Enter employee ID: ").strip()
    if not employee_id or employee_id in employees:
        print("Employee ID is empty or already exists.")
        return
    name = input("Enter employee name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    salary = get_number("Enter monthly basic salary (Rs.): ", 0.01)
    employees[employee_id] = {"name": name, "salary": salary, "attendance": []}
    print("Employee registered successfully.")

def record_attendance():
    employee_id = input("Enter employee ID: ").strip()
    if employee_id not in employees:
        print("Employee not found.")
        return
    date = input("Enter date (YYYY-MM-DD): ").strip()
    if not date:
        print("Date cannot be empty.")
        return
    attendance = employees[employee_id]["attendance"]
    for record in attendance:
        if record[0] == date:
            print("Attendance has already been recorded for this date.")
            return
    status = input("Enter status (Present/Absent/Leave): ").strip().capitalize()
    if status not in ("Present", "Absent", "Leave"):
        print("Invalid attendance status.")
        return
    if len(attendance) >= 30:
        print("A maximum of 30 attendance records is allowed per employee.")
        return
    attendance.append((date, status))
    print("Attendance recorded successfully.")

def display_attendance():
    employee_id = input("Enter employee ID: ").strip()
    if employee_id not in employees:
        print("Employee not found.")
        return
    attendance = employees[employee_id]["attendance"]
    print(f"\nAttendance history for {employees[employee_id]['name']}:")
    if not attendance:
        print("No attendance records available.")
        return
    for date, status in attendance:
        print(f"{date}: {status}")

def attendance_counts(attendance):
    present = 0
    absent = 0
    leave = 0
    for date, status in attendance:
        if status == "Present":
            present += 1
        elif status == "Absent":
            absent += 1
        elif status == "Leave":
            leave += 1
    return present, absent, leave

def calculate_salary(employee):
    present, absent, leave = attendance_counts(employee["attendance"])
    daily_salary = employee["salary"] / 30
    salary = employee["salary"] - (absent * daily_salary)
    recorded_days = present + absent + leave
    attendance_rate = ((present + leave) / recorded_days * 100) if recorded_days else 0
    bonus = salary * 0.10 if attendance_rate >= 95 else 0
    return salary + bonus, present, absent, leave, attendance_rate, bonus

def display_attendance_rates():
    if not employees:
        print("No employees are registered.")
        return
    highest_id = None
    lowest_id = None
    highest_rate = -1
    lowest_rate = 101
    for employee_id, employee in employees.items():
        present, absent, leave = attendance_counts(employee["attendance"])
        recorded = present + absent + leave
        rate = ((present + leave) / recorded * 100) if recorded else 0
        if rate > highest_rate:
            highest_rate = rate
            highest_id = employee_id
        if rate < lowest_rate:
            lowest_rate = rate
            lowest_id = employee_id
    print(f"Highest attendance: {employees[highest_id]['name']} ({highest_rate:.2f}%)")
    print(f"Lowest attendance: {employees[lowest_id]['name']} ({lowest_rate:.2f}%)")

def payroll_report():
    if not employees:
        print("No employees are registered.")
        return
    print("\n================ MONTHLY PAYROLL REPORT ================")
    for employee_id, employee in employees.items():
        salary, present, absent, leave, rate, bonus = calculate_salary(employee)
        print(f"\nID: {employee_id} | Name: {employee['name']}")
        print(f"Present: {present} | Absent: {absent} | Leave: {leave}")
        print(f"Attendance rate: {rate:.2f}%")
        print(f"Basic salary: Rs. {employee['salary']:.2f}")
        print(f"Absence deduction: Rs. {(absent * employee['salary'] / 30):.2f}")
        print(f"Bonus: Rs. {bonus:.2f}")
        print(f"Net salary: Rs. {salary:.2f}")

def main():
    while True:
        print("\n===== EMPLOYEE PAYROLL AND ATTENDANCE =====")
        print("1. Register employee")
        print("2. Record attendance")
        print("3. Display attendance history")
        print("4. Display attendance rates")
        print("5. Generate monthly payroll report")
        print("6. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            register_employee()
        elif choice == "2":
            record_attendance()
        elif choice == "3":
            display_attendance()
        elif choice == "4":
            display_attendance_rates()
        elif choice == "5":
            payroll_report()
        elif choice == "6":
            print("Payroll system closed.")
            break
        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()
