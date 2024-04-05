import argparse
import csv
from collections import defaultdict

def find_repeated_events(file_path):
    event_counts = defaultdict(set)
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            method = row.get('Method')
            start = row.get('Start')
            end = row.get('End')
            recombinant = row.get('Recombinant')
            parent1 = row.get('Parent1')
            parent2 = row.get('Parent2')
            if method and start and end:
                event_counts[(start, end)].add((method, recombinant, parent1, parent2))

    repeated_events = [(event, methods) for event, methods in event_counts.items() if len(methods) >= 3]
    return repeated_events

def format_output(repeated_events):
    output_lines = []
    for event, methods in repeated_events:
        start, end = event  
        recombinant = methods.pop()[1]
        parent1 = methods.pop()[2]
        parent2 = methods.pop()[3]
        methods_str = ', '.join(method[0] for method in methods)
        output_lines.append(f"Recombinant/Parent1/Parent2: ('{recombinant}', '{parent1}', '{parent2}'), Positions: ('{start}'-'{end}'), Methods: ({methods_str})")
    return output_lines

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find repeated events in a CSV file.')
    parser.add_argument('-file', type=str, help='Path to the CSV file containing events data')

    args = parser.parse_args()

    if args.file:
        file_path = args.file
        repeated_events = find_repeated_events(file_path)
        formatted_output = format_output(repeated_events)
        for line in formatted_output:
            print(line)
    else:
        print("Provide the path to the CSV file using the -file argument.")

