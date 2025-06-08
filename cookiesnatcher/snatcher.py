import requests
import json

class CookieSnatcher:
    def __init__(self, user_agent=None):
        self.session = requests.Session()
        self.headers = {
            "User-Agent": user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

    def fetch_cookies(self, url: str, save_to_file: str = None) -> dict:
        response = self.session.get(url, headers=self.headers)
        cookies = self.session.cookies.get_dict()
        
        if save_to_file:
            with open(save_to_file, "w", encoding="utf-8") as f:
                json.dump(cookies, f, indent=2)
        
        return cookies
