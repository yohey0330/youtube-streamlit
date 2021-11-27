from bs4 import BeautifulSoup
import requests
url = 'https://tech-diary.net/data-science/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
header_2_and_3 = [tag.text for tag in soup.find('article').find_all(['h2', 'h3'])]
print(header_2_and_3)