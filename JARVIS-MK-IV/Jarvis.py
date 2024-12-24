from STT.SpeechRecognition import SpeechRecognitionModel
from TTS.TTS import TextToSpeech
from BRAIN.BRAINmain import generate_response
import subprocess
import datetime
import requests
from newsapi import NewsApiClient
import feedparser
import xml.etree.ElementTree as ET

def Jarvis():
    while True:
        user_query = SpeechRecognitionModel()
        print("You: ", user_query)
        if "good bye" in user_query or "bye" in user_query or "exit" in user_query:
            bye = generate_response("Goodbye JARVIS")
            print("JARVIS: " , bye)
            TextToSpeech(bye)
            '''
            file_path = "Functions/Clap_Detection.py"
            subprocess.call(['/usr/local/bin/python3', file_path])
            break
            '''
    
        elif "time" in user_query or "date" in user_query:
            current_datetime = datetime.datetime.now()

            # Print the current date and time
            print("Current Date and Time:", current_datetime)
            TextToSpeech(current_datetime)

        elif "latest news" in user_query:
            url = 'https://newsapi.org/v2/top-headlines'
            params = {
                'apiKey': "3f65029952ba4ae58e0bdd2e947ffa9f",
                'country': 'in'  # Fetch headlines from India
            }
            response = requests.get(url, params=params)
            data = response.json()

            if data['status'] == 'ok':
                articles = data['articles']
                print("Top Headlines in India:")
                for index, article in enumerate(articles, start=1):
                    print(f"\nArticle {index}:")
                    TextToSpeech(f"Article {index}")
                    print("Title:", article['title'])
                    TextToSpeech(f"Title {article['title']}")
                    print("Description:", article['description'])
                    TextToSpeech(f"Description {article['description']}")
                    print("Source:", article['source']['name'])
                    TextToSpeech(f"Source {article['source']['name']}")
                    print("URL:", article['url'])
                    print("Published At:", article['publishedAt'])
            else:
                print("Error fetching headlines:", data['message'])
             
        elif "space news" in user_query:
            nasa_rss_url = 'https://www.nasa.gov/rss/dyn/breaking_news.rss'
    
            # Send a GET request to the NASA RSS feed
            response = requests.get(nasa_rss_url)
            
            # Check if the request was successful
            if response.status_code == 200:
                # Parse the XML content of the feed
                root = ET.fromstring(response.content)
                
                # Print the news items
                print("NASA Space News:")
                print("---------------")
                for item in root.findall('.//item'):
                    title = item.find('title').text
                    link = item.find('link').text
                    description = item.find('description').text
                    print("Title:", title)
                    TextToSpeech(title)
                    print("Link:", link)
                    print("Description:", description)
                    TextToSpeech(description)
                    print()
            else:
                print("Failed to fetch NASA space news")
              
        else:
            response = generate_response(user_query)
            print("JARVIS: " , response)
            TextToSpeech(response)



if __name__ == "__main__":
        Jarvis()
