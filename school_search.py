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