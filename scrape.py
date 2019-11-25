# Import Libraries
from bs4 import BeautifulSoup
import requests
import re

# Page link to scrape
page_link = 'https://www.bellevuecollege.edu/classes/Fall2019'
page_link_2 = 'https://www2.bellevuecollege.edu/classes/Fall2019'

bc_cs = 'https://catalog.bellevuecollege.edu/preview_program.php?catoid=6&poid=1297&returnto=189'

# Fetch content
print('Fetching content from ' + bc_cs)
# page_response = requests.get(bc_cs, timeout=5)
page_response = requests.get(bc_cs, verify=False, timeout=5)


# Parse content
print()
print('Parsing content...')
page_content = BeautifulSoup(page_response.content, "html.parser")

# Get all divs with the following tag
div_tags = page_content.findAll("div", {"class": "acalog-core"})
regex_filter = reg = "[A-Z]{2,5}&?[0-9][0-9][0-9]"
pattern = re.compile(regex_filter)
for div in div_tags:
    print("__________________")
    li_tags = div.findAll("li")
    for li in li_tags:
        split_content = li.text.split(' ')
        content = str(split_content[0] + split_content[1])
        if (pattern.match(content)):
            print(content)
    # print(div)
#print(div_tags)

# Separate all list element content
'''
textContent = []
for i in range(0,20):
    paragraphs = page_content.find_all("li")[i]
    textContent.append(paragraphs)


print()
print('Output from parsed content...')
for i in textContent:
    print(i)
'''









