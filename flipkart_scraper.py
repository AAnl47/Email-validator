import requests
from bs4 import BeautifulSoup
import pandas as pd

product_url = "https://www.flipkart.com/search?q=smartphone+under+30000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

response = requests.get(product_url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

name = []
price = []
links = []
stars=[]

for product in soup.find_all('div', class_='_2kHMtA'):
    name.append(product.find('div', class_='_4rR01T').text)
    price.append(product.find('div', class_='_30jeq3 _1_WHN1').text)

    product_link = "https://www.flipkart.com" + product.find('a', class_='_1fQZEK')['href']
    links.append(product_link)

    star=product.find('div', class_='_3LWZlK')
    stars.append(star)


# Save to CSV file
data = pd.DataFrame({
    "Name": name,
    "Stars":stars,
    "Price": price,
    "Link": links
})

data.to_csv("product.csv", index=False)
print("Done")

