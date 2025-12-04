"""
GradeBook Analyzer
Author: Vicky
Date: 1 dec,2025
Description: CLI tool to analyze student marks, assign grades, and generate reports.
"""

import csv
import statistics


# Task 1: Welcome + Menu

def print_menu():
    print("\n====== GradeBook Analyzer ======")
    print("1. Manual Student Entry")
    print("2. Load from CSV File")
    print("3. Exit")
    print("================================")


# Task 2: Input Methods

def manual_input():
    marks = {}
    n = int(input("Enter number of students: "))

    for _ in range(n):
        name = input("Student Name: ")
        score = float(input("Marks: "))
        marks[name] = score

    return marks


def load_csv():
    marks = {}
    filename = input("Enter CSV filename (example: data.csv): ")

    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                name, score = row
                marks[name] = float(score)
        print("CSV Loaded Successfully!")
    except:
        print("Error: File not found or invalid format.")

    return marks


# Task 3: Statistics Functions

def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    max_student = max(marks_dict, key=marks_dict.get)
    return max_student, marks_dict[max_student]

def find_min_score(marks_dict):
    min_student = min(marks_dict, key=marks_dict.get)
    return min_student, marks_dict[min_student]

# Task 4: Grade Assignment

def assign_grades(marks_dict):
    grades = {}

    for student, marks in marks_dict.items():
        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 60:
            grade = "D"
        else:
            grade = "F"

        grades[student] = grade

    return grades


def grade_distribution(grades):
    distribution = {"A":0, "B":0, "C":0, "D":0, "F":0}

    for g in grades.values():
        distribution[g] += 1

    return distribution


# Task 5: Pass/Fail (List Comprehension)

def pass_fail_list(marks_dict):
    passed = [name for name, m in marks_dict.items() if m >= 40]
    failed = [name for name, m in marks_dict.items() if m < 40]
    return passed, failed

# Task 6: Print Table

def print_table(marks, grades):
    print("\n-----------------------------------------")
    print("Name\t\tMarks\tGrade")
    print("-----------------------------------------")

    for name in marks:
        print(f"{name:<15}\t{marks[name]:<7}\t{grades[name]}")

    print("-----------------------------------------")


# Optional: Export to CSV

def export_csv(marks, grades):
    filename = "gradebook_output.csv"

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Marks", "Grade"])

        for name in marks:
            writer.writerow([name, marks[name], grades[name]])

    print(f"\nCSV Exported Successfully → {filename}")


# MAIN LOOP

def main():
    while True:
        print_menu()
        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            marks = manual_input()

        elif choice == "2":
            marks = load_csv()

        elif choice == "3":
            print("Exiting Program...")
            break

        else:
            print("Invalid choice. Try again.")
            continue

        if len(marks) == 0:
            print("No data found! Try again.")
            continue

        # Process Data
        avg = calculate_average(marks)
        med = calculate_median(marks)
        max_stud, max_marks = find_max_score(marks)
        min_stud, min_marks = find_min_score(marks)

        grades = assign_grades(marks)
        dist = grade_distribution(grades)
        passed, failed = pass_fail_list(marks)

        # Print Analysis
        print("\n===== Analysis Summary =====")
        print(f"Average Marks: {avg:.2f}")
        print(f"Median Marks: {med}")
        print(f"Highest Score: {max_stud} ({max_marks})")
        print(f"Lowest Score: {min_stud} ({min_marks})")

        print("\nGrade Distribution:")
        for g, count in dist.items():
            print(f"{g}: {count}")

        print("\nPassed Students:", passed)
        print("Failed Students:", failed)

        print_table(marks, grades)

        # Optional Export
        exp = input("Export table to CSV? (y/n): ").lower()
        if exp == "y":
            export_csv(marks, grades)

        again = input("\nRun Again? (y/n): ").lower()
        if again != "y":
            print("Thank you for using GradeBook Analyzer!")
            break


# Run Program
main()
