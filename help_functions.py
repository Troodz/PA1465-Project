import pickle
import hashlib
import os

def create_pickle(name, obj, platform):
        with open("unittest_pkl_files/" + name + "_" + platform + ".pkl", "wb") as f:
            pickle.dump(obj, f)
        
    
def read_pickle(name, platform):
    with open("unittest_pkl_files/" + name + "_" + platform + ".pkl", "rb") as f:
        temp_pick = f.read()
    hash = hashlib.sha256() #creates hash object
    hash.update(temp_pick) #insert obj into hash buffer
    hash.digest() #idk man
    f.close()
    return hash.hexdigest() # returns hashed pickle

def folder_contains_file(path, platform):
    try:
        files = os.listdir(path)
        for file in files:
            if platform in file:
                return True
        return False
    except FileNotFoundError:
        return False