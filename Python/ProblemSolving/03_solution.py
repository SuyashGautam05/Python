# score = int(input("Enter your marks : "))
score =  103

if score >= 101:
    print("Please recheck your marks !!!")
    exit()

if score >=  90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Grade: ", grade)