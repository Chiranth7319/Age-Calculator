from tkinter import *
from tkinter import messagebox
from datetime import date, datetime

# Function to calculate age
def calculate_age():
    try:
        dob = datetime.strptime(entry_dob.get(), "%d/%m/%Y").date()
        today = date.today()

        years = today.year - dob.year
        months = today.month - dob.month
        days = today.day - dob.day

        if days < 0:
            months -= 1
            # Days in the previous month
            if today.month == 1:
                prev_month = 12
                prev_year = today.year - 1
            else:
                prev_month = today.month - 1
                prev_year = today.year

            if prev_month in [1, 3, 5, 7, 8, 10, 12]:
                days += 31
            elif prev_month in [4, 6, 9, 11]:
                days += 30
            else:
                
                if (prev_year % 4 == 0 and prev_year % 100 != 0) or (prev_year % 400 == 0):
                    days += 29
                else:
                    days += 28

        if months < 0:
            years -= 1
            months += 12

        result.config(
            text=f"Age: {years} Years, {months} Months, {days} Days"
        )

    except:
        messagebox.showerror("Error", "Enter date in DD/MM/YYYY format")


# Main window
root = Tk()
root.title("Age Calculator")
root.geometry("400x250")
root.config(bg="lightblue")

# Heading
Label(root, text="Age Calculator", font=("Arial", 18, "bold"),
      bg="lightblue").pack(pady=10)

# Date of Birth
Label(root, text="Enter DOB (DD/MM/YYYY):",
      font=("Arial", 12), bg="lightblue").pack()

entry_dob = Entry(root, font=("Arial", 12), width=20)
entry_dob.pack(pady=5)

# Button
Button(root, text="Calculate Age", font=("Arial", 12),
       command=calculate_age).pack(pady=10)

# Result Label
result = Label(root, text="", font=("Arial", 12, "bold"),
               bg="lightblue", fg="blue")
result.pack(pady=10)

root.mainloop()