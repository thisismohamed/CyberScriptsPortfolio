import hashlib

def generate_hash(data, algorithm):
    hasher = hashlib.new(algorithm)
    data_bytes = data.encode('UTF-8')
    # I USE UNICODE ENCODE 'UTF-8' BECAUSE IT ACCEPT ALL CHARACTERS AND NUMBERS
    hasher.update(data_bytes)
    hash_digest = hasher.hexdigest()
    return hash_digest

def main():
    data = input("Enter data to hash: ")
    print("\nChoose a hash algorithm:")
    print("1. MD5")
    print("2. SHA-1")
    print("3. SHA-224")
    print("4. SHA-256")
    print("5. SHA-384")
    print("6. SHA-512")
    print("7. BLAKE2B")
    print("8. BLAKE2S")
    print("9. SHA3-224")
    print("10. SHA3-256")
    print("11. SHA3-384")
    print("12. SHA3-512\n")
    choice = input("Enter your choice (1-12): ")
    algorithm_map = {
    "1": "md5",
    "2": "sha1",
    "3": "sha224",
    "4": "sha256",
    "5": "sha384",
    "6": "sha512",
    "7": "blake2b",
    "8": "blake2s",
    "9": "sha3_224",
    "10": "sha3_256",
    "11": "sha3_384",
    "12": "sha3_512"
    }
    algorithm = algorithm_map.get(choice)
    if algorithm:
        hash_result = generate_hash(data, algorithm)
        print("\nHash:",hash_result)
    else:
        print("\nInvalid choice\n")
        return main()

if __name__ == "__main__":
    main()
