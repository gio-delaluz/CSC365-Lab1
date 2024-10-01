import pandas as pd

df_students = pd.read_csv("students.txt", sep=",", header=None,
            names=["StLastName", "StFirstName", "Grade", "Classroom","Bus", "GPA", "TLastName", "TFirstName"])

# Convert Grade, Classroom, and Bus into categorical variables
df_students['Grade'] = df_students['Grade'].astype('category')
df_students['Classroom'] = df_students['Classroom'].astype('category')
df_students['Bus'] = df_students['Bus'].astype('category')

def convert_grade_to_level(grade):
    if 0 <= grade <= 5:
        return 'kindergarten'
    elif 6 <= grade <= 8:
        return 'middle school'
    elif 9 <= grade <= 12:
        return 'high school'
    else:
        return 'unknown'
    
df_students['Grade Level'] = df_students['Grade'].apply(convert_grade_to_level)

def searchStudent(lastname: str, bus=False):
    df_found = df_students[df_students["StLastName"] == lastname]
    
    if df_found.empty:
        return
    else:
        # '_' means ignore index
        for _, row in df_found.iterrows():
            student_name = f"{row['StFirstName'].lower().capitalize()} {row['StLastName'].lower().capitalize()}"
            if bus:
                print(f"{student_name}, who takes bus route {row['Bus']}.")
            else:
                teacher_name = f"{row['TFirstName'].lower().capitalize()} {row['TLastName'].lower().capitalize()}"
                print(f"{student_name} is a {row['Grade Level']} student assigned to the class of {teacher_name}.")

def findTStudents(lastname: str):
    df_found = df_students[df_students["TLastName"] == lastname]

    if df_found.empty:
        return
    else:
        # '_' means ignore index
        for _, row in df_found.iterrows():
            student_name = f"{row['StFirstName'].lower().capitalize()} {row['StLastName'].lower().capitalize()}"
            teacher_name = f"{row['TFirstName'].lower().capitalize()} {row['TLastName'].lower().capitalize()}"
            print(f"{student_name} is assigned to the class of {teacher_name}.")

def findGStudents(number: int, low=False, high=False):
    df_found = df_students[df_students["Grade"] == number]

    if df_found.empty:
        return
    else:
        if not low and not high:
            # '_' means ignore index
            for _, row in df_found.iterrows():
                student_name = f"{row['StFirstName'].lower().capitalize()} {row['StLastName'].lower().capitalize()}"
                print(f"{student_name} is in grade {row["Grade"]}.")
        elif low:
            # Row number of lowest GPA
            min = df_found["GPA"].idxmin()

            student_first = f"{df_found.loc[min, "StFirstName"].lower().capitalize()}"
            student_last = f"{df_found.loc[min, "StLastName"].lower().capitalize()}"
            teacher_name = f"{df_found.loc[min, "TFirstName"].lower().capitalize()} {df_found.loc[min, "TLastName"].lower().capitalize()}"

            print(f"{student_first} {student_last}, "
            f"who takes bus route {df_found.loc[min, "Bus"]}, is assigned to the class of "
            f"{teacher_name}. {student_first} "
            f"has a GPA of {df_found.loc[min, "GPA"]}.")
        elif high:
            # Row number of highest GPA
            max = df_found["GPA"].idxmax()

            student_first = f"{df_found.loc[max, "StFirstName"].lower().capitalize()}"
            student_last = f"{df_found.loc[max, "StLastName"].lower().capitalize()}"
            teacher_name = f"{df_found.loc[max, "TFirstName"].lower().capitalize()} {df_found.loc[max, "TLastName"].lower().capitalize()}"

            print(f"{student_first} {student_last}, "
            f"who takes bus route {df_found.loc[max, "Bus"]}, is assigned to the class of "
            f"{df_found.loc[max, "TFirstName"]} {df_found.loc[max, "TLastName"]}. {student_first} "
            f"has a GPA of {df_found.loc[max, "GPA"]}.")

def calcAvgGPA(number: str):
    df_found = df_students[df_students["Grade"] == number]

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
        print(f"Grade %d has average GPA of %.2f." % (number, avg))

def getInfo():
    num_grades = 7
    for i in range(num_grades): 
        try:
            total = df_students.groupby('Grade', observed="False").size()[i]
            print(f"%d: %d" % (i, total))
        # If the value (grade) doesn't exist, a there will be a
        # key error
        except KeyError:
            print(f"%d: 0" % i)