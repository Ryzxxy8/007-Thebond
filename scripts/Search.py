from urllib.parse import urlencode


class WebSearch:
    def __init__(self, query: str) -> None:
        self.query = query.strip()
        self.search()

    def search(self) -> None:
        if not self.query:
            print("[ERROR] Search query cannot be empty.")
            return

        if len(self.query) > 300:
            print("[ERROR] Search query is too long (max 300 characters).")
            return

        if any(ord(char) < 32 for char in self.query):
            print("[ERROR] Search query contains unsupported control characters.")
            return

        params = urlencode({
            "q": self.query,
            "safe": "active"
        })

        url = f"https://www.google.com/search?{params}"

        print("\n===== WEB SEARCH =====")
        print("Open this link in your browser:")
        print(url)
        print("\n[INFO] No scraping or API key is used.")
