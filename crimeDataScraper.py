import urllib.request
import urllib.parse
import urllib.error

crimeFile = "crimeData.json"

try:
    url = "https://data.seattle.gov/resource/tazs-3rd5.json"
    response = urllib.request.urlopen(url)
    html = response.read()
    print(html.decode('utf-8'))  # Decode the bytes to a string
    print(f"Result code: {response.getcode()}")
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} {e.reason}")
except urllib.error.URLError as e:
    print(f"URL Error: {e.reason}")
