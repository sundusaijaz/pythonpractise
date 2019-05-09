name = input("Enter name of Student: ")
rollno = input("Enter Roll no of Student: ")
sub_1 = int(input("Enter marks obtained in 1st subject: "))
sub_2 = int(input("Enter marks obtained in 2nd subject: "))
sub_3 = int(input("Enter marks obtained in 3rd subject: "))
sub_4 = int(input("Enter marks obtained in 4th subject: "))
sub_5 = int(input("Enter marks obtained in 5th subject: "))
marks_obtain = sub_1 + sub_2 + sub_3 + sub_4 + sub_5
total_marks = 500
percent = ((marks_obtain / total_marks) * 100)
if percent >= 90:
    print("Grade A+")
elif percent >= 80 & percent < 90 :
    print("Grade A") 
elif percent >= 70 & percent < 80 :
    print("Grade B") 
elif percent >= 60 & percent < 70 :
    print("Grade C")    
elif percent >= 50 & percent < 60 :
    print("Grade D")
else:
    print("Fail")            