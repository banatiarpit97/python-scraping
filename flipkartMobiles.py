import requests
from bs4 import BeautifulSoup
import pandas

url1 = "https://www.flipkart.com/search?as=off&as-show=on&otracker=start&page="
url2 = "&q=mobiles&viewType=list"

allMobiles = []

#upto 5 pages only
for i in range(1, 5):
    url = url1+str(i)+url2
    r = requests.get(url)
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')

    mobiles = soup.find_all('div', {'class':'_1-2Iqu'});
    for mobile in mobiles:
        tempFeatures = ""
        mobileDictionary = {}
        FeaturesArray = []
        name = mobile.find('div', {'class':'_3wU53n'})
        if(name):
            mobileDictionary['name'] = name.text
        else:
            mobileDictionary['name'] = "none"
        ram = mobile.find('div', {'class':'OiPjke'})
        if(ram):
            mobileDictionary['ram'] = ram.text
        else:
            mobileDictionary['ram'] = "none"
        price = mobile.find('div', {'class':'_1vC4OE'})
        if(price):
            mobileDictionary['price'] = price.text
        else:
            mobileDictionary['price'] = "none"
        discount = mobile.find('div', {'class':'VGWI6T'})
        if(discount):
            mobileDictionary['discount'] = discount.text
        else:
            mobileDictionary['discount'] = "none"
        rating = mobile.find('div', {'class', 'hGSR34 _2beYZw'})
        if(rating):
            rating = rating.text
            rating = rating.split("★");
            rating = rating[0]
            mobileDictionary['rating'] = rating
        else:
            mobileDictionary['rating'] = "none"
        features = mobile.find_all('li', {'class':'tVe95H'})
        if(features):
            for feature in features:
                FeaturesArray.append(feature.text)
                tempFeatures += feature.text
                tempFeatures +="\n"
            mobileDictionary['features'] = tempFeatures
        else:
            mobileDictionary['features'] = "none"
        allMobiles.append(mobileDictionary)

df = pandas.DataFrame(allMobiles)
print(df)
df.to_csv("flipkartMobiles.csv")
