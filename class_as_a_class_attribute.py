class Schedule:

    # initialize Schedule Class
    def __init__(self, period_1, period_2, period_3, period_4, period_5, period_6):
        self.period_1 = period_1
        self.period_2 = period_2
        self.period_3 = period_3
        self.period_4 = period_4
        self.period_5 = period_5
        self.period_6 = period_6

    def last_class(self):
        return f"The last class of the day is {self.period_6}."



class Student:

    #initialize class
    def __init__(self, id_number, first_name, last_name, gender, period_1, period_2, period_3, period_4, period_5, period_6):
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.schedule = Schedule(period_1, period_2, period_3, period_4, period_5, period_6)

    def print_name(self):
        return self.first_name


# New Student

brian = Student(123,"Brian","Murray","male", "Math","History","Science","English","IST","Study Hall")
print(brian.print_name())
print(brian.schedule.last_class())

# "Math","History","Science","English","IST","Study Hall")


