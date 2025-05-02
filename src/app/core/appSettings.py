from dotenv import load_dotenv
import os
load_dotenv()

class AppSetting:
    def __init__(self):
        self.SERPER_API_KEY = os.getenv("SERPER_API_KEY")
        self.SERPER_API_URL = "https://google.serper.dev/news"
   
appSettings = AppSetting()