import hashlib

hash_value = '461A4156850722C3DB3A410D2B9E6988339B203E4C6D1A22E58EBA32EECB9BAA'

float_number = float(int(hashlib.sha256(hash_value.encode('utf-8')).hexdigest(), 16) % (10 ** 8) / 100)

print(float_number)

