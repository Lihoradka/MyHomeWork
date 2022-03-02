class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []
        self.lecture_estimation = []
    def rate_lc(self, lecturer, lecture, grade):
        if isinstance(lecturer, Lecturer) and lecture in self.lecture_estimation and lecture in lecturer.courses_attached:
            if lecture in lecturer.grades:
                lecturer.grades[lecture] += [grade]
            else:
                lecturer.grades[lecture] = [grade]
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, Python=9.9, Git=9.9, Start_coding=9.9):
        self.lecture_in_progress = []
        self.grades = []
        self.Python = Python
        self.Git = Git
        self.Start_coding = 'Введение в программирование'
        self.courses_attached = []
        self.name = []
        self.surname = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        self.name = Some
        self.surname = Buddy
    def __str__(self):
        return 'Имя: '+self.name,'Фамилия: '+self.surname
    some_reviewer =  Reviewer() 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

best_lecturer = Lecturer('Some', 'Buddy')
#best_lecturer.courses_attached = Student.courses_attached

#cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
print(best_student.grades)
print(some_reviewer)