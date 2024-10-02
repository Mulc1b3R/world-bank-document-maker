import csv
import wbgapi as wb

# Get information about World Bank indicators
series_info = wb.series.info()

# Convert Featureset object to a list
series_info_list = list(series_info)

# Write the information to a CSV file
with open('info/wb_indicators_info.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'value'])  # Write the header
    for series in series_info_list:
        writer.writerow([series['id'], series['value']])

print("Data saved to 'wb_indicators_info.csv' successfully.")