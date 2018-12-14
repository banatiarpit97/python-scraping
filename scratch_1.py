import requests
from bs4 import BeautifulSoup
r = requests.get('http://pythonhow.com/example.html')

content = r.content
soup = BeautifulSoup(content, 'html.parser')
pretty = soup.prettify()

divs = soup.find_all('div',{'class':'cities'})

for div in divs:
    print(div.find('h2').text)

for div in divs:
    print(div.find('p').text)
