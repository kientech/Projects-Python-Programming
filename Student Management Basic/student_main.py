from student_manegerment import Student

list_students = []

while True:
    print('''
        1. Add a new student
        2. Update information of students
        3. Delete student
        4. Find students
        5. Number of students
        6. Show information of all students
        7. Exit program
        ''')

    select = input("Enter feature, Please: ")

    if str(select).isdigit():
        select = int(select)
        if select == 1:
            id = int(input("Enter id student: "))
            name = input("Enter name student: ")
            student = Student(id, name)
            list_students.append(student)
        
        elif select == 2:
            id = int(input("Enter ID of Student you want to modify: "))
            for i in list_students:
                if i.get_id() == id:
                    i.set_name(input("Enter new name of student: "))
                    i.show_info()
                elif i.get_id() != id:
                    print(f"ID {id} isn't in the list students")
        
        elif select == 3:
            id = int(input("Enter ID you want to remove: "))
            for i in list_students:
                if i.get_id() == id:
                    list_students.remove(i)
            print("Removed Successfully")
            
        elif select == 4:
            id = int(input("Enter ID of student you want to find: "))
            
            for i in list_students:                  
                if i.get_id() == id:
                    print(f'ID {id} named {i.get_name()}')
            
        elif select == 5:
            print(f"\nThere are {len(list_students)} students")
        
        elif select == 6:
            if len(list_students) == 0:
                print("Please add student to the list!!!")
            else:
                print("Information of all students.")
                for i in list_students:
                    i.show_info()
                    print("---------")
                print(f"{len(list_students)} Students!")
        
        elif select == 7:
            print("EXITED!")
            break
    else:
        print("Plase enter again...")

        
