007-TheBond

Educational Information Toolkit

A Python-based command-line toolkit for basic information lookup and validation. Designed for educational use and authorized security research.

Use this toolkit only with your own information or data you have permission to check.

Features

Feature	Description
IP Lookup	Retrieves public IP address information using IPWho.is.
Phone Number Information	Parses and validates phone number information using phonenumbers.
Email Validation	Checks email address format and normalization.
Email Breach Check	Optional breach check using the Have I Been Pwned API.
Web Search	Creates a Google search link with SafeSearch enabled.

Important Notes

* Email breach checking requires a configured HIBP API key.
* Web Search opens a browser link. It does not scrape search results.
* IP geolocation provides approximate network-related information, not a person’s precise location or identity.
* Phone number information does not identify the owner of a number.

Requirements

* Python 3.10 or newer
* Git
* Internet connection
* pip

Installation

Clone the repository:

git clone https://github.com/Ryzxxy8/007-Thebond.git
cd 007-Thebond

Create a virtual environment:

python3 -m venv .venv

Activate it:

source .venv/bin/activate

Install dependencies:

python -m pip install --upgrade pip
pip install -r requirements.txt

Usage

Start the toolkit:

python scripts/007-TheBond.py

Main Menu

===== 007 THEBOND =====
Educational Information Toolkit
1. IP Lookup
2. Phone Number Information
3. Email Validation and Breach Check
4. Web Search
5. Exit

Choose an option and follow the prompts.

Email Breach Check Configuration

Email format validation works without an API key.

To enable breach checking, obtain an API key from Have I Been Pwned and configure the HIBP_API_KEY environment variable.

Linux / macOS:

export HIBP_API_KEY="your_api_key"

Then run the toolkit again.

Do not share your API key or commit it to GitHub.

Docker

A Dockerfile is included in this repository.

Docker support has not yet been tested by the maintainer. The following commands are provided for testing and are not a guarantee of successful operation.

Build:

docker build -t 007-thebond .

Run:

docker run --rm -it 007-thebond

Project Structure

007-Thebond/
├── scripts/
│   ├── 007-TheBond.py
│   ├── IpLookup.py
│   ├── PhoneLookup.py
│   ├── EmailLookup.py
│   └── Search.py
├── assets/
├── .github/
├── Dockerfile
├── auto-installer.py
├── requirements.txt
├── LICENSE
└── README.md

Responsible Use

This project is intended for education and authorized information lookup.

* Only check your own information or information you are authorized to access.
* Respect privacy and applicable laws.
* Do not use this toolkit for harassment, stalking, unauthorized surveillance, or other harmful activities.
* Keep API keys and other secrets private.

Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test your changes.
5. Submit a Pull Request.

Please ensure contributions are safe, documented, and consistent with the project’s purpose.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Maintainer

Maintained by Ryzxxy8

Repository: https://github.com/Ryzxxy8/007-Thebond
