from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from TTS.TTS import TextToSpeech

Link = "file:///Users/BPS/Desktop/JARVIS-MK-IV/STT/voice.html"
chrome_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36"
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--use-fake-device-for-media-stream")
#chrome_options.add_argument("--headless=new")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(Link)
driver.minimize_window()

def SpeechRecognitionModel():
      driver.find_element(by=By.ID,value="start").click()
      print("Listening...")
      TextToSpeech("Speech Recognition Initialized...")
      while True:
            try:
                  Text = driver.find_element(by=By.ID,value="output").text
                  if Text:
                        driver.find_element(by=By.ID,value="end").click()
                        print(Text)
                        return Text

                  else:
                        sleep(0.333)

            except:
                  pass

SpeechRecognitionModel()