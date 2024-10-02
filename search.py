import googlesearch
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# User input for search query and country code
search_query = input("Enter the search query: ")
country_code = input("Enter the country code: ")

# Define custom User-Agent
user_agent = UserAgent().chrome

# Perform Google search
search_results = googlesearch.search(search_query, num=10, stop=10, user_agent=user_agent)

# Set the file path for saving the results
file_path = f"Docs/{country_code}/links.html"

# Write the search results to the specified file
with open(file_path, "w") as file:
    file.write("<html><body>\n")
    for i, url in enumerate(search_results, 1):
        file.write(f"<p>{i}. <a href='{url}'>{url}</a></p>\n")
    file.write("</body></html>")
    print(f"Search results saved to {file_path}")

# Print the search results to the terminal
print("Search results:")
for i, url in enumerate(search_results, 1):
    print(f"{i}. {url}")