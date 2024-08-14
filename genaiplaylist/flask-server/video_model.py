#importing the llm_response class from the llm_model file
from llm_model import llm_response
from googleapiclient.discovery import build
import os #to be able to hide my api key for yt

#gets the api_key that I put in the nano /.zshrc file
#had to do source ~/.zshrc in the vscode terminal as well to make sure this echo'ed properly

yt_api_key = os.environ.get('YT_API_KEY')
youtube_service = build('youtube','v3',developerKey=yt_api_key)

#All working

#example of the youtube api being used
request = youtube_service.channels().list(
    part='statistics', forUsername='schafer5'
)

#executing the api request
response = request.execute()
print(response)

#idea could be to list the duration of the playlist that we produce (important to the user)

#this is to iterate through the bulleted list of steps we compiled in the llm_model
for i in llm_response.lst:
    print(i)
    print()