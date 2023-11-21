import csv
from itertools import product

def generate_combinations():
    # Define the characters to combine
    characters = ['F', '9']

    # Generate all unique combinations
    combinations = product(characters, repeat=8)

    # Convert each combination to a string
    combinations_as_strings = [''.join(combination) for combination in combinations]

    return combinations_as_strings

def save_to_csv(combinations, filename='combinations.csv'):
    try:
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Combination'])
            csv_writer.writerows([(combination,) for combination in combinations])
        print(f"Combinations saved to {filename}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    try:
        combinations = generate_combinations()

        # Display the generated combinations
        print("Generated Combinations:")
        for combination in combinations:
            print(combination)

        save_to_csv(combinations)

        print("Total Combinations:", len(combinations))
    except KeyboardInterrupt:
        print("Program terminated by user.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

