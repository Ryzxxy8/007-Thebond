import ipaddress
import requests


class IpLookup:
    def __init__(self, ip: str) -> None:
        self.ip = ip.strip()
        self.data = {}
        self.lookup()

    def lookup(self):
        try:
            # Validate IP address
            ipaddress.ip_address(self.ip)

            url = f"https://ipwho.is/{self.ip}"
            response = requests.get(url, timeout=20)
            response.raise_for_status()

            self.data = response.json()

            if not self.data.get("success"):
                print("[ERROR] IP lookup failed.")
                print(self.data.get("message", "Unknown error"))
                return

            self.print_data()

        except ValueError:
            print("[ERROR] Invalid IP address.")
        except requests.RequestException as e:
            print(f"[ERROR] Network request failed: {e}")
        except requests.exceptions.JSONDecodeError:
            print("[ERROR] Invalid API response.")

    def print_data(self):
        connection = self.data.get("connection") or {}
        timezone = self.data.get("timezone") or {}

        print("\n===== IP LOOKUP RESULTS =====")
        print(f"IP: {self.data.get('ip', 'Unknown')}")
        print(f"Type: {self.data.get('type', 'Unknown')}")
        print(f"Country: {self.data.get('country', 'Unknown')}")
        print(f"Country Code: {self.data.get('country_code', 'Unknown')}")
        print(f"Region: {self.data.get('region', 'Unknown')}")
        print(f"City: {self.data.get('city', 'Unknown')}")
        print(f"Postal Code: {self.data.get('postal', 'Unknown')}")
        print(f"Time Zone: {timezone.get('id', 'Unknown')}")
        print(f"ISP: {connection.get('isp', 'Unknown')}")
        print(f"Organization: {connection.get('org', 'Unknown')}")
        print(f"ASN: {connection.get('asn', 'Unknown')}")
        print("\nLookup completed.\n")
