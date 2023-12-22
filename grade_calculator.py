"""
    Nazmul Zaman 
    Bsc in IT
"""

def user_grade(marks):
    if not 0 <= marks <= 100:
        return "Invalid Entry"
    elif marks < 40:
        return "Fail"
    elif marks < 50:
        return "D"
    elif marks < 60:
        return "C"
    elif marks < 70:
        return "B"
    elif marks < 80:
        return "A-"
    elif marks < 90:
        return "A"
    else:
        return "A+"

while True:
    try:
        marks = input("Enter your marks (or type 'exit' to end): ")
        if marks.lower() == "exit":
            break
        marks = int(marks)
        grade = user_grade(marks)
        print(f"Your grade is: {grade}")
    except ValueError:
        print("Please enter a valid integer for marks.")
