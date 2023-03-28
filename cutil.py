#imports necessary modules and defines end.
import platform
import os
import subprocess
import time
import keyboard
import string
import datetime
end = "\033[0m"

osname = platform.system()

#A function to only get numbers and only one number
def getopt():
    alphabet = list(string.ascii_letters)
    while True:
        for letter in alphabet: # detect when a letter is pressed
            if keyboard.is_pressed(letter):
                print("Please enter a valid option")
        for num in range(10): # detect numbers 0-9
            if keyboard.is_pressed(str(num)):
                return str(num)
            
#checking if the terminal supports ansi
    
if osname == "Windows":
    from winreg import *
    try:
        #if it supports ansi it will continue forward
        key_to_read = r'Console'
        reg = ConnectRegistry(None, HKEY_CURRENT_USER)
        k = OpenKey(reg, key_to_read)

    except:
        #if not it will tweak it through the registry and advise the user to relaunch the console
        print("Creating registry key...")
        
        reg_key = OpenKey(
            HKEY_CURRENT_USER,
            r'Console',
            0, KEY_SET_VALUE)
        
        SetValueEx(reg_key,"VirtualTerminalLevel",0, REG_DWORD,1)
        
        print("Done")
        print("Please relaunch the console")
        time.sleep(2)
        exit()
#Version number
ver = "1.0"

# Startup Information
print("\033[1;35mCUtil version\033[34m",ver,"\033[35m Running on\033[34m",osname,"\033[35m Current Date:\033[34m",datetime.date.today(),"\033[35m.")

# Waits and cleans up the console
time.sleep(1.9)
test = os.system('cls' if osname == 'Windows' else 'clear')
print(test)
#Gets the name of the file that wants to be compiled
print("\033[1;36mPlease enter the file name you want to compile\033[32m")
filename = input("Filename: ")

print("\033[36m Please select the language the file is programmed in\033[33m")

print("1) C ")
print("2) C++")
print("3) Java")

opt = getopt()

print(end)