import wbgapi as wb

# Prompt user to enter the indicator to retrieve metadata
indicator = input("Enter the World Bank indicator code to retrieve metadata: ")

# Get metadata for the entered indicator and print it to the terminal
metadata = wb.series.metadata.get(indicator)
print(metadata)

# Write the indicator metadata to a file with a name that adapts based on the entered indicator
file_name = f'{indicator}_metadata.txt'
with open(file_name, 'w') as file:
    file.write(str(metadata))