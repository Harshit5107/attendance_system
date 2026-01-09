#  Student Management 

# this is the feature detail od student management to user in short menu of student management
def student_management_menu():
    
    print("\n--------------------     Student Management     --------------------\n")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Profile Summary")
    print("7. Student Statistics")
    print("8. Back to Main Menu\n")
    
# this code is for the add new student and save that data in the student.txt file   
def add_student():
    
    s=int(input("\nEnter How Many Student You Want To Add :- "))
    print("\n\n")
    
    student_detail=open("data/students.txt","a")
    
    for i in range(0,s):
        
        id=input("Enter Student ID :- ")
        name=input("Enter Student Name :- ")
        Department=input("Enter Student Department :- ")
        semester=input("Enter Student Current Semester :- ")
        date_of_birth=input("Enter Birth Date (DD-MM-YYYY) :- ")
        gender=input("Enter Studnet Gender ( M / F / T ) :- ")
        contact_number=int(input("Enter Student Mobile Number :- "))
        email_id=input("Enter Student E-Mail ID :- ")
        admission_year=int(input("Enter Student Admission Year :- "))
        status=input("Enter Students Status ( Active / Inactive ) :- ")
        print("\n\n")
        
        
        
        student_detail.write(f"ID              :- {id}\n")
        student_detail.write(f"Name            :- {name}\n")
        student_detail.write(f"Department      :- {Department}\n")
        student_detail.write(f"semester        :- {semester}\n")
        student_detail.write(f"Date Of Birth   :- {date_of_birth}\n")
        student_detail.write(f"Gender          :- {gender}\n")
        student_detail.write(f"Contact Number  :- {contact_number}\n")
        student_detail.write(f"E-mail ID       :- {email_id}\n")
        student_detail.write(f"Addmisiion Year :- {admission_year}\n")
        student_detail.write(f"Status          :- {status}\n\n")
        
    student_detail.close()
    
    
# this code is for the view all student details to user
def view_students():
    
    display_student=open("data/students.txt","r")
    
    store_student_detail=display_student.read() #in this all data stores of student.txt and after it display it
    
    print(store_student_detail)
    
    
    
              
        
# this is the main code where the code starts when the main.py call it   
def student_management():
    
    while True:
        
        
        student_management_menu()
        n=int(input("Enter What You Want To Do              :- "))
        print("\n\n")
        
        if n==1:
            add_student()
        
        elif n==2:
            view_students()
            
            
        elif n==8:
            
            print("--------------   Thank You So Much   --------------  Back To Main Menu  --------------")
            break
        
        else:
            
            print("-----------------   Invalid Input   -----------------")
        
    
    