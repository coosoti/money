def hash_to_float(hash_value):
    # Take the first 8 characters of the hash and convert to an integer
    hash_integer = int(hash_value[:8], 16)

    # Scale the integer to a float between 0 and 1
    float_value = hash_integer / (16**8)

    # Map the float to the desired range (e.g., 1.0 to 5.0)
    result = 1.0 + float_value * 4.0

    return result

# Given hash value
hash_value = "7202e421f010bc55e333a9cd31af215f2410da42eee5f92aa701cf5b0891d482"

# Generate float value from hash value
generated_number = hash_to_float(hash_value)

# Print the result
print(f"The hash value {hash_value} translates to: {generated_number:.2f}")

