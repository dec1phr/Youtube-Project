from googleapiclient.discovery import build

API_KEY = "AIzaSyAFdR_ceBa1gtOL5Pf7OT03Ic_LgHkjpPg"
youtube = build("youtube", "v3", developerKey=API_KEY)

def like_count(top_results):
    total_likes = {}
    for i in top_results:
        
        request = youtube.videos().list(
            part="statistics",
            id = i
        )
        response = request.execute()
        likes = int(response["items"][0]["statistics"].get("likeCount", 0))
        total_likes.update({str(i): likes})
        
    return total_likes
    
