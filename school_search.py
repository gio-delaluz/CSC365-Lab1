import pandas as pd

df_students = pd.read_csv("list.txt", sep=",", header=None,
            names=["StLastName", "StFirstName", "Grade", "Classroom","Bus", "GPA"])

df_teachers = pd.read_csv("teachers.txt", sep=",", header=None, 
            names=['TLastName', 'TFirstName', 'Classroom'])

# Convert Grade, Classroom, and Bus into categorical variables
df_students['Grade'] = df_students['Grade'].astype('category')
df_students['Classroom'] = df_students['Classroom'].astype('category')
df_students['Bus'] = df_students['Bus'].astype('category')

def check_cols():
    if len(df_students.columns) != 6 or len(df_teachers.columns) != 3:
        return False
    
    # df_students['Grade Level'] = df_students['Grade'].apply(convert_grade_to_level)
    return True

# def convert_grade_to_level(grade):
    # if grade == 0:
    #     return 'kindergarten'
    # elif 1 <= grade <= 5:
    #     return 'elementary school'
    # elif 6 <= grade <= 8:
    #     return 'middle school'
    # elif 9 <= grade <= 12:
    #     return 'high school'
    # else:
    #     return 'unknown'

def searchStudent(lastname: str, bus=False):
    df_found = df_students[df_students["StLastName"] == lastname]
    
    if df_found.empty:
        print(f"No student found with the last name {lastname.lower().capitalize()}.")
        return
    else:
        # '_' means ignore index
        for _, row in df_found.iterrows():
            student_name = f"{row['StFirstName'].lower().capitalize()} {row['StLastName'].lower().capitalize()}"
            if bus:
                if row['Bus'] == 0:
                    print(f"{student_name} does not ride the bus to school.")
                else:
                    print(f"{student_name}, who takes bus route {row['Bus']}.")
            else:
                if row['Grade'] == 0:
                    grade = "Kindergarten"
                else:
                    grade = f"Grade {row['Grade']}"

                df_teacher = df_teachers[df_teachers['Classroom'] == row['Classroom']]
                teacher = df_teacher.iloc[0]
                teacher_name = f"{teacher['TFirstName'].lower().capitalize()} {teacher['TLastName'].lower().capitalize()}"
                print(f"{student_name} is a {grade} student assigned to the class of {teacher_name}.")

def findTStudents(lastname: str):
    # Find the teacher by last name
    df_found = df_teachers[df_teachers["TLastName"] == lastname]

    # Check if the teacher is found
    if df_found.empty:
        print(f"No teacher found with the last name {lastname.lower().capitalize()}.")
        return

    # For each teacher found (in case of duplicates)
    for _, teacher_row in df_found.iterrows():
        teacher_name = f"{teacher_row['TFirstName'].lower().capitalize()} {teacher_row['TLastName'].lower().capitalize()}"
        classroom = teacher_row['Classroom']

        # Find students assigned to this teacher's classroom
        students_in_class = df_students[df_students['Classroom'] == classroom]

        if students_in_class.empty:
            print(f"No students found for instructor {teacher_name} in classroom {classroom}.")
        else:
            print(f"Students assigned to instructor {teacher_name} in classroom {classroom}:")
            for _, student_row in students_in_class.iterrows():
                student_name = f"{student_row['StFirstName'].lower().capitalize()}  {student_row['StLastName'].lower().capitalize()}"
                print(f"\t{student_name}")

def findGStudents(number: int, low=False, high=False):
    df_found = df_students[df_students["Grade"] == number]
    if number == 0:
        grade = "Kindergarten"
    else:
        grade = f"Grade {number}"

    if df_found.empty:
        print(f'No student found with the grade {number}')
        return
    else:
        if not low and not high:
            # '_' means ignore index
            for _, row in df_found.iterrows():
                student_name = f"{row['StFirstName'].lower().capitalize()} {row['StLastName'].lower().capitalize()}"
                print(f"{student_name} is in {grade}.")
        elif low:
            # Row number of lowest GPA
            min = df_found["GPA"].idxmin()

            student_first = f"{df_found.at[min, "StFirstName"].lower().capitalize()}"
            student_last = f"{df_found.at[min, "StLastName"].lower().capitalize()}"

            df_teacher = df_teachers[df_teachers['Classroom'] == df_found.at[min, "Classroom"]]
            teacher = df_teacher.iloc[0]
            teacher_name = f"{teacher['TFirstName'].lower().capitalize()} {teacher['TLastName'].lower().capitalize()}"

            print(f"{student_first} {student_last}, "
            f"who takes bus route {df_found.at[min, "Bus"]}, is assigned to the class of "
            f"{teacher_name}. {student_first} "
            f"has a GPA of {df_found.at[min, "GPA"]}.")
        elif high:
            # Row number of highest GPA
            max = df_found["GPA"].idxmax()

            student_first = f"{df_found.at[max, "StFirstName"].lower().capitalize()}"
            student_last = f"{df_found.at[max, "StLastName"].lower().capitalize()}"
            
            df_teacher = df_teachers[df_teachers['Classroom'] == df_found.at[max, "Classroom"]]
            teacher = df_teacher.iloc[0]
            teacher_name = f"{teacher['TFirstName'].lower().capitalize()} {teacher['TLastName'].lower().capitalize()}"

            print(f"{student_first} {student_last}, "
            f"who takes bus route {df_found.at[max, "Bus"]}, is assigned to the class of "
            f"{teacher_name}. {student_first} "
            f"has a GPA of {df_found.at[max, "GPA"]}.")

