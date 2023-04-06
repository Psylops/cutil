import json
import os

def create(Name, Language, Filename):
    """
    Creates a profile with the given parameters.
    """
    os.chdir("./profiles")
    f = open("{Name}.json", "w")  
    
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
    f = open("{Name}.json", "r")
    profileparams = json.load(f.read())
    return profileparams
    