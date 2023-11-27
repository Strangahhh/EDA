import requests
from bs4 import BeautifulSoup

# Replace 'https://example.com' with the URL of the website you want to scrape
url = 'https://www.jobmyway.com/%E0%B8%AB%E0%B8%B2%E0%B8%87%E0%B8%B2%E0%B8%99'

# Send a GET request to the URL and store the response
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
  # Parse the HTML content using Beautiful Soup
  soup = BeautifulSoup(response.content, 'lxml')

  # Print the HTML code
  print(soup.prettify())
else:
  print('Error: Failed to fetch the website.')
