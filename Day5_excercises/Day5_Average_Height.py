# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆

# calculate the average without using len() and sum()
students_number = 0
cumulative_height = 0

#counting the number of the members
for i in student_heights:
  students_number += 1

for i in student_heights:
  cumulative_height += i

print(f"Average height is = {cumulative_height/students_number}")

#Write your code below this row 👇




