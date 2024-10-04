## Project Setup
- Virtual Environment
- python -m venv .venv (Windows) // python3 -m venv .venv (MacOS)
- venv\Scripts\activate (Windows) // source .venv/bin/activate (MacOS)
- (venv) pip install pandas → added to virtual environment folder
- python main.py (Windows)  // python3 main.py (MacOS)
- can now query for commands*
- Deactivate

## New Commands
- C[lassroom] <Number> [T[eacher]]: Given a classroom number, returns a list
of all students assigned to it. If also given the teacher option, it will instead return the teacher(s) teaching in it.
- G[rade] <Number> [T[eacher]]: Given a grade, returns a list of all students in that grade. Given the additional teacher option, returns a list of all teachers that teach that grade.
- E[nrollment]: Returns a list of all classrooms in ascending order followed by total student enrollment in that classroom.