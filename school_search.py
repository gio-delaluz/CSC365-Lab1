import pandas as pd

df_students = pd.read_csv("students.txt", sep=",", header=None,
            names=["StLastName", "StFirstName", "Grade", "Classroom","Bus", "GPA", "TLastName", "TFirstName"])

def searchStudent(lastname: str, bus=False):
    df_found = df_students[df_students["StLastName"] == lastname]
    
    if df_found.empty:
        return
    else:
        # '_' means ignore index
        for _, row in df_found.iterrows():
            if bus:
                print(f"{row["StFirstName"]} {row["StLastName"]}, who takes bus route {row["Bus"]}.")
            else:
                print(f"{row["StFirstName"]} {row["StLastName"]} is a {row["Grade"]} student assigned to the class of {row["TFirstName"]} {row["TLastName"]}.")

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
            