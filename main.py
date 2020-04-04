# ----------------------------------------------------------------------------
# This program creates a course registration system. It allows students to add # and drop courses. It also lists courses students are registered for.
# ----------------------------------------------------------------------------

import student


def main():
    # main function manages the registration program. There is no parameter. 
    #  main program creates lists for student login, class registration, class # sizes, and class roster lists

    student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
    course_list = ['CSC101', 'CSC102', 'CSC103']
    roster_list = [['1004', '1003'], ['1001'], ['1002']]
    max_size_list = [3, 2, 1]