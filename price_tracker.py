import requests
from bs4 import BeautifulSoup
import time

headers =  {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

URL = input("Enter the url of the product: ")

def find_price(URL):
    r = requests.get(URL,headers = headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    try:
        if 'amazon' in URL:
            # try:
                price = soup.find('span',class_='a-price-whole')
                return price
            # except:
            #     price = soup.find('span',id='priceblock_dealprice')
            #     return price

        elif 'flipkart' in URL:
            price = soup.find('div',class_="_30jeq3 _16Jk6d")
            return price
    except:
        return

while True:   
    price = find_price(URL)
    if price == None:
        print("Invalid URL")
        break
    else:
        print(f"Your current price is : {price.get_text()}")
        time.sleep(10)