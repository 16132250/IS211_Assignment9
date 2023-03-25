import urllib.request
from bs4 import BeautifulSoup
url = "http://www.google.com"

def get_data(url):
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    return response

if __name__ == "__main__":
    page = get_data(url)
    soup = BeautifulSoup(page, 'html.parser')

    print(soup.prettify())
