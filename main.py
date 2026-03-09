import urllib.request
import re
import yt_dlp
from itertools import islice

usr = str(input("Your input goes here: "))
html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+usr)

video_ids = list(re.findall(r"watch\?v=(\S{11})", html.read().decode()))

ydl_opts = {}
top_results ={}
for urls in video_ids[:20]:
    #url = str("https://www.youtube.com/watch/?v="+video_ids[0])
    with yt_dlp.YoutubeDL(ydl_opts) as ytdl:
        try:
            info = ytdl.extract_info(urls, download=False)
            top_results.update({str(urls):int(info["view_count"])})
        except:
            pass
        
        
sorted_views = islice(sorted(list(top_results.values()), reverse=True), 3)      
        
for key, value in top_results.items():
    if value in sorted_views:
        print(key)
               
