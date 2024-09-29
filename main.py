from school_search import findStudents

def printQueryCommands():
    print("\t• S[tudent]: <lastname> [B[us]]\n\t• T[eacher]: <lastname>\n\t• B[us]: <number>\n\t• G[rade]: <number> [H[igh]|L[ow]]\n\t• A[verage]: <number>• I[nfo]\n\t• Q[uit]")

def sourceQuery(user_query: str) -> bool:
    query = user_query.split()
    len(query)
    
    if len(query) == 0:
        return True
    
    student_options = {"S:", "Student:"}
    bus_options = {"B", "Bus"}

    if query[0] in student_options:
        if len(query) == 2:
            lastname = query[1].upper()
            findStudents(lastname)
            return True

        elif len(query) == 3:
            if query[2] in bus_options:
                lastname = query[1].upper()
                findStudents(lastname, True)
                return True
            else:
                print("That didn't seem to work. Try one of these queries:")
                printQueryCommands()
                return True
        else:
            print("That didn't seem to work. Try one of these queries:")
            printQueryCommands()
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