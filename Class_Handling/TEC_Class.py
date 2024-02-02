from Class_Handling.Teacher_Class import Teacher

class TEC:
    def __init__(self):
        self.teachers = []

    def create_teacher(self, first_name, last_name):
        teacher = Teacher(first_name, last_name)
        self.teachers.append(teacher)

    def get_teacher_by_name(self, first_name, last_name):
        for teacher in self.teachers:
            if teacher.first_name == first_name and teacher.last_name == last_name:
                return teacher
        return None

    def update_teacher_subjects(self, teacher, subjects):
        teacher.subjects = subjects

    def remove_teacher(self, teacher):
        if teacher in self.teachers:
            self.teachers.remove(teacher)

    def get_all_teachers(self):
        return self.teachers
