from Class_Handling.Person_Class import Person
class Teacher(Person):
    def __init__(self, firstname, lastname, subject=[]):
        super().__init__(firstname, lastname)
        self.subject = subject

    def add_subject(self, new_subject):
        if new_subject not in self.subject:
            self.subject.append(new_subject)

    def remove_subject(self, subject):
        if subject in self.subject:
            self.subject.remove(subject)
