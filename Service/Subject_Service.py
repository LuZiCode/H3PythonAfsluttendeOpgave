#!/usr/bin/env python

def display_subjects(caller):
    subjs = get_subjects()
    titles = {
        "create": "[VALG AF FAG TIL LÆRER]\n",
        "edit": "[TILFØJ ET NYT FAG TIL LÆREN]\n",
    }
    action = titles.get(caller, "[HANDLING]\n")
    print(action)
    for index, key in enumerate(subjs, start=1):
        print(f'[{index}] {subjs[key]}')
    print('\n[EFTERLAD BLANK FOR AT AFSLUTTE]')
    return subjs
        

def get_subjects():
    subjects = {
        '1' : 'IoT Embedded',
        '2' : 'Python',
        '3' : 'BigData 1',
        '4' : 'Softwaresikkerhed og test',
        '5' : 'Serversideprogrammering'
    }
    return subjects

def display_teachers_subjects(subjectsObject):
    index = 1
    subjects_dict = {}
    for subject in subjectsObject:
        print(f'\t- [{index}] {subject}')
        subjects_dict[str(index)] = subject
        index += 1
    return subjects_dict
        
def subjects_count():
    return ['1', '2', '3', '4', '5']