# Public access modifier
# By default, all members within a class are public
class ClassSchedule:
    def __init__(self, course, instructor):
        self.course = course
        self.instructor = instructor

    def display_course(self):
        print(f'Course: {self.course}, Instructor: {self.instructor}')

sched = ClassSchedule('Chemistry', 'Mr. Doe')
sched.display_course()
sched.course

# Protected access modifier
# denoted by prefix _ prevent members from being accessed outside the class, except from subclass
class ClassScheduleProtected:
    def __init__(self, course, instructor):
        self._course = course
        self._instructor = instructor

    def display_course(self):
        print(f'Course: {self._course}, Instructor: {self._instructor}')

sched_prot = ClassScheduleProtected('Biology', 'Mx. Smith')
sched_prot.display_course()

# Private access modifier
# dentoed by __ declare members to be only accesible within the class. 
class ClassSchedulePrivate:
    def __init__(self, course, instructor):
        self.__course = course # private
        self.__instructor = instructor # private

    def display_course(self):
        print(f'Course: {self.__course}, Instructor: {self.__instructor}')

sched_priv = ClassSchedulePrivate('Biology', 'Ms. Smith')
 
sched_priv.__course # this will throw an Attribute Error because we're trying to access a private member
 
sched_priv.display_course() # this won't throw an Attribute Error because this method is public