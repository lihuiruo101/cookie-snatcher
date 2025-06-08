from cookiesnatcher import CookieSnatcher

snatcher = CookieSnatcher()
cookies = snatcher.fetch_cookies("https://naver.com", save_to_file="cookies.json")
print("쿠키 수집 완료:", cookies)
