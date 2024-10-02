import csv
import json

# Read the list of World Bank indicators from a text file
with open('wb-indicators-list.txt', 'r') as indicators_file:
    indicators_list = indicators_file.read().splitlines()

# Process each indicator data and save country-specific CSV files
for indicator in indicators_list:
    # Read data from the main CSV file
    with open(f'data/{indicator}/{indicator}.csv', newline='', encoding='utf-8-sig') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Skip the header
        
        for row in csvreader:
            country_code = row[1]
            country_data = row[4:]

            # Save data for each country in a new CSV file
            output_file = f'data/{indicator}/{indicator}.{country_code}.csv'
            with open(output_file, 'w', newline='', encoding='utf-8') as new_csvfile:
                csvwriter = csv.writer(new_csvfile)
                csvwriter.writerow(header)  # Write the header
                csvwriter.writerow(row)  # Write the data for the specific country

            print(f"Data for country {country_code} saved to '{output_file}' for indicator: {indicator}.")