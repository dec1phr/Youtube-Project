from googleapiclient.discovery import build
import urllib.request
import re
import yt_dlp
import view
import youtubedataapiv3



if __name__ == '__main__':
    
    usr = str(input("Your input goes here: "))
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+usr)

    video_ids = list(re.findall(r"watch\?v=(\S{11})", html.read().decode()))

    ydl_opts = {}
    top_results ={}

    for urls in video_ids[:20]: #the url contains individual urls #the video_ids contains all the 11 part of the links and it's basically a list
        #url = str("https://www.youtube.com/watch/?v="+video_ids[0])
        with yt_dlp.YoutubeDL(ydl_opts) as ytdl:
            try:
                info = ytdl.extract_info(urls, download=False)
                top_results.update({str(urls):int(info["view_count"])})
            except:
                pass
            
            
    by_view = view.views(top_results)

    for v in by_view:
        print("https://www.youtube.com/watch/?v="+v)

    youtubedata = youtubedataapiv3.like_count(video_ids)
    print(video_ids[0])
    print(youtubedata)
