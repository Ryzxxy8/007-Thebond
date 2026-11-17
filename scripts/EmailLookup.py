import email_validator
import requests
import os


class Color:
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    reset = "\033[0m"


class EmailLookup:
    def __init__(self, email):
        self.email = email.strip()
        self.hibp_api_key = os.getenv("HIBP_API_KEY")
        self.color = Color()
        self.timeout = 10
        self.lookup()

    def lookup(self):
        try:
            email_info = email_validator.validate_email(
                self.email,
                check_deliverability=False
            )
            self.email = email_info.normalized

            print(
                f"{self.color.green}[OK] Email format is valid.{self.color.reset}"
            )
            print(f"Email: {self.email}")

            if not self.hibp_api_key:
                print(
                    f"{self.color.yellow}[INFO] HIBP API Key not configured. "
                    f"Breach check skipped.{self.color.reset}"
                )
                return

            hibp_data = self.check_hibp()

            if hibp_data is None:
                return

            if not hibp_data:
                print(
                    f"{self.color.green}[OK] No breaches found.{self.color.reset}"
                )
                return

            print("\n===== BREACH RESULTS =====")

            for breach in hibp_data:
                print(f"Name: {breach['name']}")
                print(f"Date: {breach['date']}")
                print(f"Count: {breach['pwncount']:,}")
                print(f"Leaked: {breach['types']}")
                print("-" * 30)

        except email_validator.EmailNotValidError:
            print(
                f"{self.color.red}[ERROR] Invalid email format.{self.color.reset}"
            )

    def check_hibp(self):
        try:
            url = (
                "https://haveibeenpwned.com/api/v3/"
                f"breachedaccount/{self.email}"
            )

            headers = {
                "hibp-api-key": self.hibp_api_key,
                "User-Agent": "007-TheBond"
            }

            params = {"truncateResponse": "false"}

            response = requests.get(
                url,
                headers=headers,
                params=params,
                timeout=self.timeout
            )

            if response.status_code == 404:
                return []

            if response.status_code == 401:
                print("[ERROR] Invalid HIBP API Key.")
                return None

            response.raise_for_status()

            results = []

            for breach in response.json():
                results.append({
                    "name": breach["Title"],
                    "date": breach["BreachDate"],
                    "pwncount": breach["PwnCount"],
                    "types": ", ".join(breach["DataClasses"])
                })

            return results

        except requests.RequestException as error:
            print(f"[ERROR] HIBP request failed: {error}")
            return None
