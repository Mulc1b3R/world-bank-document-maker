import csv

# Read data from the main CSV file
with open(f'data/.csv', newline='', encoding='utf-8-sig') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header

    for row in csvreader:
        country_code = row[1]
        country_data = row[4:]

        # Save data for each country in a new CSV file
        output_file = f'data/.{country_code}.csv'
        with open(output_file, 'w', newline='', encoding='utf-8') as new_csvfile:
            csvwriter = csv.writer(new_csvfile)
            csvwriter.writerow(header)  # Write the header
            csvwriter.writerow(row)  # Write the data for the specific country

        print(f"Data for country {country_code} saved to '{output_file}'.")