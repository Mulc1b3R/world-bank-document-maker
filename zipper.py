import os
import zipfile

def zip_folder(folder_path, zip_filename):
    # Get the list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Create a zip file
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in files:
            file_path = os.path.join(folder_path, file)
            zipf.write(file_path, os.path.basename(file_path))

    print(f"All files in '{folder_path}' zipped to '{zip_filename}' successfully.")

# Folder path containing files to be zipped
folder_path = "path/to/folder"
# Name of the output zip file
zip_filename = "output.zip"

# Call the function to zip the folder
zip_folder(folder_path, zip_filename)