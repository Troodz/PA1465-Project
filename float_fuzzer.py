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

def pickle_and_hash(i, data, platform):
    """
    Pickle the data and compute its hash.
    """
    pickled_data = pickle.dumps(data)

    with open("fuzz_pkl_files/" + platform  + str(i) + ".pkl", "wb") as f:
        f.write(pickled_data)

    data_hash = hashlib.sha256(pickled_data).hexdigest()
    return data_hash

def fuzzer(iterations, platform):
    """
    Fuzz testing for pickle serialization and hash validation.
    """

    for i in range(iterations):

        random.seed(i)
        # Generate a random recursive data structure
        recursive_data = generate_recursive_data(random.randint(1, 5), i)

        # Pickle the data and compute its hash
        data_hash = pickle_and_hash(i, recursive_data, platform)
        with open("fuzz_pkl_files/" + platform + str(i) + ".pkl", "rb") as f:
            file_hashed_data = hashlib.sha256(f.read()).hexdigest()
        # Check if the hash is already in the dictionary
        success_count = 0
        failure_count = 0

        for i in range(iterations):
            random.seed(i)
            # Generate a random recursive data structure
            recursive_data = generate_recursive_data(random.randint(1, 5), i)

            # Pickle the data and compute its hash
            data_hash = pickle_and_hash(i, recursive_data, platform)
            with open("fuzz_pkl_files/" + platform + str(i) + ".pkl", "rb") as f:
                file_hashed_data = hashlib.sha256(f.read()).hexdigest()
            
            if data_hash != file_hashed_data:
                failure_count += 1
            else:
                success_count += 1

    print("\nFuzz test completed.")
    print(f"Success count: {success_count}")
    print(f"Failure count: {failure_count}")


