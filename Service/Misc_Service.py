#!/usr/bin/env python
import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def exit_program():
    clear_console()
    wait_time("Programmet lukkes....")
    time.sleep(1)
    exit()
    
def wait_time(prompt):
    print(f'\n{prompt}')
    time.sleep(1)
    
def main_menu_count():
    return ['1', '2', '3', '4']