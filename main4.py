import hashlib

def hash_to_float(hash_value):
    # Use hashlib to generate a digest (hash) from the input string
    hash_digest = hashlib.sha256(hash_value.encode()).hexdigest()

    # Convert the hash digest to a decimal integer
    hash_integer = int(hash_digest, 16)

    # Scale the integer to a float between 0 and 1
    float_value = hash_integer / (2**256)

    # Map the float to the desired range (e.g., 1.0 to 3.0)
    result = 1.0 + float_value * 2.0

    return result

# Given hash values
hash_values = [
    "9b713a2ce3a9842c39fa058ea9e364495c6a641df3e9ddf797d40c563758e237",
    "945d7dbf62f99a7edb36e47ce279b1d2ad809893a181a7c40733e2de29281b01",
    "6ca72e1d72eb679c5b23098ed5194d78efbfff257e1a319fc3ad91ef322f33cc"
]

# Generate float values from hash values
generated_numbers = [hash_to_float(hash_value) for hash_value in hash_values]

# Print the result
for i, value in enumerate(generated_numbers, start=1):
    print(f"Hash {i} generates: {value:.2f}")

