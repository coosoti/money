import re

def process_hash(original_hash):
    text = original_hash[:8]

    if re.match(re.compile(r"\d[A-F]\d{4}[A-F]\d"), text):
        return 1.38
    elif re.match(re.compile(r"\d{3}[A-F]\d[A-F]\d{2}"), text):
        return 1.05
    elif re.match(re.compile(r"[A-F]\d{3}[A-F]\d{2}[A-F]"), text):
        return 1.25
    elif re.match(re.compile(r"[A-F]\d[A-F]\d{5}"), text):
        return 1.29
    elif re.match(re.compile(r"\d{3}[A-F]{3}\d{2}"), text):
        return 1.08
    elif re.match(re.compile(r"[A-F]\d{7}"), text):
        return 1.4
    elif re.match(re.compile(r"\d{8}"), text):
        return 6540.14
    elif re.match(re.compile(r"\d{2}[A-F]\d[A-F]\d[A-F]{2}"), text):
        return 251.78
    elif re.match(re.compile(r"[A-F]{2}\d{4}[A-F]{2}"), text):
        return 47.32
    elif re.match(re.compile(r"[A-F]{2}\d{5}[A-F]"), text):
        return 1.62
    elif re.match(re.compile(r"\d{3}[A-F]\d{4}"), text):
        return 5.47
    elif re.match(re.compile(r"\d[A-F]\d[A-F]\d[A-F]{2}\d"), text):
        return 5.31
    elif re.match(re.compile(r"[A-F]\d[A-F]{2}\d{4}"), text):
        return 15.53
    elif re.match(re.compile(r"\d[A-F]\d[A-F]{2}\d[A-F]{2}"), text):
        return 52.3
    elif re.match(re.compile(r"\d[A-F]\d[A-F]\d[A-F]\d[A-F]"), text):
        return 12
    elif re.match(re.compile(r"[A-F]\d{5}[A-F]\d"), text):
        return 1.2
    elif re.match(re.compile(r"\d{2}[A-F]{2}\d{4}"), text):
        return 18.05
    elif re.match(re.compile(r"\d{2}[A-F]\d{3}[A-F]\d"), text):
        return 6.05
    elif re.match(re.compile(r"\d[A-F]\d{2}[A-F]{3}\d"), text):
        return 21.88
    else:
        return None

# Loop to prompt the user for input
while True:
    # Get input from the user
    original_hash = input("Enter the original hash (type 'exit' to stop): ")

    # Check if the user wants to exit
    if original_hash.lower() == 'exit':
        break

    # Process the hash and print the result
    result = process_hash(original_hash)
    if result is not None:
        print("Result:", result)
    else:
        print("Not a match")
