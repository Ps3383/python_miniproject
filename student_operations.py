from os import system
from datetime import datetime
from khayyam import JalaliDatetime #to change time to jalali

clear=lambda : system("cls")


from pickle import load
try :
      with open("Active_students.db","rb") as sti :
       active_students=load(sti)
except(FileNotFoundError):
   active_students=[]

try:
   with open("graduated_students.db","rb") as gci:
      graduated_students=load(gci)
except(FileNotFoundError):
 graduated_students = []


now = JalaliDatetime.now() #do this to calculate age

code_melli_list=[] # to check repeated code melli
student_code_list=[] # to check repeated student code


def add_student():
    clear()
    student={}
    student["first_name"]=str(input("enter first name : "))
    student["last_name"]=str(input("enter last name : "))


    while True: 
     birthdate_str =input("enter your birthday yyyy-mm-dd : ")
     if birthdate_str.lower() == 'exit':
         break
     try:
          birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
          birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
          student["birthday"]=birthdate
          break
        
     except ValueError:
         print("ba format dadeh shode vared kon ! ")

    age =calculate_age(birthdate) #def in down this code
    student["age"]=age


    while True:
         code_melli=(input("enter code_melli(10 digit number) : "))

         if len(code_melli)!=10:
            print("enter 10 digits")
            continue
         if code_melli in code_melli_list:   
              print("tekrari vared kardi")
              continue

         else:
           student["code_melli"]=code_melli  
           code_melli_list.append(code_melli)
           break
     
    while True:
         student_code=input("enter student code(5 digit number) : ")
         if len(student_code)!=5:
              print("enter 5 digit !")
              continue
         if student_code in student_code_list:
              print("tekrari hast dobare vared kon !")
              continue
         else:
              student["student_code"]=student_code
              student_code_list.append(student_code)
              break


    student["courses"]=input("enter the courses(if there are more than one use (,)) : ").split(",")
    student["grades"] = input("Enter the grades (if there are more than one use(,)): ").split(",")
    grades = [float(grade) for grade in student["grades"]]
    total_grades = sum(grades)
    average_grade = total_grades/len(grades)
    student["average_grade"] = float(average_grade)
    student["max_grade"]=max(grades)
    student["min_grade"]=min(grades)
    
    active_students.append(student)

def find_active_student():
    clear()
    code_melli=input("enter active_student_code_melli that you want to find : ")
    for student in active_students:
        if student["code_melli"]==code_melli:
               print("\n\n******************************\n")
               print("first name :",    student["first_name"])
               print("last_name :",     student["last_name"])
               print("birthday :",      student["birthday"])
               print("code_melli :",    student["code_melli"])
               print("student_code :",  student["student_code"])
               print("courses :",       student["courses"])
               print("grades :",        student["grades"])
               print("average_grades: ",student["average_grade"])
               print("max grade :",     student["max_grade"])
               print("min grade :",     student["min_grade"])
               print("age :",           student["age"])
               input("\npress any key to back to menu")
              
               break
    else :
         input("\n\ncant find ! press any key to back to menu ")


def find_graduated_student():
    clear()
    code_melli=input("enter graduated_student_code_melli that you want to find : ")
    for student in graduated_students:
        if student["code_melli"]==code_melli:
               print("\n\n******************************\n")
               print("first name :",    student["first_name"])
               print("last_name :",     student["last_name"])
               print("birthday :",      student["birthday"])
               print("code_melli :",    student["code_melli"])
               print("student_code :",  student["student_code"])
               print("courses :",       student["courses"])
               print("grades :",        student["grades"])
               print("average_grades: ",student["average_grade"])
               print("max grade :",     student["max_grade"])
               print("min grade :",     student["min_grade"])
               print("age :",           student["age"])
               input("\npress any key to back to menu")
               
              
               break
    else :
         input("\n\ncant find ! press any key to back to menu ")





