import os

# Create the 'QR-CODES' folder if it doesn't exist
output_folder = 'data'
os.makedirs(output_folder, exist_ok=True)

# Read indicators list from 'wb-indicators-list.txt'
with open('wb-indicators-list.txt', 'r') as file:
    for line in file:
        indicator_name = line.strip()
        indicator_folder = os.path.join(output_folder, indicator_name)

        # Create a folder for each indicator
        os.makedirs(indicator_folder, exist_ok=True)

print('Folders created successfully.')