from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

Link = "file:///Users/BPS/Desktop/JARVIS/Gui.html"
chrome_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36"
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--use-fake-device-for-media-stream")
#chrome_options.add_argument("--headless=new")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(Link)

def GUI():
    driver.find_element(by=By.XPATH,value="/html/body/main/button").click()
    file_path = "/Users/BPS/Desktop/JARVIS/Jarvis.py"

    if os.path.exists(file_path):
        # Execute the file
        os.system("python3 " + file_path)
    else:
        pass

GUI()
input(">>> ")
driver.quit()

