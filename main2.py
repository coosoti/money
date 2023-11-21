import numpy as np

# Given data
hash_values = [
    "9b713a2ce3a9842c39fa058ea9e364495c6a641df3e9ddf797d40c563758e237",
    "945d7dbf62f99a7edb36e47ce279b1d2ad809893a181a7c40733e2de29281b01",
    "6ca72e1d72eb679c5b23098ed5194d78efbfff257e1a319fc3ad91ef322f33cc"
]

generated_numbers = [2.91, 2.34, 1.73]

# Convert hash values to integers
hash_integers = [int(hash_value, 16) for hash_value in hash_values]

# Explicitly provide weights parameter to np.corrcoef
correlation_coefficient = np.corrcoef(hash_integers, generated_numbers, rowvar=False)[0, 1]

# Print the result
print(f"Correlation Coefficient: {correlation_coefficient}")

