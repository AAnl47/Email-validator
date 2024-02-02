import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

headers =  {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

url = "https://www.amazon.in/Redmi-Arctic-Storage-Dimensity-Slimmest/dp/B0CQPGG8KG/?_encoding=UTF8&pd_rd_w=N1m2W&content-id=amzn1.sym.44901b9b-bd56-4240-8b6b-3ad72079fb43%3Aamzn1.symc.adba8a53-36db-43df-a081-77d28e1b71e6&pf_rd_p=44901b9b-bd56-4240-8b6b-3ad72079fb43&pf_rd_r=284D9TYX2X8C03MWBHYR&pd_rd_wg=v836U&pd_rd_r=03bb965a-3a53-4513-876a-24bede1e5c08&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1"
def extract_price():
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    price = float(soup.find('span', class_="a-price-whole").text.replace(",",""))
    return price

SMTP_SERVER = "smtp.gmail.com"
PORT = 587
EMAIL_ID = "aanand5899@gmail.com"
PASSWORD = "ieeutbksbhnrlcok"

def notify():
    server = SMTP(SMTP_SERVER,PORT)
    server.starttls()
    server.login(EMAIL_ID,PASSWORD)

    subject = "Price Alert"
    body = "Price has fallen. Buy it now" + url
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(EMAIL_ID, EMAIL_ID, msg)
    server.quit()

affordable_price = 17000

if extract_price() <= affordable_price:
    notify()
