from googleapiclient.discovery import build

API_KEY = "AIzaSyAFdR_ceBa1gtOL5Pf7OT03Ic_LgHkjpPg"
youtube = build("youtube", "v3", developerKey=API_KEY)

def like_count(video_ids):
    request = youtube.videos().list(
        part="statistics",
        id = video_ids[0]
    )
    response = request.execute()
    likes = response["items"][0]["statistics"]["likeCount"]
    return likes
    