def findBus(busNum: int):
    df_found = df_students[df_students['Bus'] == busNum]

    if df_found.empty:
        print(f'No student found on Bus #{busNum}')
        return
    
    else:
        for _, row in df_found.iterrows():
            if row['Grade'] == 0:
                grade = "Kindergarten"
            else:
                grade = f"Grade {row['Grade']}"

            student_name = f"{row['StFirstName'].lower().capitalize()} {row['StLastName'].lower().capitalize()}"
            print(f'{student_name} is a {grade} student assigned to classroom {row['Classroom']}.')

def findClassroomStudents(class_num: int):
    df_found = df_students[df_students['Classroom'] == class_num]

    if df_found.empty:
        print(f'No student(s) found in Classroom #{class_num}')
        return
    else:
        print(f'Students in Classroom #{class_num}')
        for _, row in df_found.iterrows():
            student_name = f"{row['StFirstName'].lower().capitalize()} {row['StLastName'].lower().capitalize()}"
            print(f'\t{student_name}')

def findClassroomTeachers(class_num: int):
    df_found = df_teachers[df_teachers["Classroom"] == class_num]

    if df_found.empty:
        print(f'No teacher(s) found for Classroom #{class_num}')
        return
    else:
        print(f'Teacher(s) of Classroom #{class_num}')
        for _, row in df_found.iterrows():
            teacher_name = f"{row['TFirstName'].lower().capitalize()} {row['TLastName'].lower().capitalize()}"
            print(f'\t{teacher_name}')

def findGradeTeachers(number: int):
    df_found = df_students[df_students["Grade"] == number]

    if number == 0:
        grade = "Kindergarten"
    else:
        grade = f"Grade {number}"

    if df_found.empty:
        print(f"No teacher(s) found for {grade}")
        return

    df_filtered = df_found.drop_duplicates(subset="Classroom")

    print(f"Teachers for {grade}:")
    for _, row in df_filtered.iterrows():
        # print(type(row))
        temp = df_teachers[df_teachers["Classroom"] == row["Classroom"]]
        for _, trow in temp.iterrows():
            teacher_name = f"{trow["TFirstName"].lower().capitalize()} {trow["TLastName"].lower().capitalize()}"
            print(f"\t- {teacher_name}")


def calcAvgGPA_Grade(number: str):
    df_found = df_students[df_students["Grade"] == number]
    if number == 0:
        grade = "Kindergarten"
    else:
        grade = f"Grade {number}"

    if df_found.empty:
        return
    else:
        total = 0
        num_rows = len(df_found.index)
        # '_' means ignore index
        for _, row in df_found.iterrows():
            total += row["GPA"]
        avg = total / num_rows
        # .2f formats to 2 decimal places
        print(f"{grade} has average GPA of %.2f." % (avg))

def calcAvgGPA_Teacher():
    merged_df = pd.merge(df_students, df_teachers, on="Classroom")
    grouped = merged_df.groupby(["TFirstName", "TLastName"], observed=False)["GPA"].agg(['mean', 'count'])
    grouped = grouped.sort_values(by='mean', ascending=True)
    print("Avg. Class GPA by Teacher:")

    for (tfirst, tlast), row in grouped.iterrows():
        teacher_name = f"{tfirst.capitalize()} {tlast.capitalize()}"
        print(f"\t{teacher_name} -- Avg. GPA: {row['mean']:.2f} -- Total: {row['count']:.0f}")

def calcAvgGPA_Bus():
    # Group by bus route, calculate average GPA and count of students
    grouped = df_students.groupby("Bus", observed=False).agg(avg_GPA=('GPA', 'mean'), count=('GPA', 'size'))
    
    # Sort the grouped DataFrame by average GPA in ascending order
    grouped = grouped.sort_values(by='avg_GPA', ascending=True)
    
    # Print the average GPA by bus route, formatted similarly to the teacher function
    print("Avg. Class GPA by Bus Route:")
    for bus, row in grouped.iterrows():
        print(f"\tBus Route {bus} -- Avg. GPA: {row['avg_GPA']:.2f} -- Total: {row['count']:.0f}")


def getEnrollment():
    try:
        print("Classroom Enrollment Status:")
        # Enrollment by classroom using groupby
        enrollment_by_classroom = df_students.groupby("Classroom", observed=False).size().sort_index()
        for classroom, count in enrollment_by_classroom.items():
            print(f"\tRoom #{classroom}: {count}")
    except:
        print("Encountered an error.")
        
def getInfo():
    num_grades = 7
    for i in range(num_grades): 
        try:
            total = df_students.groupby('Grade', observed="False").size()[i]
            print(f"{i}: {total}")
        # If the value (grade) doesn't exist, a there will be a
        # key error
        except KeyError:
            print(f"{i}: 0")