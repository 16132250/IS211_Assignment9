import urllib.request
from bs4 import BeautifulSoup
from prettytable import PrettyTable

url = "https://en.wikipedia.org/wiki/List_of_streaming_media_services"

def get_data(url):
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    return response

if __name__ == "__main__":
    page = get_data(url)
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find('table', class_='wikitable')


    rows = table.find_all('tr')

    pt = PrettyTable(['Service Name', 'Service Launch Date', 'Subscription Totals'])

    # Loop through each row and print the text content of each cell
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 3:
            name = cells[0].get_text().strip()
            date = cells[1].get_text().strip()
            subs = cells[2].get_text().strip()
            pt.add_row([name, date, subs])

    print(pt)