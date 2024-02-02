#!/usr/bin/env python
from Class_Handling.TEC_Class import TEC
# import Misc_Service


def create_teacher():
    first_name = input("Indtast lærerens fornavn: ")
    last_name = input("Indtast lærerens efternavn: ")
    try:
        TEC.create_teacher(first_name, last_name)
        # Misc_Service.wait_time("Læren blev oprettet.")
    except:
        # Misc_Service.wait_time("Der skete den fejl under oprettelse af læren...")    
        print("fail")

def update_teacher():
    print("update_teacher hit")
    
def list_teachers():
    print("list_teachers hit")