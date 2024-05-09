import os
import unittest
import math
from decimal import *
from help_functions import create_pickle, read_pickle, folder_contains_file

test_dir = "tests/"
platform = "windows"

class version_check:
    def __init__(self) -> None:
        self.value = ()



class TestPickleLibrary(unittest.TestCase):

    def test_import_pickle(self):
        try:
            import pickle
        except ImportError:
            self.fail("Could not import pickle")

    def test_zero_tuple(self):
        test_object = ()
        create_pickle("zeroTuple",test_object, platform)
        try:
            read_pickle("zeroTuple", platform)
        except Exception as e:
            self.fail(e)
        
    
    def test_special_char(self):
        test_object = "teståäö"
        create_pickle("specialChar",test_object, platform)
        try:
            read_pickle("specialChar", platform)
        except Exception as e:
            self.fail(e)
    
    def test_float(self):
        getcontext().prec=1000
        float1 = Decimal(2) ** Decimal(0.5)
        getcontext().prec=1001
        float2 = Decimal(2) ** Decimal(0.5)
        create_pickle("float1",float1, platform)
        create_pickle("float2",float2, platform)
        self.assertNotEqual(read_pickle("float1", platform), read_pickle("float2", platform))
   
    def test_nan(self):
        test_object = math.nan #would also work with float('nan')
        create_pickle("nan",test_object, platform)
        try:
            read_pickle("nan", platform)
        except Exception as e:
            self.fail(e)

    
    def test_inf(self):
        test_object = math.inf
        create_pickle("inf",test_object, platform)
        try:
            read_pickle("inf", platform)
        except Exception as e:
            self.fail(e)
        
    def test_negative_inf(self):
        test_object = -math.inf
        create_pickle("ninf",test_object, platform)
        try:
            read_pickle("ninf", platform)
        except Exception as e:
            self.fail(e)
    
    def test_complex(self):
        test_object = complex(1,2)
        create_pickle("complex",test_object, platform)
        try:
            read_pickle("complex", platform)
        except Exception as e:
            self.fail(e)
    
    # If pklfiles from multiple platforms exist

    # Check if pkl files encodes the same between platforms for unittests
    if folder_contains_file("unittest_pkl_files/", "windows") and folder_contains_file("unittest_pkl_files/", "linux"):
        linux_list, windows_list = [], []

        for file in os.listdir("unittest_pkl_files/"):
            if "linux" in file:
                linux_list.append(file.split("_")[0])
            elif "windows" in file:
                windows_list.append(file.split("_")[0])

        def test_unittests_between_platforms(self):
            for i in range(len(self.linux_list)):
                self.assertNotEqual(read_pickle(self.linux_list[i], "linux"), read_pickle(self.windows_list[i], "windows"))

    # Check if pkl files encodes the same between platforms for fuzzing
    if folder_contains_file("fuzz_pkl_files/", "windows") and folder_contains_file("fuzz_pkl_files/", "linux"):
        linux_list, windows_list = [], []

        for file in os.listdir("fuzz_pkl_files/"):
            if "linux" in file:
                linux_list.append(file.split("_")[0])
            elif "windows" in file:
                windows_list.append(file.split("_")[0])

        def test_fuzz_between_platforms(self):
            for i in range(len(self.linux_list)):
                self.assertNotEqual(read_pickle(self.linux_list[i], "linux"), read_pickle(self.windows_list[i], "windows"))
    
        
        
if __name__ == '__main__':
    unittest.main()
    