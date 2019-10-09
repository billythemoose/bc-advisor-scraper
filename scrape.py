# Import Libraries
from bs4 import BeautifulSoup
import requests

# Page link to scrape
page_link = 'https://www.bellevuecollege.edu/classes/Fall2019'
page_link_2 = 'https://www2.bellevuecollege.edu/classes/Fall2019'

# Fetch content
print('Fetching content from ' + page_link)
page_response = requests.get(page_link, timeout=5)


# Parse content
print()
print('Parsing content...')
page_content = BeautifulSoup(page_response.content, "html.parser")

# Separate all list element content
textContent = []
for i in range(0,20):
    paragraphs = page_content.find_all("li")[i]
    textContent.append(paragraphs)

print()
print('Output from parsed content...')
for i in textContent:
    print(i)










