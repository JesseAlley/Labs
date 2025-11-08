#Jesse Alley
#Student GPA 
#This application will accept a student name and their gpa and determine whether they make the Dean's List or the Honor Roll or neither

processing = True

while(processing):
    #Gather student's last name
    last_name = input("Please enter student's last name ")

    exit_command = {"ZZZ", "zzz"}

    #Check for loop exit command
    if(last_name in exit_command):
        print("Terminating program")
        break;

    #Process new student
    else:
        #Gather student's first name
        first_name = input("Please enter student's first name ")

        #Gather student's GPA
        student_gpa = float(input("Please enter student's GPA "))

        #Print student record
        print(f"\n{first_name} {last_name}'s GPA is {student_gpa}")

        #Determine student's academic standing
        if(student_gpa >= 3.5):
            print(f"{first_name} is on the Dean's List\n")
        elif(student_gpa >= 3.25):
            print(f"{first_name} is on the Honor Roll\n")
        else:
            print("\n")