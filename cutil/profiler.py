import json
import os

def create(Name, Language, Filename):
    """
    Creates a profile with the given parameters.
    """
    os.chdir("./profiles")
    f = open("%s.json"%Name, "w")  
    
    profileparams = {
        "Name": Name,
        "Language": Language,
        "Filename": Filename
    }
    
    j = json.dumps(profileparams)
    
    print(f.write(j))
    
def load(Name):
    """
    Reads a created profile
    """
    os.chdir("./profiles")
    f = open("%s.json"%Name, "r")
    profileparams = json.load(f.read())
    return profileparams
create("Test", 'C', "test.txt")