import requests
import zipfile
import io

# Load the list of World Bank indicators from a text file
with open('wb-indicators-list.txt', 'r') as indicators_file:
    indicators_list = indicators_file.read().splitlines()

# Function to download and unzip the zipped CSV file for the given indicator
def download_and_unzip_world_bank_csv_data(indicator):
    url = f"https://api.worldbank.org/v2/en/indicator/{indicator}?downloadformat=csv"

    response = requests.get(url)

    if response.status_code == 200:
        zip_file = zipfile.ZipFile(io.BytesIO(response.content))
        csv_filename = f"{indicator}.csv"
        zip_file.extractall(path=f"data/{indicator}/")
        zip_file.close()
        print(f"CSV file for {indicator} has been downloaded and unzipped successfully.")
    else:
        print(f"Failed to download the CSV file for indicator: {indicator}")

# Iterate over each indicator in the list and download its data
for indicator in indicators_list:
    download_and_unzip_world_bank_csv_data(indicator)