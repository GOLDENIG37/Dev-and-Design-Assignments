Number_of_Student = int(input("How many students do you have? "))
student_name = []
student_grade = []
count = 0 
while count < Number_of_Student:
    name = input("What is the name of the student? ")
    student_name.append(name)
    grade = int(input(f"What is {name} grade? "))
    if grade <= 100 and grade > 0:
        student_grade.append(grade)
        count += 1
    else:
        grade = int(input(f"{name} grade is incorrect, try again: "))

#Average grade of students
total_grade = 0
for each_grade in student_grade:
    total_grade += each_grade 

average = total_grade / Number_of_Student
print(f"The average grade of my students are {average}")

#Determine pass and fail status
for i in range(Number_of_Student ):
    if student_grade[i] <= 80:
        print(f" {student_name[i]} failed with score {student_grade[i]} ")
    else:
        print(f" {student_name[i]} passed with score {student_grade[i]} ")


lowest_score = student_grade[i]
highest_score = student_grade[i]

best_student = student_name[i]
worst_student = student_name[i]

if highest_score < student_grade[i]:
    highest_score = student_grade[i]
    best_student = student_name[i]

if lowest_score > student_grade[i]:
    lowest_score = student_grade[i]
    worst_student = student_name[i]

print(f"The student with the highest score is {best_student} with {highest_score} out of 100.")
print(f"The student with the lowest score is {worst_student} with {lowest_score} out of 100.")