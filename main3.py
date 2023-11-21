import hashlib

def hash_to_float(hash_value):
    # Use hashlib to generate a hash object
    hash_object = hashlib.sha256(hash_value.encode('utf-8'))

    # Get the hexadecimal digest
    hex_digest = hash_object.hexdigest()

    # Convert the hexadecimal digest to an integer
    hash_integer = int(hex_digest, 16)

    # Scale the integer to a float in the desired range
    float_value = hash_integer % 5 + 1  # Adjust the range as needed

    return float_value

# Given hash values
hash_values = [
    "9b713a2ce3a9842c39fa058ea9e364495c6a641df3e9ddf797d40c563758e237",
    "945d7dbf62f99a7edb36e47ce279b1d2ad809893a181a7c40733e2de29281b01",
    "6ca72e1d72eb679c5b23098ed5194d78efbfff257e1a319fc3ad91ef322f33cc"
]

# Generate float values from hash values
float_values = [hash_to_float(hash_value) for hash_value in hash_values]

# Print the result
for hash_value, float_value in zip(hash_values, float_values):
    print(f"{hash_value} generates {float_value}")

