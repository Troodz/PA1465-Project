import pickle 
import subprocess
import os
import unittest
import random
import hashlib
import math
test_dir = "tests/"

class version_check:
    def __init__(self) -> None:
        self.value = ()



class test_program(unittest.TestCase):

    def create_pickle(self,name, obj):
        with open(name + ".pkl", "wb") as f:
            pickle.dump(obj, f)
        
    
    def read_pickle(self, name):
        with open(name+".pkl", "rb") as f:
            temp_pick = f.read()
        hash = hashlib.sha256() #creates hash object
        hash.update(temp_pick) #insert obj into hash buffer
        hash.digest() #idk man
        f.close()
        return hash.hexdigest() # returns hashed pickle

    def load_pickle(self, obj):
        return pickle.loads(obj)

    #Different tests
    def test_different_version(self):
        test_object = ()
        path = r"C:\Users\koffe\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python3.9.exe"
        subprocess.run([path, test_dir+"version_check.py"])
        
        self.create_pickle("ver3.10", test_object)
        self.assertEqual(self.read_pickle("ver3.10"), self.read_pickle("ver3.9"))

    def test_zero_tuple(self):
        test_object = ()
        self.create_pickle("zero_tuple1",test_object)
        self.create_pickle("zero_tuple2",test_object)
        self.assertEqual(self.read_pickle("zero_tuple1"),self.read_pickle("zero_tuple2"))
    
    def test_special_char(self):
        test_object = "teståäö"
        self.create_pickle("special1",test_object)
        self.create_pickle("special2",test_object)
        self.assertEqual(self.read_pickle("special1"),self.read_pickle("special2"))
    
    def test_float(self):
        test_object = math.pi
        self.create_pickle("float1",test_object)
        self.create_pickle("float2",test_object)
        self.assertEqual(self.read_pickle("float1"),self.read_pickle("float2"))
   
    def test_nan(self):
        test_object = math.nan #would also work with float('nan')
        self.create_pickle("nan1",test_object)
        self.create_pickle("nan2",test_object)
        obj1 = self.read_pickle("nan1")
        obj2 = self.read_pickle("nan2")
        self.assertEqual(obj1,obj2)
    
    def test_inf(self):
        test_object = math.inf
        self.create_pickle("inf1",test_object)
        self.create_pickle("inf2",test_object)
        obj1 = self.read_pickle("inf1")
        obj2 = self.read_pickle("inf2")
        self.assertEqual(obj1,obj2)
        
if __name__ == '__main__':
    unittest.main()
    