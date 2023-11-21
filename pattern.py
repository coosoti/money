import csv
import re

def generate_pattern(text):
    pattern = ''
    current_char = text[0]
    counter = 1

    for char in text[1:]:
        if char == current_char:
            counter += 1
        else:
            if current_char == 'F':
                pattern += f'[A-F]{{{counter}}}'
            elif current_char == '9':
                pattern += f'\d{{{counter}}}'
            counter = 1
            current_char = char

    # Add the last part of the pattern
    if current_char == 'F':
        pattern += f'[A-F]{{{counter}}}'
    elif current_char == '9':
        pattern += f'\d{{{counter}}}'
    
    return pattern

def process_csv(input_filename='combinations.csv', output_filename='combinations_with_patterns.csv'):
    try:
        with open(input_filename, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)
            examples = [row[0] for row in csv_reader]

        # Generate patterns and update the CSV file
        with open(output_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Combination', 'Pattern'])

            for example in examples:
                result_pattern = generate_pattern(example)
                csv_writer.writerow([example, result_pattern])

        print(f"Patterns updated and saved to {output_filename}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    process_csv()

if __name__ == "__main__":
    main()

