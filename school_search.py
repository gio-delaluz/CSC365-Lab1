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
            print(f"{row["StFirstName"]} {row["StLastName"]} is assigned to the class of {row["TFirstName"]} {row["TLastName"]}.")

def findGStudents(number: int, low=False, high=False):
    df_found = df_students[df_students["Grade"] == number]

    if df_found.empty:
        return
    else:
        if not low and not high:
            # '_' means ignore index
            for _, row in df_found.iterrows():
                print(f"{row["StFirstName"]} {row["StLastName"]} is in grade {row["Grade"]}.")
        elif low:
            # Row number of lowest GPA
            min = df_found["GPA"].idxmin()
            print(f"{df_found.loc[min, "StFirstName"]} {df_found.loc[min, "StLastName"]}, "
            f"who takes bus route {df_found.loc[min, "Bus"]}, is assigned to the class of "
            f"{df_found.loc[min, "TFirstName"]} {df_found.loc[min, "TLastName"]}. {df_found.loc[min, "StFirstName"]} "
            f"has a GPA of {df_found.loc[min, "GPA"]}.")
        elif high:
            # Row number of highest GPA
            max = df_found["GPA"].idxmax()
            print(f"{df_found.loc[max, "StFirstName"]} {df_found.loc[max, "StLastName"]}, "
            f"who takes bus route {df_found.loc[max, "Bus"]}, is assigned to the class of "
            f"{df_found.loc[max, "TFirstName"]} {df_found.loc[max, "TLastName"]}. {df_found.loc[max, "StFirstName"]} "
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
