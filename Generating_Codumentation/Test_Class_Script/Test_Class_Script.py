"""
Script to start app
"""
from Student import Student
from Team import Team

if __name__ == '__main__':
    team = Team("Red")
    student = Student("Giorgio", 18)
    team.add_member(student)
    for member in team.members:
        print(member.name)
        print(member.age)
