# attendance_system


#this is for call add student code fron student.py
from student import student_management



# this code is for the show feature to user in short menu
def showmenu():
    
    
    print("\n======================================================================")
    print("                  SMART ATTENDANCE MANAGEMENT SYSTEM") 
    print("======================================================================\n")
    
    print("1. Student Management")
    print("2. Attendance Management")
    print("3. Performance / Marks Management")
    print("4. Performance Analysis")
    print("5. Reports Generation")
    print("6. Admin Settings")
    print("7. Exit System\n")



# this is the main where execution start
while True:
    
    showmenu()
    n=int(input("Enter What You Want To Do :- "))
    print("\n\n")
    
    if n==1:
        student_management()
        
    
    elif n==7:
        
        print("Thanks")
        break
    
    else:
        
        print("-----------------   Invalid Input   -----------------")