import requests
from bs4 import BeautifulSoup

def get_exchange_rate():
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }
    response = requests.get("http://finance.naver.com/marketindex/", headers = headers);

    soup = BeautifulSoup(response.content, 'html.parser');
    price = soup.select_one("div.head_info > span.value").text;
    print(f"KRW: {price}");

while True:
    get_exchange_rate();



