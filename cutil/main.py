#imports necessary modules.
import platform, sys, os, subprocess
import logging
import argparse
import opt, splash, isadmin
import time

# create parser
parser = argparse.ArgumentParser()
 
# add arguments to the parser
parser.add_argument('-o', '--help')
 
# parse the arguments
args = parser.parse_args()

    
def helper():
    f = open("help.txt", 'r')
    filecontents = f.read()
    print(filecontents)
    f.close()
    
#if args.command == "help":
#    helper()
#    exit()

# defines end which prevents coloring the terminal and checks if it ran as admin.
end = "\033[0m"

#admin = isadmin()

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

#Splash line
splash.Splash(ver)

# Waits and cleans up the console
time.sleep(1.9)
clr = os.system('cls' if osname == 'Windows' else 'clear')

#Gets the name of the file that wants to be compiled
print("\033[1;36mPlease enter the file name you want to compile\033[32m")
filename = input("Filename: ")

print("\033[36m Please select the language the file is programmed in\033[33m")

print("1) C ")
print("2) C++")
print("3) Java")
print("4) Typescript")

opt = opt.getopt()


match opt:
    case 1:
        os.system("")
    case 2:
        os.system("")
print("\033[36mDo you want to execute the program?")
runfile = input("\033[32mY/n]")
if runfile == True:
    run = os.system("start {}" if osname == "Windows" else "./{}".format(filename, filename))





print(end)
