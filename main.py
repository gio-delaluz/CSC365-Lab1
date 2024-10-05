from school_search import *

def printQueryCommands():
    print("\t• S[tudent]: <lastname> [B[us]]\n\t• T[eacher]: <lastname>\n\t• B[us]: <number>\n\t• G[rade]: <number> [H[igh]|L[ow]]\n\t• A[verage]: [<N[umber]><T[eacher]><B[us]><A[ll]>]\n\t• C[lassroom]: <Number> T[eacher]\n\t• I[nfo]\n\t• Q[uit]")

def errorCheck():
    print("That didn't seem to work. Try one of these queries:")
    printQueryCommands()

def check_if_int(value: str) -> int:
    try:
        return int(value)
    except:
        errorCheck()
        return None

def sourceQuery(user_query: str) -> bool:

    query = user_query.split()
    query_len = len(query)
    
    if query_len == 0:
        return True
    
    student_options = {"S", "S:", "Student", "Student:"}
    bus_options = {"B", "B:", "Bus", "Bus"}
    teacher_options = {"T", "T:", "Teacher", "Teacher:"}
    grade_options = {"G", "G:", "Grade", "Grade:"}
    avg_options = {"A", "A:", "Average", "Average:"}
    class_options = {"C", "C:", "Classroom", "Classroom:"}

    low_flags = {"L", "Low"}
    high_flags = {"H", "High"}
    info_options = {"I", "Info"}
    quit_options = {"Q", "Quit"}
    enrollment_options = {"E", "Enrollment"}


    if query[0] in student_options:
        if query_len == 2:
            lastname = query[1].upper()
            searchStudent(lastname)
            return True

        # S[tudent]: <lastname> [B[us]]
        elif query_len == 3:
            if query[2] in bus_options:
                lastname = query[1].upper()
                searchStudent(lastname, True)
                return True
            else:
                errorCheck()
                return True
        else:
            errorCheck()
            return True
    # T[eacher]: <lastname>
    elif query[0] in teacher_options:
        if query_len == 2:
            lastname = query[1].upper()
            findTStudents(lastname)
            return True
        else:
            errorCheck()
            return True
    # G[rade]: <Number>
    elif query[0] in grade_options:
        if query_len == 2:
            grade_number = check_if_int(query[1])
            if grade_number is not None:
                findGStudents(grade_number)
            return True
        elif query_len == 3:
            grade_number = check_if_int(query[1])
            if grade_number is not None:
                if query[2] in low_flags:
                    findGStudents(grade_number, True, False)
                elif query[2] in high_flags:
                    findGStudents(grade_number, False, True)
                # G[rade]: <Number> [T[eacher]]
                elif query[2] in teacher_options:
                    findGradeTeachers(grade_number)
                else:
                    errorCheck() # check if this works properly
            return True
        else:
            errorCheck()
            return True
    # A[verage]: [<N[umber]><T[eacher]><B[us]><A[ll]>]
    elif query[0] in avg_options:
        if query_len == 2:
            if query[1] in {"Teacher", "T"}:
                calcAvgGPA_Teacher()
            elif query[1] in {"Bus", "B"}:
                calcAvgGPA_Bus()
            else:
                grade_number = check_if_int(query[1])
                if grade_number is not None:
                    calcAvgGPA_Grade(grade_number)
            return True
        else:
            errorCheck()
        return True
    # B[us] <Number>
    elif query[0] in bus_options:
        if query_len == 2:
            bus_number = check_if_int(query[1])
            if bus_number is not None:
                findBus(bus_number)
            return True
        else:
            errorCheck()
            return True
    # C[lassroom]: <Number> T[eacher]
    elif query[0] in class_options:
        if query_len == 2:
            grade_level = check_if_int(query[1])
            if grade_level is not None:
                findClassroomStudents(grade_level)
            return True
        elif query_len == 3:
            grade_level = check_if_int(query[1])
            if grade_level is not None:
                if query[2] == 'T' or query[2] == 'Teacher':
                    findClassroomTeachers(grade_level)
                else:
                    errorCheck() # check if this works properly
            return True
        else:
            errorCheck()
            return True
    elif query[0] in enrollment_options:
        if query_len == 1:
            getEnrollment()
            return
        else:
            errorCheck()
            return True
    elif query[0] in info_options:
        if query_len == 1:
            getInfo()
            return True
        else:
            errorCheck()
            return True
    elif query[0] in quit_options:
        if query_len == 1:
            return False
        else:
            errorCheck()
            return True
    else:
        return True

def main():
    flag = True
    # Exit program if incorrect number of columns in text file
    if check_cols():
        while flag:
            query = input("Enter command: ")
            flag = sourceQuery(query)

if __name__ == "__main__":
    main()