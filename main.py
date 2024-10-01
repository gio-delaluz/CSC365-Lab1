from school_search import *

def printQueryCommands():
    print("\t• S[tudent]: <lastname> [B[us]]\n\t• T[eacher]: <lastname>\n\t• B[us]: <number>\n\t• G[rade]: <number> [H[igh]|L[ow]]\n\t• A[verage]: <number>• I[nfo]\n\t• Q[uit]")

def errorCheck():
    print("That didn't seem to work. Try one of these queries:")
    printQueryCommands()

def sourceQuery(user_query: str) -> bool:
    query = user_query.split()
    query_len = len(query)
    
    if query_len == 0:
        return True
    
    student_options = {"S", "Student"}
    bus_options = {"B", "Bus",}
    teacher_options = {"T", "Teacher"}
    grade_options = {"G", "Grade"}
    low_flags = {"L", "Low"}
    high_flags = {"H", "High"}
    avg_options = {"A", "Average"}
    info_options = {"I", "Info"}

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
            findGStudents(int(query[1]))
            return True
        elif query_len == 3:
            if query[2] in low_flags:
                findGStudents(int(query[1]), True, False)
            elif query[2] in high_flags:
                findGStudents(int(query[1]), False, True)
            else:
                errorCheck()
            return True
        else:
            errorCheck()
            return True
    # A[verage]: <Number>
    elif query[0] in avg_options:
        if query_len == 2:
            calcAvgGPA(int(query[1]))
            return True
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
    elif query[0] == "Q":
        return False
    
    else:
        return True

def main():
    flag = True
    while flag:
        query = input("Enter command: ")
        flag = sourceQuery(query)

if __name__ == "__main__":
    main()