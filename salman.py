grade = int(input("Enter your grade: "))

if (grade > 100) or (grade < 0):
    print("Invalid value")
else:
    if (grade <= 100) and (grade >= 90): 
        print("Your grade is A")
        print("With complement")
    elif (grade < 90) and (grade >= 80): 
        print("Your grade is B")
        print("Very Satisfy")
    elif (grade < 80) and (grade >= 70): 
        print("Your grade is C")
        print("Satisfying")
    elif (grade < 70) and (grade >= 60): 
        print("Your grade is D")
        print("Not Satisfactory")
    elif (grade < 59): 
        print("Your grade is E")
        print("Didn't PASS")
