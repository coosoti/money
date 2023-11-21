import csv
import re
from itertools import product

def generate_combinations():
    # Define the characters to combine
    characters = ['A-Z', '0-9']

    # Generate all unique combinations with repetition indicators
    combinations_with_repetition = product(characters, repeat=8)

    # Convert each combination to a string
    combinations_as_strings = [''.join(combination) for combination in combinations_with_repetition]

    return combinations_as_strings

def generate_pattern(combination):
    pattern = ''
    for char in combination:
        if char == 'A-Z':
            pattern += '[A-Z]'
        elif char == '0-9':
            pattern += '\d'
        else:
            pattern += char

    return pattern

def save_to_csv(combinations, filename='combinations.csv'):
    try:
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Combination', 'Regex Pattern'])
            for combination in combinations:
                pattern = generate_pattern(combination)
                csv_writer.writerow([combination, pattern])
        print(f"Combinations and Patterns saved to {filename}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    try:
        combinations = generate_combinations()

        # Display the generated combinations and patterns
        print("Generated Combinations and Patterns:")
        for combination in combinations:
            pattern = generate_pattern(combination)
            print(f"Combination: {combination}, Pattern: {pattern}")

        save_to_csv(combinations)

        print("Total Combinations:", len(combinations))
    except KeyboardInterrupt:
        print("Program terminated by user.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

