#!/usr/bin/env python
from Class_Handling.TEC_Class import TEC
from Class_Handling.Teacher_Class import Teacher
from Service.Misc_Service import wait_time, clear_console
from Service.Subject_Service import display_subjects, display_teachers_subjects, subjects_count
tec = TEC()

def create_teacher():
    clear_console()
    print("[OPRETTELSE AF LÆRER]\n")
    while True:
        first_name = input("Indtast lærerens fornavn: ").capitalize()
        last_name = input("Indtast lærerens efternavn: ").capitalize()
        subjects = pick_subjects()
        try:
            if tec.find_teachers(first_name + " " +last_name):
                wait_time("Læren er allerede oprettet. Prøv igen....")
                continue
            teacher = Teacher(first_name, last_name, subjects)
            tec.create_teacher(teacher)
            clear_console()
            wait_time(f"{first_name} blev oprettet...")
            return
        except:
            wait_time("Der skete den fejl under oprettelse af læren...")    

def update_teacher():
    clear_console()
    print("\n[OPDATERING AF LÆRER]")
    chosen_teacher = list_teachers(False)
    if chosen_teacher is None:
        return
    teacherObject = tec.find_teachers(chosen_teacher)
    if teacherObject:
        print(f'\n{chosen_teacher} er tilmeldt følgende fag:')
        display_teachers_subjects(teacherObject.subject)
        print(f'\n[1] Tilføj flere fag for {chosen_teacher}\n[2] Slet et fag')
        edit_choice = input("Vælg 1, eller 2: ")
        if edit_choice == '1':
            clear_console()
            subjects = display_subjects("edit")
            while True:
                chosen_subject = input("Vælg et fag fra listen: ")
                if chosen_subject in subjects_count():
                    if subjects[chosen_subject] in teacherObject.subject:
                        wait_time("\nFaget er allerede på listen...")
                    else:
                        teacherObject.add_subject(subjects[chosen_subject])
                        print(f'\nNuværende fag:')
                        display_teachers_subjects(teacherObject.subject)
                elif chosen_subject == '':
                    wait_time("Forlader... tilbage til main menuen")
                    return
                else:
                    wait_time("\nForket valg.. Prøv igen")
        elif edit_choice == '2':
            clear_console()
            print("[FJERN ET FAG]\n")
            current_subjects = display_teachers_subjects(teacherObject.subject)
            chosen_delete = input("Vælg et fag at fjerne: ")
            if chosen_delete in current_subjects:
                teacherObject.remove_subject(current_subjects[chosen_delete])
                wait_time("Faget er nu blevet slettet. Forlader....")
                return
            else:
                wait_time("Læren har ikke det fag. Prøv igen....")
    
def list_teachers(display_subjects):
    if display_subjects:
        clear_console()
    print("\n[LISTE AF ALLE LÆRER]")
    teachers_dict = {}
    index = 1
    if not tec.teachers:
        wait_time("Der er ingen lærerer!")
        return None
    for teacher in tec.teachers:
        print("\n")
        full_name = f"{teacher.firstname} {teacher.lastname}"
        print(f'[{index}] {full_name}')
        teachers_dict[str(index)] = full_name
        index += 1
        if display_subjects:
            display_teachers_subjects(teacher.subject)
    if not display_subjects:
        chosen_teacher = input("\nVælg en lærer fra listen: ")
        if chosen_teacher in teachers_dict:
            return teachers_dict[chosen_teacher]
        else:
            wait_time("Ingen lærer fundet med det nummer....")
    else:
        enter = input('\nTryk på [ENTER] for at forlade listen ')
        clear_console()
        wait_time("Forlader...")
    
def pick_subjects():
    chosen_subjects = []
    clear_console()
    subjects = display_subjects("create")
    while True:
        subject = input("Vælg et fag fra listen: ")
        if subject in subjects_count():
            if subjects[subject] in chosen_subjects:
                wait_time("\nFaget er allerede på listen...")
            else:
                chosen_subjects.append(subjects[subject])
                print(f'\nNuværende fag:')
                display_teachers_subjects(chosen_subjects)
        elif subject == '':
            clear_console()
            wait_time("Forlader... tilbage til main menuen")
            return chosen_subjects
        else:
            wait_time("\nForket valg.. Prøv igen")
                
