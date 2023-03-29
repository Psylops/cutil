import platform
import datetime
import os
import time

def Splash(ver):
    """
    A simple TUI splash function that can be used to display info\n   about the system, Program version and Date and time.
    """
    print("\033[1;35mCUtil version\033[34m",ver,"\033[35m Running on\033[34m",platform.system(),"\033[35m Current Date:\033[34m",datetime.date.today(),"\033[35m.")
