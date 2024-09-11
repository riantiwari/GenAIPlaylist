#importing the llm_response class from the llm_model file
from llm_model import llm_response
from googleapiclient.discovery import build
import os  # to be able to hide my api key for yt
from flask import Flask, jsonify, request
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load YouTube API key from environment variable
yt_api_key = os.environ.get('YT_API_KEY')
youtube_service = build('youtube', 'v3', developerKey=yt_api_key)

# Function to fetch YouTube video link with the highest rating
def get_link(search_name):
    search_request = youtube_service.search().list(
        q=search_name,  
        part='snippet',
        maxResults=5,  
        type='video',
        order='relevance'
    ).execute()

    video_ids = [item['id']['videoId'] for item in search_request['items']]

    video_response = youtube_service.videos().list(
        part='statistics,snippet',
        id=','.join(video_ids)
    ).execute()

    best_video = max(video_response['items'], key=lambda x: int(x['statistics'].get('likeCount', 0)))
    best_video_id = best_video['id']
    video_link = f"https://www.youtube.com/watch?v={best_video_id}"
    return video_link

# Route to handle search query
@app.route("/home", methods=['GET'])
def playlist():
    search_query = request.args.get('search')  # Get query from frontend request
    print(f"Search query received: {search_query}")
    
    # Use llm_response to get relevant subtopics for the search query
    subtopics = llm_response.get_response(search_query)
    playlist_links = set()  # Use a set to avoid duplicate links
    
    for topic in subtopics:
        playlist_links.add(get_link(topic))
    
    print(playlist_links)

    # Return the playlist links as JSON
    return jsonify({"home": list(playlist_links)})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
