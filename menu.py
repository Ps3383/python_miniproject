
import student_operations as so

#-------------main-----------
while True :
    so.clear()
    print("press A to add student")
    print("press F to find active student")
    print("press FG to find graduated student")
    print("press L to see list of Active students ")
    print("press D to delete active student")
    print("press DG to delete graduated student ")
    print("press S to save student ")
    print("press C to change courses of active student")
    print("press LG to see list of graduated students")
    print("press M to move student to graduate ")
    print("print Q to quit application")
    choice=input("enter your choice : ").upper()

    if choice=='A':
      so.add_student()

    elif choice=='F':
       so.find_active_student()

    elif choice=="FG":
       so.find_graduated_student()  

    elif choice=='L':
       so.list_active_student()

    elif choice=='D':
       so.delete_active_student()

    elif choice=="DG":
       so.delete_gradute_student()
    
    elif choice=='S':
       so.save_student()

    elif choice=='C':
       so.change_student()

    elif choice=="LG":
       so.list_graduate_student()

    elif choice == 'M':
      code_melli = input("Enter the code_melli of the student to move to graduated list : ")
      so.move_to_graduated(code_melli)   
    
    elif choice=='Q':
       exit()
    else :
       input("wrong input! press any key to back to menu ")   