import pickle
import hashlib
import sys
class version_check:
    def __init__(self) -> None:
        self.value = ()


def create_pickle(obj):
    with open("ver3.9.pkl", "wb") as f:
        pickle.dump(obj, f)





create_pickle(())

