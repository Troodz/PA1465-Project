import pickle
import hashlib
import random

def generate_recursive_data(depth, seed):
    """
    Generate a random recursive data structure.
    """
    random.seed(seed)
    if depth <= 0:
        return random.choice([random.randint(0, 100), random.random(), random.choice(['a', 'b', 'c'])])
    else:
        return [generate_recursive_data((depth - 1), seed) for _ in range(random.randint(1, 5))]

def pickle_and_hash(i, data):
    """
    Pickle the data and compute its hash.
    """
    pickled_data = pickle.dumps(data)

    with open("fuzz_pkl_files/" + str(i) + ".pkl", "wb") as f:
        f.write(pickled_data)

    data_hash = hashlib.sha256(pickled_data).hexdigest()
    return data_hash

def fuzzer(iterations):
    """
    Fuzz testing for pickle serialization and hash validation.
    """
    pickles_and_hashes = {}  # Store pickled data and corresponding hashes

    for i in range(iterations):

        random.seed(i)
        # Generate a random recursive data structure
        recursive_data = generate_recursive_data(random.randint(1, 10), i)

        # Pickle the data and compute its hash
        data_hash = pickle_and_hash(i, recursive_data)
        with open("fuzz_pkl_files/" + str(i) + ".pkl", "rb") as f:
            pickled_data = pickle.load(f)

        # Check if the hash is already in the dictionary
        if data_hash in pickles_and_hashes:
            # Compare the pickles to ensure consistency
            if pickles_and_hashes[data_hash] != pickled_data:
                print("Inconsistent pickle for the same input!")
        else:
            # Store the pickled data and hash
            pickles_and_hashes[data_hash] = pickled_data

    print("Fuzz test completed.")

# Example usage:
fuzzer(100)
