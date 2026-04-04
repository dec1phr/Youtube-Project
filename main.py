from googleapiclient.discovery import build
import urllib.request
import re
import yt_dlp
import view
import youtubedataapiv3



if __name__ == '__main__':
    
    print("-----------Welcome to Yinder ^^----------")
    print("-----------------------------------------")
    print("Choose options:")
    target = int(input("1 - search normal stuffs \n2 - looking for something to learn"))
    if target == 1:
        duration = int(input("Minimum Duration?: "))
        #still haven't decide what to do next:(


    

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
            
            
    by_view = view.views(top_results) #stores the top 10 video urls(11 letter part) which has been sorted by views
    youtubedata = youtubedataapiv3.like_count(by_view)
    video = []

    # keys = list(by_view.keys())
    # views = list(by_view.values())
    # likes = list(youtubedata.values())

    for urls in by_view:
        print("https://www.youtube.com/watch?v="+urls)
        
    


    
        
    print(video)
