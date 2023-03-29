#imports necessary modules and defines end.
import platform
import os
import logging
import subprocess
import cutil.opt as opt
import cutil.splash as splash

import time
end = "\033[0m"

#TODO add daemon mode where it will compile after detecting file changes.
#TODO add ability to make and read profiles for different files.
#TODO add logging and save it in a temporary place
#TODO add the ability to update itself
#TODO also finish it

osname = platform.system()
            
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

splash.Splash(ver)

# Waits and cleans up the console
time.sleep(1.9)
test = os.system('cls' if platform.system() == 'Windows' else 'clear')

#Gets the name of the file that wants to be compiled
print("\033[1;36mPlease enter the file name you want to compile\033[32m")
filename = input("Filename: ")

print("\033[36m Please select the language the file is programmed in\033[33m")

print("1) C ")
print("2) C++")
print("3) Java")

opt = opt.getopt()

print(end)