# a simple program for converting scores to grades with dictionaries
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}
# going through the scores then storing it inside another dictionary
for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"

    elif 81 <= student_scores[key] < 91:
        student_grades[key] = "Exceeds Expectations"

    elif 71 <= student_scores[key] < 81:
        student_grades[key] = "Acceptable"

    else:
        student_grades[key] = "Fail"

# printing the grades dictionary

for key in student_grades:
    print(f"{key} : {student_grades[key]}.")