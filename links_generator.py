import requests
from bs4 import BeautifulSoup
 
# Function to extract links from a webpage
def extract_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
 
    # Extract links from <a> tags
    links = [link.get('href') for link in soup.find_all('a', href=True)]
 
    # Extract links from other tags like <link> and <script>
    other_tags = ['link', 'script', 'img']  # Add more tags if needed
    for tag in other_tags:
        links.extend([element.get('href') for element in soup.find_all(tag, href=True)])
 
    # Filter out None values and empty strings
    links = list(filter(None, links))
    
    return links
 
 
#Main function
url = "https://www.aitpune.com/"
all_links = extract_links(url)
print(all_links)
