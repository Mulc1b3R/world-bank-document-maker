import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

# URL of the webpage to analyze
base_url = 'https://www.zerohedge.com/'

# Specify a user agent to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Fetch the webpage content with the specified user agent
response = requests.get(base_url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all linked JavaScript files in the webpage
    script_tags = soup.find_all('script', src=True)
    
    for script_tag in script_tags:
        js_url = urljoin(base_url, script_tag['src'])
        js_response = requests.get(js_url)
        
        if js_response.status_code == 200:
            js_content = js_response.text
            
            # Search for .json files or URLs containing 'api' in the JavaScript content
            json_files = re.findall(r'"(.*?\.json)"', js_content)
            api_urls = re.findall(r'"(.*?api.*?)"', js_content)
            # Search for 'apikey=' or 'api-key' in URL query strings
            api_keys = re.findall(r'[?&](?:api-)?key=([^&#]+)', js_content)
            xml_files = re.findall(r'"(.*?\.xml)"', js_content)

            if json_files or api_urls:
                print(f"JavaScript file: {js_url}")
                for json_file in json_files:
                    print(f"Found .json file: {urljoin(base_url, json_file)}")
                for api_url in api_urls:
                    print(f"Found API URL: {urljoin(base_url, api_url)}")
        

            if api_keys or xml_files:
                print(f"JavaScript file: {js_url}")
                for xml_files in xml_files:
                    print(f"Found .xml file: {urljoin(base_url, json_file)}")
                for api_keys in api_keys:
                    print(f"Found API URL: {urljoin(base_url, api_url)}")

        else:
            print(f"Failed to fetch JavaScript file: {js_url}")            
else:
    print("Failed to fetch the webpage.")
