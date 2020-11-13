from bs4 import BeautifulSoup
import urllib3
import requests
import lxml
import pandas as pd


#

htmlParser = "lxml"
html=requests.get('https://www.youtube.com/playlist?list=PLzdXffP5JtUmwzX3SjSK0Kmx34ahgk5NG')
# response=html.read()
soup=BeautifulSoup(html.text, htmlParser)
print(soup)
links = soup.find_all('a')#, attrs={'class': 'yt-simple-endpoint style-scope ytd-playlist-video-renderer'})
#print(links)

#for a in links:
#    print(a.get("href"))



#page = requests.get("https://www.youtube.com/playlist?list=PLzdXffP5JtUkiV6UJt7amA-XRXGdx1w-R")
#soup = BeautifulSoup(page.text, 'lxml')
#playlist = soup.find_all('a', {"class_ ": "pl-video-title-link"})
#items_container = playlist.find_all(class_="style-scope ytd-item-section-renderer")
#items_box = items_container.find(class_="style-scope ytd-playlist-video-list-renderer")
#items = items_box.find(class_="style-scope ytd-playlist-video-renderer")
#rack = items.find_all(href="/watch?v={};list=PLzdXffP5JtUkiV6UJt7amA-XRXGdx1w-R&amp")
#for l in playlist:
#    print(l.get('href'))

#print(items[0].find(class_="period-name").get_text())
#print(items[0].find(class_="short-desc").get_text())
#print(items[0].find(class_="temp").get_text())

#period_names = [item.find(class_="period-name").get_text() for item in items]
#short_desc = [item.find(class_="short-desc").get_text() for item in items]
#temp = [item.find(class_="temp").get_text() for item in items]


#print(period_names)
#print(short_desc)
#print(temp)

#weather_stuff = pd.DataFrame(
#    {"period": period_names,
#     "short_desc": short_desc,
#     "temp": temp,})

#print(weather_stuff)
#weather_stuff.to_csv("june.csv")