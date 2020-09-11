# This is an example of two separate objects (of the same class) sharing a different object (of a different class)

# the class the two objects will come from
# the two students will share the same course
class Student:

    def __init__(self, name, grade, course):
        self.name = name    # string
        self.grade = grade  # integer
        self.course = course  # Course object

    def __repr__(self):
        return f'My name is {self.name}.'
    
    def print_grade(self):
        return f'{self.name} is in grade {self.grade}.'


# Course class - both students will share an instance of the course class as their course
class Course:

    def __init__(self, name, chapters):
        self.name = name         # string
        self.chapters = chapters # integers

    def print_chapters(self):
        return f'{self.name} has {self.chapters} chapters'


# defining Algebra1 to be an instance of the course class
Algebra1 = Course("Algebra 1",6)

brian = Student("Brian", 9, Algebra1)
kyle = Student("Kyle", 10, Algebra1)

# both brian (Student) and kyle (Student) can access the properties from Algebra1 (Course)
print(brian.course.print_chapters())
print(kyle.course.print_chapters())

# an Algebra1 property changed by brian (Student) has also been changed for Kyle
brian.course.name = "Algebra 2"

print(kyle.course.name)  # Result = Algebra 2