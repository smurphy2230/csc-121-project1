def add_course(id, c_list, r_list, m_list):

    #  -----------------------------------------------------------------------
    #  This function adds a student to a course. It has 4 parameters: id is the student ID,
    #  c_list is the course list, r_list is the #  #  roster list, m_list is the maximum class size list.
    #  _______________________________________________________________________

    course = input("Enter the course you want to add: ")
    course = course.upper()
    if course in c_list:
        course_index = c_list.index(course)
        if id in r_list[course_index]:
            print("You are already taking this course.")
            print()
        elif len(r_list[course_index]) == m_list[course_index]:
            print("This class is full.")
            print()
        else:
            r_list[course_index].append(id)
            print("Course successfully added")
            print()
    else:
        print("course not found")
        print()


def drop_course(id, c_list, r_list):

    #  --------------------------------------------------------------------
    #  This function drops a student from a course. It has 3 parameters: id is the student ID,
    #  c_list is the course list, r_list is the roster list.
    #  --------------------------------------------------------------------

    drop = input("Enter the course you want to drop: ")
    drop = drop.upper()
    if drop in c_list:
        drop_index = c_list.index(drop)
        if id in r_list[drop_index]:
            r_list[drop_index].remove(id)
            print("Course successfully dropped")
            print()
        else:
            print("You are not taking this course.")
            print()
    else:
        print("Course not found")
        print()


def list_courses(id, c_list, r_list):

    #  ------------------------------------------------------------------
    #  This function lists and counts the numbe of courses the student is registered for.
    #  It has 3 parameters: id is the student ID, c_list is the course list, r_list is the roster list.
    #  ------------------------------------------------------------------

    print("Courses registered for:")
    course_count = 0
    for i in range(len(r_list)):
        if id in r_list[i]:
            print(c_list[i])
            course_count += 1
    print("Number of classes registered for: ", course_count)
    print()
