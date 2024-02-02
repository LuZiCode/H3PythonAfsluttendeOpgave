#!/usr/bin/env python
# from Service.Teacher_Service import create_teacher, update_teacher, list_teachers
from Service.Teacher_Service import create_teacher, update_teacher, list_teachers
# from Service.Misc_Service import clear_console, exit_program, wait_time
from Service.Misc_Service import clear_console, exit_program, wait_time

def main():
    while True:
        # clear_console()
        print('[1] Opret lærer\n[2] Opdater lærer\n[3] Vis liste af alle lærer\n[4] Exit')
        choice = input("Vælg 1, 2, 3 eller 4: ")
        if choice in ['1', '2', '3', '4']:
            handle_choice(choice)
        else:
            wait_time("Forkert valg.. Prøv igen.....")
            
            
def handle_choice(option):
    options = {
        '1' : create_teacher,
        '2' : update_teacher,
        '3' : list_teachers,
        '4' : exit_program
    }
    try:
        options[option]()
    except ModuleNotFoundError:
        print("Metoden kunne ikke findes??....")


if __name__ == "__main__":
    main()