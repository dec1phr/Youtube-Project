from googleapiclient.discovery import build
import urllib.request
import re
import yt_dlp
from itertools import islice

API_KEY = "API_KEY"

def views(top_results):
    by_view = {}
    sorted_views = list(islice(sorted(list(top_results.values()), reverse=True), 3))
    for key, value in top_results.items():
        if value in sorted_views:
            by_view.update({key: value})
    return by_view

def like_count(top_results):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    total_likes = {}
    for i in top_results:
        request = youtube.videos().list(
            part="statistics",
            id=i
        )
        response = request.execute()
        likes = int(response["items"][0]["statistics"].get("likeCount", 0))
        total_likes.update({str(i): likes})
    return total_likes

if __name__ == '__main__':
    print("-----------Welcome to Yinder ^^----------")
    print("-----------------------------------------")
    print("Choose options:")
    target = int(input("1 - search normal stuffs \n2 - looking for something to learn\n"))

    if target == 1:
        duration = int(input("Minimum Duration?: "))
        # still haven't decided what to do next :(

    usr = str(input("Your input goes here: "))
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + usr)
    video_ids = list(re.findall(r"watch\?v=(\S{11})", html.read().decode()))

    ydl_opts = {}
    top_results = {}

    for urls in video_ids[:20]:
        with yt_dlp.YoutubeDL(ydl_opts) as ytdl:
            try:
                info = ytdl.extract_info(urls, download=False)
                top_results.update({str(urls): int(info["view_count"])})
            except:
                pass

    by_view = views(top_results)
    youtubedata = like_count(by_view)

   
    for urls in by_view:
        print("https://www.youtube.com/watch?v=" + urls)
