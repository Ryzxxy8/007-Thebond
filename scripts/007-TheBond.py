#!/usr/bin/env python3

import sys
import time

from IpLookup import IpLookup
from PhoneLookup import PhoneLookup
from EmailLookup import EmailLookup
from Search import WebSearch


def typewriter(text: str, delay: float = 0.001) -> None:
    for char in text:
        sys.stdout.write(char)
        time.sleep(delay)
        sys.stdout.flush()
    print("\n")


def list_options() -> None:
    options = [
        "1. IP Lookup",
        "2. Phone Number Information",
        "3. Email Validation and Breach Check",
        "4. Web Search",
        "5. Exit"
    ]

    print("\n" + "=" * 20 + " OPTIONS " + "=" * 20)
    for option in options:
        print(option)


def main():
    print("\n===== 007 THEBOND =====")
    print("Educational Information Toolkit")
    print("Use only your own data or data you are authorized to check.")

    while True:
        list_options()

        try:
            option = input("\nSelect option: ").strip()

            if option == "1":
                ip = input("Enter test IP address: ").strip()
                IpLookup(ip)

            elif option == "2":
                phone = input("Enter phone number with country code: ").strip()
                PhoneLookup(phone)

            elif option == "3":
                email = input("Enter your email address: ").strip()
                EmailLookup(email)

            elif option == "4":
                query = input("Enter search query: ").strip()
                WebSearch(query)

            elif option == "5":
                print("Goodbye!")
                break

            else:
                print("[ERROR] Invalid option.")

        except KeyboardInterrupt:
            print("\nProgram interrupted.")
            break


if __name__ == "__main__":
    main()
