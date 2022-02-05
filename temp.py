import requests
from bs4 import BeautifulSoup


response = requests.get('https://2ip.ru/')
if response:
    soup = BeautifulSoup(response.text, 'html.parser')
    ip = soup.find('div', class_='ip').text
    print(ip.strip())
