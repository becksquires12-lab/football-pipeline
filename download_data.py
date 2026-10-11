import requests
from pathlib import Path

URL = "https://www.football-data.co.uk/mmz4281/2526/E0.csv"
OUTPUT = Path("data/raw/E0_2526.csv")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

response = requests.get(URL, timeout=30)
response.raise_for_status()
OUTPUT.write_bytes(response.content)

print(f"Saved {OUTPUT}")
