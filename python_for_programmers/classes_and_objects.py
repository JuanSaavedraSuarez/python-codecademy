class Dog:
    pass

pepper = Dog()
print(pepper)

class ClassSchedule:
    def __init__(self,course):
        self.course = course
    
    def __del__(self):
        print("Schedule deleted")

first = ClassSchedule('Math')
print(first.course)

sched = ClassSchedule('Chemistry')
del sched
