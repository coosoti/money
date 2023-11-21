import csv
import re

def remove_pattern_occurrences(pattern):
    return re.sub(r'\{1\}', '', pattern)

def process_csv(input_filename='combinations_with_patterns.csv', output_filename='combinations_updated.csv'):
    try:
        examples_with_patterns = []

        with open(input_filename, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)

            for row in csv_reader:
                row[1] = remove_pattern_occurrences(row[1])
                examples_with_patterns.append(row)

        # Update the output CSV file with patterns
        with open(output_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(header)
            csv_writer.writerows(examples_with_patterns)

        print(f"Patterns updated and saved to {output_filename}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    process_csv()

if __name__ == "__main__":
    main()

