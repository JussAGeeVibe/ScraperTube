import json
import re
import requests
import urllib.request

from pytube import YouTube

class Helper:
    def __init__(self):
        pass

    def title_to_underscore_title(self, title: str):
        title = re.sub("[\W_]+", "_", title)
        return title.lower()

    def id_from_url(self, url: str):
        return url.rsplit('=', 1)[1]


class YouTubeStats:
    def __init__(self, url: str):
        #self.json_url = urllib.request.urlopen(url)
        self.json_url = requests.get(url)
        self.data = json.loads(self.json_url.text)

    def print_data(self):
        print(self.data)

    def get_video_title(self):
        return self.data["items"][0]["snippet"]["title"]

    def get_video_description(self):
        return self.data["items"][0]["snippet"]["description"]

    def download_video(self, youtube_url: str, title: str):
        YouTube(youtube_url).streams.first().download(filename=title)


#youtube API key
api_key = #refer to notepad file

link_file = "video_links.csv"
with open(link_file, "r") as f:
    content = f.readlines()

content = list(map(lambda s: s.strip(), content))
content = list(map(lambda s: s.strip(','), content))

helper = Helper()

for youtube_url in content:
    video_id = helper.id_from_url(youtube_url)
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
    yt_stats = YouTubeStats(url)
    title = yt_stats.get_video_title()
    title = helper.title_to_underscore_title(title)
    print(title)
    description = yt_stats.get_video_description()
    print(description)

#    with open(f"{title}_description.txt", "w", encoding='utf-8') as f:
#        f.write(description)

    yt_stats.download_video(youtube_url, title)





#s = "https://www.youtube.com/watch?v=jLDUXj6V3bA"
#t = "Just something to put this into perspective"
#helper = Helper()
#print(helper.id_from_url(s))
#print(helper.title_to_underscore_title(t))

#video_id = "ZkYOvViSx3E"

#json_url = urllib.request.urlopen(url)
#data = json.loads(json_url.read())

#print(data)

