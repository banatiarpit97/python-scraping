import requests
from bs4 import BeautifulSoup
import os

playersList = []
class player():
    def __init__(self):
        self.name = ""
        self.link = ""
        self.height = ""
        self.weight = ""
        self.age = ""
        self.previousTeams = ""

url = "http://www.nba.com/players/"
r = requests.get(url)
html_content = r.content
soup = BeautifulSoup(html_content, 'html.parser')

allPlayersSection = soup.find('section', {'class':'row nba-player-index__row'})

allPlayersName = allPlayersSection.find_all('p', {'class':'nba-player-index__name'})

PlayerSection = allPlayersSection.find_all('section', {'class':'nba-player-index__trending-item'})

# allPlayersLink = allPlayersSection.find_all('a')

if not os.path.exists('player_images'):
    os.makedirs('player_images')

for pl in PlayerSection:
    newPlayer = player()
    newPlayer.name = pl.find('p', {'class':'nba-player-index__name'}).text
    newPlayer.link = "http://www.nba.com" + pl.find('a')['href']
    r2 = requests.get(newPlayer.link)
    soup = BeautifulSoup(r2.content, 'html.parser')
    infoSection = soup.find('section', {'class':'nba-player-vitals'})
    heightSection = infoSection.find('section', {'class':'nba-player-vitals__top-left'})
    newPlayer.height = heightSection.find('p', {'class':'nba-player-vitals__top-info-imperial'}).text
    weightSection = infoSection.find('section', {'class':'nba-player-vitals__top-right'})
    newPlayer.weight = weightSection.find('p', {'class':'nba-player-vitals__top-info-imperial'}).text
    bottomMenu = infoSection.find('section', {'class':'nba-player-vitals__bottom'})
    tabs = bottomMenu.find_all('li');
    for tab in tabs:
        if(tab.find(text = 'AGE')):
            newPlayer.age = tab.find('span', {'class':'nba-player-vitals__bottom-heading'}).nextSibling.text
            newPlayer.age = newPlayer.age.strip()
        if(tab.find(text = 'PREVIOUSLY')):
            newPlayer.previousTeams = tab.find('span', {'class':'nba-player-vitals__bottom-heading'}).nextSibling.text
    # imgSection = soup.find('section', {'class':'nba-player-header__item nba-player-header__headshot'})
    # imgSrc = "http:"+imgSection.find('img')['src']
    # imgFile = open('player_images/{0}.jpg'.format(newPlayer.name), 'wb')
    # imgR = requests.get(imgSrc)
    # imgFile.write(imgR.content)
    # imgFile.close()
    # print(newPlayer.name, newPlayer.link, newPlayer.height, newPlayer.weight, newPlayer.age, newPlayer.previousTeams)



# for player in playersList:
#     print(player.name, player.link, player.height, player.weight, player.age, player.previousTeams)


