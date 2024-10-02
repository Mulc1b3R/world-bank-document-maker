import requests
import zipfile
import io

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
        print("Failed to download the CSV file. Please check the indicator and try again.")

# Get user input for the indicator
indicator = input("Enter the World Bank indicator code (e.g., EG.ELC.ACCS.RU.ZS): ")

# Download and unzip the zipped CSV file for the specified indicator
download_and_unzip_world_bank_csv_data(indicator)