print("Exam Grade Calculator")
name_of_exam = input("Name of exam? ")
print("=== " + name_of_exam + " ===")
total_score = int(input("Max. Possible Score?: "))
score = int(input("Your Score?: "))
percent = int((score / total_score) * 100)

if percent < 50:
    grade = "F"
elif percent < 60:
    grade = "D"
elif percent < 70:
    grade = "C"
elif percent < 80:
    grade = "B"
elif percent < 90:
    grade = "A"
elif percent <= 100:
    grade = "A+"
else:
    print("Wrong Score..!, Try again:)")

if percent <= 100:
    print(f"You got {percent}% and your grade is {grade}")
