def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def add_student(records):
    name = input("Enter student name: ").strip()
    num_subjects = int(input("Enter number of subjects: "))
    marks = []
    for i in range(num_subjects):
        score = float(input(f"Enter marks for subject {i + 1} (out of 100): "))
        marks.append(score)

    total = sum(marks)
    percentage = round(total / num_subjects, 2)
    grade = calculate_grade(percentage)

    records.append({
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    })
    print(f"\nRecord added for {name} | Percentage: {percentage}% | Grade: {grade}\n")


def view_records(records):
    if not records:
        print("\nNo student records found.\n")
        return

    print("\n--- Student Grade Report ---")
    for student in records:
        print(f"Name: {student['name']} | Total: {student['total']} | Percentage: {student['percentage']}% | Grade: {student['grade']}")
    print("----------------------------\n")


def main():
    student_records = []
    while True:
        print("=== Student Grade Calculator ===")
        print("1. Add Student Marks")
        print("2. View All Student Reports")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_student(student_records)
        elif choice == "2":
            view_records(student_records)
        elif choice == "3":
            print("Exiting Student Grade Calculator.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
