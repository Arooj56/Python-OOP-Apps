import tkinter as tk
from tkinter import messagebox

grade_to_point = {
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D": 1.3,
    "F": 0.0,
}


def calculate_gpa():
    try:
        total_credits = 0
        total_grade_points = 0

        for i in range(len(grade_entries)):
            grade = grade_entries[i].get().upper()
            credit = float(credit_entries[i].get())

            if grade not in grade_to_point:
                raise ValueError(f"Invalid grade: {grade}")

            grade_point = grade_to_point[grade]
            total_credits += credit
            total_grade_points += grade_point * credit

        if total_credits == 0:
            raise ValueError("Total credits cannot be zero.")

        gpa = total_grade_points / total_credits
        gpa_label.config(text=f"GPA: {gpa:.2f}")

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))


def calculate_cgpa():
    try:
        total_credits = 0
        total_grade_points = 0

        for i in range(len(grade_entries)):
            grade = grade_entries[i].get().upper()
            credit = float(credit_entries[i].get())

            if grade not in grade_to_point:
                raise ValueError(f"Invalid grade: {grade}")

            grade_point = grade_to_point[grade]
            total_credits += credit
            total_grade_points += grade_point * credit

        if total_credits == 0:
            raise ValueError("Total credits cannot be zero.")

        gpa = total_grade_points / total_credits
        previous_gpa = float(prev_gpa_entry.get())
        previous_credits = float(prev_credits_entry.get())

        if previous_credits > 0:
            cgpa = ((previous_gpa * previous_credits) + total_grade_points) / (
                previous_credits + total_credits
            )
        else:
            cgpa = gpa

        gpa_label.config(text=f"GPA: {gpa:.2f}")
        cgpa_label.config(text=f"CGPA: {cgpa:.2f}")

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))


def add_subject(subject_name="", credit_default="3"):
    row = len(subject_entries) + 3
    subject_entry = tk.Entry(root, width=20)
    subject_entry.grid(row=row, column=0, padx=10, pady=5)
    subject_entries.append(subject_entry)

    grade_entry = tk.Entry(root, width=15)
    grade_entry.grid(row=row, column=1, padx=10, pady=5)
    grade_entries.append(grade_entry)

    if subject_name:
        subject_entry.insert(0, subject_name)

        credit_entry = tk.Entry(root, width=10)
        credit_entry.insert(0, "0.5")
        credit_entry.grid(row=row, column=2, padx=10, pady=5)
        credit_entries.append(credit_entry)

    else:
        credit_var = tk.StringVar(value=credit_default)
        credit_entry = tk.OptionMenu(root, credit_var, "1", "2", "3", "4")
        credit_entry.grid(row=row, column=2, padx=10, pady=5)
        credit_entries.append(credit_var)

root = tk.Tk()
root.title("GPA Calculator")

subject_entries = []
grade_entries = []
credit_entries = []


add_subject("QT", "0.5")

for _ in range(5):
    add_subject()

add_button = tk.Button(root, text="Add Another Subject", command=add_subject)
add_button.grid(row=0, column=0, columnspan=3, pady=5)

tk.Label(root, text="Subject Names").grid(row=2, column=0, padx=10, pady=5)
tk.Label(root, text="Grades").grid(row=2, column=1, padx=10, pady=5)
tk.Label(root, text="Credit Hours").grid(row=2, column=2, padx=10, pady=5)

gpa_label = tk.Label(root, text="GPA: ")
gpa_label.grid(row=100, column=1, columnspan=1, pady=5)

calculate_gpa_button = tk.Button(root, text="Calculate GPA", command=calculate_gpa)
calculate_gpa_button.grid(row=100, column=0, pady=5, padx=5)

tk.Label(root, text="Previous GPA:").grid(row=101, column=0, padx=10, pady=5)
prev_gpa_entry = tk.Entry(root, width=15)
prev_gpa_entry.grid(row=101, column=1, padx=10, pady=5)

tk.Label(root, text="  Previous Total Credits:").grid(row=102, column=0, padx=10, pady=5)
prev_credits_entry = tk.Entry(root, width=15)
prev_credits_entry.grid(row=102, column=1, padx=10, pady=5)

calculate_cgpa_button = tk.Button(root, text="Calculate CGPA", command=calculate_cgpa)
calculate_cgpa_button.grid(row=103, column=0, pady=5, padx=5)

cgpa_label = tk.Label(root, text="CGPA: ")
cgpa_label.grid(row=103, column=1, pady=5)
root.mainloop()
