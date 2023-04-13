import json
import os

def create(Name, Language, Filename):
    """
    Creates a profile with the given parameters.
    """
    try:
        os.chdir("./profiles")
        f = open("%s.json"%Name, "w")  

        profileparams = {
            "Name": Name,
            "Language": Language,
            "Filename": Filename
        }

        j = json.dumps(profileparams)

        print(f.write(j))
        return 0
    except:
        return 1    
def load(Name):
    """
    Reads a created profile
    """
    os.chdir("./profiles")
    f = open("%s.json"%Name, "r")
    profileparams = json.load(f.read())
    return profileparams

def delete(Name):
    try:
        os.chdir("./profiles")
        f = delete("%s.json"%Name)
        return 0
    except:
        return 1
    