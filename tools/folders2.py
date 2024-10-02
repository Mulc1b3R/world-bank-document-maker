import json
import os

# Read the country data from input.json
with open('input.json', 'r') as file:
    country_data = json.load(file)

# Create folders named after each country code in the Docs folder
for country_code in country_data.keys():
    folder_name = f"Docs/{country_code}"
    os.makedirs(folder_name, exist_ok=True)
    print(f"Created folder: {folder_name}")

print("Folders have been created successfully.")