def list_active_student():
     clear()
     print("+++++++++++++++++++++ Active_students ++++++++++++++++++++++\n\n")
     for student in active_students:
               print("first name :",  student["first_name"])
               print("last_name :",   student["last_name"])
               print("birthday :",    student["birthday"])
               print("code_melli :",  student["code_melli"])
               print("student_code :",student["student_code"],"\n\n")
               #print("courses :",     student["courses"])
               #print("grades :",      student["grades"])
               #print("average_grades : ",student["average_grade"])
               #print("max grade :",   student["max_grade"])
               #print("min grade :",   student["min_grade"])
               #print("age :",         student["age"],"\n\n")
               print("******************************\n")
     input("press any key to back to menu")


def list_graduate_student():
    clear()
    print("++++++++++++++  graduated_students  ++++++++++++++++\n\n")
    for student in graduated_students:
               print("first name :",      student["first_name"])
               print("last_name :",       student["last_name"])
               print("birthday :",        student["birthday"])
               print("code_melli :",      student["code_melli"])
               print("student_code :",    student["student_code"],"\n\n")
               #print("courses :",        student["courses"])
               #print("grades :",         student["grades"])
               #print("average_grades : ",student["average_grade"])
               #print("max grade :",      student["max_grade"])
               #print("min grade :",      student["min_grade"])
               #print("age :",            student["age"],"\n\n")
               print("******************************\n")
    input("press any key to back to menu")



def delete_active_student():
      clear()
      code_melli=input("enter code_melli of active student that you want to delete : ")
      for student in active_students:
            if student["code_melli"]==code_melli:
                  active_students.remove(student)
                  save_student()
                  input("your student was sussesfuly delete press any key to back to menu")                
                  break            
      else:
            input("\n\ndoes not exist ! press any key to back to menu ")


def delete_gradute_student():
      clear()
      code_melli=input("enter code_melli of graduted student that you want to delete : ")
      for student in graduated_students:
            if student["code_melli"]==code_melli:
                  graduated_students.remove(student)
                  save_graduated_students()
                  input("your graduted_student was sussesfuly delete ! press any key to back to menu")                
                  break            
      else:
            input("\n\ndoes not exist ! press any key to back to menu ")



def save_student():
      from pickle import dump
      with open("Active_students.db","wb") as sti:
          dump(active_students,sti)
          input("successfully saved ! press any key to back to menu")



def save_graduated_students():
    from pickle import dump
    with open("graduated_students.db", "wb") as gsi:
        dump(graduated_students, gsi)



def move_to_graduated(code_melli):
    for student in active_students:
        if student["code_melli"] == code_melli:
            graduated_students.append(student)
            active_students.remove(student)
            print("Student moved to graduated list successfully!") 
            save_graduated_students()  # Save changes to the graduated students database
            save_student()  # Save changes to the main database
            return
    else:
        input("Student not found in the main database. press any key to back to menu.")
        return




def change_student():
    clear()
    code_melli = input("Enter the code_melli of the student you want to modify : ")

    for student in active_students:
        if student["code_melli"] == code_melli:
            print("+++++++++++++")
            print("1. Change Courses")
            print("2. Change Grades")
            print("3. Back to Menu")
            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                new_courses = input("Enter the new courses from fist then choose change grades (if there are more than one, use comma): ").split(",")
                student["courses"] = new_courses
                print("Courses updated successfully!")

            elif choice == '2':
                new_grades = input("Enter the new grades from the first (if there are more than one, use comma): ").split(",")
                grades = [int(grade) for grade in new_grades]
                total_grades = sum(grades)
                average_grade = total_grades / len(grades)
                student["grades"] = new_grades
                student["average_grade"] = float(average_grade)
                student["max_grade"] = max(grades)
                student["min_grade"] = min(grades)
                print("Grades updated successfully!")

            elif choice == '3':
                return

            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

            break

    else:
        input("\n\nStudent not found ! press any key to back to menu ")
      

def calculate_age(birthdate):
    today = now
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

