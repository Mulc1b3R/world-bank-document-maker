import json
import matplotlib.pyplot as plt
import requests
import pandas as pd
import io

# User input to enter the country code and indicator
country_code = input("Enter the country code: ")
wb_indicator = input("Enter the World Bank indicator: ")

# First World Bank API URL
url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/{wb_indicator}?format=json"

# Define the second World Bank API URL for Excel format
second_url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/{wb_indicator}/?downloadformat=excel&dataformat=table"

# Read metadata JSON file to extract description and metadata for the indicator
with open(f'metadata/{wb_indicator}_metadata.json', 'r') as metadata_file:
    metadata = json.load(metadata_file)
    indicator_description = metadata['description']
    indicator_metadata = metadata['metadata']

# Make the first API request
response = requests.get(url)
data = response.json()

# Make the second API request
second_response = requests.get(second_url)

# Read the Excel content from the response
excel_data = pd.read_excel(io.BytesIO(second_response.content))

# Extracting data from the Excel file based on the actual column names
data_columns = excel_data.columns

second_data_content = ""
for idx, row in excel_data.iterrows():
    row_content = ""
    for column in data_columns:
        row_content += f"<p>{column}: {row[column]}</p>"
    second_data_content += f"<div>{row_content}</div>"

# Displaying each row as a separate <div> within the main <div>
second_data_div_content = f"""
<div>
    <h3>Data Points for {indicator_description} for {country_code}</h3>
    {second_data_content}
</div>
"""

# Extracting data points and years
data_points = []
years = []
for entry in data[1]:
    if entry['value']:
        data_points.append(float(entry['value']))
        years.append(entry['date'])

# Reverse the lists to plot from oldest to most recent dates
data_points.reverse()
years.reverse()

# Generate the plot
plt.figure(figsize=(12, 8))
plt.plot(years, data_points, marker='o', color='b', linestyle='-', linewidth=2)
plt.title(f'{indicator_description} for {country_code}')
plt.xlabel('Years')
plt.ylabel(f'{indicator_description}')
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.grid(True)

# Save the plot image
plt.savefig(f'Docs/{country_code}/{indicator_description}.png')
plt.show()

print(f"Plot image saved as 'Docs/{country_code}/{indicator_description}.png'")

# Read metadata JSON file to extract description and metadata for the indicator
with open(f'metadata/{wb_indicator}_metadata.json', 'r') as metadata_file:
    metadata = json.load(metadata_file)
    indicator_description = metadata['description']
    indicator_metadata = metadata['metadata']

# Define and populate data_div_content as required based on the extracted data
# Define the data_div_content as an HTML table
data_table_rows = ""
for idx, row in enumerate(data_points):
    data_table_rows += f"<tr><td>{years[idx]}</td><td>{row}</td></tr>"

data_div_content = f"""
<div>
    <h3>Data Points for {indicator_description} for {country_code}</h3>
    <table>
        <tr>
            <th>Year</th>
            <th>Data</th>
        </tr>
        {data_table_rows}
    </table>
</div>
"""

# Define the second_data_div_content as an HTML table
second_table_rows = ""
for row in excel_data.iterrows():
    columns = row[1]
    second_table_row = ""
    for column in data_columns:
        second_table_row += f"<td>{columns[column]}</td>"
    second_table_rows += f"<tr>{second_table_row}</tr>"

second_data_div_content = f"""
<div>
    <h3>Data Points for {indicator_description} from Second API</h3>
    <table>
        <tr>
            {[f"<th>{column}</th>" for column in data_columns]}
        </tr>
        {second_table_rows}
    </table>
</div>
"""

# Create metadata HTML content
metadata_content = f'<h3>Metadata for {wb_indicator}</h3><br><br><p>{indicator_metadata}</p>'



# Create the full HTML content with all sections including the corrected data_div_content
html_content = f"""
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{indicator_description} for {country_code}</title>
    <link rel="stylesheet" href="../style.css">
    <link rel="icon" type="image/jpg" href="favicon.jpg">
</head>
<body>
    <center>
        <h2>{indicator_description} for {country_code}</h2>
        <img src="{indicator_description}.png"><br>
        <div id="metadata">{metadata_content}</div><br></center>
        <div>{data_div_content}</div><br>
        <div>{second_data_div_content}</div><br>
        <br><br>
        API DATA:<br><br>
        
<a href="https://api.worldbank.org/v2/sources/2/country/{country_code}/series/{wb_indicator}/metadata?format=json">JSON FORMAT</a>
<br>
<a href="https://api.worldbank.org/v2/sources/2/country/{country_code}/series/{wb_indicator}/metadata">XML FORMAT</a>
<br><br>
Download Urls:
<br><br>
<a href="https://api.worldbank.org/v2/en/indicator/{wb_indicator}?downloadformat=csv">Download CSV Data</a>
<br>
<a href="https://api.worldbank.org/v2/en/indicator/{wb_indicator}?downloadformat=xml">Download XML Data</a>
<br>
<br><a href="links.html">See all links</a>
<br><br
    
</body>
</html>
"""

# Save the HTML content to a file
html_file_path = f'Docs/{country_code}/{indicator_description}.html'
with open(html_file_path, 'w') as html_file:
    html_file.write(html_content)

print(f"HTML document for {wb_indicator} {country_code} created and saved in: {html_file_path}")

