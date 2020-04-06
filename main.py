# ----------------------------------------------------------------------------
# This program creates a course registration system. It allows students to add # and drop courses. It also lists courses students are registered for.
# ----------------------------------------------------------------------------

import student


def main():
    # main function manages the registration program. There is no parameter.
    #  main program creates lists for student login, class registration, class # sizes, and class roster lists

    student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444')]
    course_list = ['CSC101', 'CSC102', 'CSC103']
    roster_list = [['1004', '1003'], ['1001'], ['1002']]
    max_size_list = [3, 2, 1]

    choice = 0
    while choice == 0:
        id = input("Enter student ID to log in, or 0 to quit: ")
        if id == '0':
            print("program exited")
            print()
            break
        else:
            # calls login function
            identify = login(id, student_list)
            # boolean if true
            if identify:
                print("login successful")
                choice = int(input(
                    "Enter 1 to add course, 2 to drop course, 3 to list current courses, 0 to exit program: "))
                while choice in (1, 2, 3):
                    if choice == 1:
                        # call add_course function from student.py
                        student.add_course(
                            id, course_list, roster_list, max_size_list)
                        choice = int(input(
                            "Enter 1 to add course, 2 to drop course, 3 to list current courses, 0 to exit program: "))

                    elif choice == 2:
                        # call drop_course function from student.py
                        student.drop_course(id, course_list, roster_list)
                        choice = int(input(
                            "Enter 1 to add course, 2 to drop course, 3 to list current courses, 0 to exit program: "))

                    elif choice == 3:
                        # call list_courses function from student.py
                        student.list_courses(id, course_list, roster_list)
                        choice = int(input(
                            "Enter 1 to add course, 2 to drop course, 3 to list current courses, 0 to exit program: "))
                if choice == 0:
                    print("session ended")
                    print()

            else:
                print("login credentials incorrect")
                print()


def login(id, s_list):

    #  --------------------------------------------------------------------------------------------------
    #  this function allows students to login. It has two parameters, s_list, which is the student list.
    #  If the ID and PIN combination is in # s_list login is successful and function returns True.
    #  Otherwise, display error message and return False.
    #  --------------------------------------------------------------------------------------------------

    password = input("Enter PIN: ")
    id_password = (id, password)
    if id_password in s_list:
        return True
    else:
        print("Incorrect PIN")
        return False


main()
