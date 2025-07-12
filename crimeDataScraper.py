import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime
import calendar

def days_in_month(month, year):
    return calendar.monthrange(year, month)[1]

current_datetime = datetime.now()

year = current_datetime.year
month = current_datetime.month
day = current_datetime.day
#2024-01-01

while year >= 1900:     
    start_date = f"{year}-{month}-{day}T00:00:00.000"
    end_date = f"{year}-{month}-{day}T23:59:59.999"

    #URL encoding
    base_url = 'https://data.seattle.gov'
    query = f"offense_date between '{start_date}' and '{end_date}'"
    encoded = urllib.parse.quote(query)

    ##url = f"{base_url}/resource/tazs-3rd5.json?$where={encoded}"
    print(day, month, year)
    day = day - 1
    if day == 0:
        month = month - 1
        day = days_in_month(month, year)
    if month == 1 and day == 1:
        print(day, month, year)
        year = year - 1
        month = 12
        day = days_in_month(month,year)

#            try:
#                response = urllib.request.urlopen(url)
#                html = response.read()
#                print(html.decode('utf-8'))  # Decode the bytes to a string
#                print(f"Result code: {response.getcode()}")
#            except urllib.error.HTTPError as e:
#                print(f"HTTP Error: {e.code} {e.reason}")
#            except urllib.error.URLError as e:
#                print(f"URL Error: {e.reason}")
