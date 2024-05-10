import os
import unittest
import math
from decimal import *
from help_functions import create_pickle, read_pickle, folder_contains_file
from float_fuzzer import fuzzer

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
        create_pickle("zeroTuple",test_object, platform, "unittest_pkl_files/")
        try:
            read_pickle(f"zeroTuple_{platform}.pkl", "unittest_pkl_files/")
        except Exception as e:
            self.fail(e)
        
    
    def test_special_char(self):
        test_object = "teståäö"
        create_pickle("specialChar",test_object, platform, "unittest_pkl_files/")
        try:
            read_pickle(f"specialChar_{platform}.pkl", "unittest_pkl_files/")
        except Exception as e:
            self.fail(e)
    
    def test_float(self):
        getcontext().prec=10000
        float1 = Decimal(2) ** Decimal(0.5)
        getcontext().prec=10001
        float2 = Decimal(2) ** Decimal(0.5)
        create_pickle("float1",float1, platform, "unittest_pkl_files/")
        create_pickle("float2",float2, platform, "unittest_pkl_files/")
        self.assertNotEqual(read_pickle(f"float1_{platform}.pkl", "unittest_pkl_files/"), read_pickle(f"float2_{platform}.pkl", "unittest_pkl_files/"))
   
    def test_nan(self):
        test_object = math.nan #would also work with float('nan')
        create_pickle("nan",test_object, platform, "unittest_pkl_files/")
        try:
            read_pickle(f"nan_{platform}.pkl", "unittest_pkl_files/")
        except Exception as e:
            self.fail(e)

    
    def test_inf(self):
        test_object = math.inf
        create_pickle("inf",test_object, platform, "unittest_pkl_files/")
        try:
            read_pickle(f"inf_{platform}.pkl", "unittest_pkl_files/")
        except Exception as e:
            self.fail(e)
        
    def test_negative_inf(self):
        test_object = -math.inf
        create_pickle("ninf",test_object, platform, "unittest_pkl_files/")
        try:
            read_pickle(f"ninf_{platform}.pkl", "unittest_pkl_files/")
        except Exception as e:
            self.fail(e)
    
    def test_complex(self):
        test_object = complex(1,2)
        create_pickle("complex",test_object, platform, "unittest_pkl_files/")
        try:
            read_pickle(f"complex_{platform}.pkl", "unittest_pkl_files/")
        except Exception as e:
            self.fail(e)

    # Executing the fuzzing test
    def test_fuzzing(self):
        fuzzer(100, platform)
    
    # If pklfiles from multiple platforms exist

    # Check if pkl files encodes the same between platforms for unittests
    if folder_contains_file("unittest_pkl_files/", "windows") and folder_contains_file("unittest_pkl_files/", "linux"):
        linux_unit_list, windows_unit_list,  = [], []
        print("Performing platform comparison for unittests")

        for file in os.listdir("unittest_pkl_files/"):
            if "linux" in file:
                linux_unit_list.append(file)
            elif "windows" in file:
                windows_unit_list.append(file)

        def test_unittests_between_platforms(self):
            for i in range(len(self.linux_unit_list)):
                print(self.linux_unit_list[i], "||", self.windows_unit_list[i])
                print(read_pickle(self.linux_unit_list[i], "unittest_pkl_files/"), "||" , read_pickle(self.windows_unit_list[i], "unittest_pkl_files/"), "\n")
                self.assertEqual(read_pickle(self.linux_unit_list[i], "unittest_pkl_files/"), read_pickle(self.windows_unit_list[i], "unittest_pkl_files/"))

    # Check if pkl files encodes the same between platforms for fuzzing
    if folder_contains_file("fuzz_pkl_files/", "windows") and folder_contains_file("fuzz_pkl_files/", "linux"):
        linux_fuzz_list, windows_fuzz_list = [], []
        print("Performing platform comparison for fuzzing")
        for file in os.listdir("fuzz_pkl_files/"):
            if "linux" in file:
                linux_fuzz_list.append(file)
            elif "windows" in file:
                windows_fuzz_list.append(file)

        def test_fuzz_between_platforms(self):
            for i in range(len(self.linux_fuzz_list)):
                self.assertEqual(read_pickle(self.linux_fuzz_list[i], "fuzz_pkl_files/"), read_pickle(self.windows_fuzz_list[i], "fuzz_pkl_files/"))
    
        
        
if __name__ == '__main__':
    unittest.main()
    