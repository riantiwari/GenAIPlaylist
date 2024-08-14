#importing the llm_response class from the llm_model file
from llm_model import llm_response
from googleapiclient.discovery import build
import os #to be able to hide my api key for yt
from flask import Flask, jsonify
from flask_cors import CORS

#gets the api_key that I put in the nano /.zshrc file
#had to do source ~/.zshrc in the vscode terminal as well to make sure this echo'ed properly

app=Flask(__name__)
CORS(app)

yt_api_key = os.environ.get('YT_API_KEY')
youtube_service = build('youtube','v3',developerKey=yt_api_key)

#this method gets searches youtube for the parameter search query and then returns
#a link to the video with the highest rating most related to that search
def get_link(search_name):
    search_request = youtube_service.search().list(
        q=search_name,  # Replace with your search query
        part='snippet',
        maxResults=5,  # Get top 5 results
        type='video',
        order='relevance'  # Sort by relevance (or use 'rating' for rating)
    ).execute()  

    video_ids = [item['id']['videoId'] for item in search_request['items']]

    video_response = youtube_service.videos().list(
        part='statistics,snippet',
        id=','.join(video_ids)
    ).execute()

    best_video = max(video_response['items'], key=lambda x: int(x['statistics'].get('likeCount', 0)))
    best_video_id = best_video['id']
    #best_video_title = best_video['snippet']['title']
    video_link = f"https://www.youtube.com/watch?v={best_video_id}"
    return video_link

@app.route("/home", methods=['GET'])
def playlist():
    playlist_links = list()
    #comment this stuff out for now because I exceeded my quota limit
    # for i in llm_response.lst:
    #     playlist_links.append(get_link(i))
    playlist_links = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://www.youtube.com/watch?v=3JZ_D3ELwOQ"
    ]
    return jsonify({"home": playlist_links})

if __name__=="__main__":
    app.run(debug=True)

