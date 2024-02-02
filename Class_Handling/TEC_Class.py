from Class_Handling.Teacher_Class import Teacher

class TEC:
    def __init__(self):
        self.teachers = []

    def create_teacher(self, teacher):
        self.teachers.append(teacher)

    def find_teachers(self, fullname):
        firstname, lastname = fullname.split(' ', 1)
        for teacher in self.teachers:
            if teacher.firstname == firstname and teacher.lastname == lastname:
                return teacher
        return None
