# cookie-snatcher

웹사이트에 접속해서 쿠키를 자동으로 수집하는 파이썬 모듈.

## 사용 예제

```python
from cookiesnatcher import CookieSnatcher

snatcher = CookieSnatcher()
cookies = snatcher.fetch_cookies("https://example.com", save_to_file="cookies.json")
print(cookies)

---

## ✅ GitHub 업로드 방법
1. 위 구조로 파일 저장
2. GitHub에 새 레포지토리 생성 (이름: `cookie-snatcher`)
3. 아래 명령어로 업로드:
```bash
git init
git remote add origin https://github.com/yourname/cookie-snatcher.git
git add .
git commit -m "initial commit"
git push -u origin master
