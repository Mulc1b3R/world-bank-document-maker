import json
import os

metadata_folder = 'metadata'  # Path to the metadata folder containing JSON files
descriptions_file = 'indicators_titles.txt'  # Path to the file containing descriptions

# Read the descriptions from the descriptions file
with open(descriptions_file, 'r') as file:
    descriptions = [line.strip() for line in file]

# Sort the file paths based on their order in the folder
file_paths = [os.path.join(metadata_folder, file) for file in sorted(os.listdir(metadata_folder))]

# Update each JSON file with its corresponding description
for description, file_path in zip(descriptions, file_paths):
    with open(file_path, 'r+') as json_file:
        data = json.load(json_file)
        data['description'] = description  # Add description field to the JSON data
        json_file.seek(0)  # Move to the start of the file
        json.dump(data, json_file, indent=4)  # Write the updated JSON data back to the file

print("Descriptions added to the JSON files successfully.")