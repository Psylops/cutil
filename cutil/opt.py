import string
import keyboard

def getopt():
    """
    Gets keyboard input from the user and returns the value they entered.\n
    WARNING! This function only outputs numbers and doesn't allow letters.
    """
    alphabet = list(string.ascii_letters)
    while True:
        for letter in alphabet: # detect when a letter is pressed
            if keyboard.is_pressed(letter):
                print("\033[31mPlease enter a valid option")
                return Exception
        for num in range(10): # detect numbers 0-9
            if keyboard.is_pressed(str(num)):
                return str(num)