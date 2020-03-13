import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = 'https://www.amazon.in/Acer-AN515-42-15-6-inch-Windows-Graphics/dp/B07GYF15LN/ref=sr_1_5?keywords=acer+nitro&qid=1584112808&sr=8-5'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

def check_price():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    proper_price = int(price[2:4]+price[5:8])

    if proper_price <= 50000:
        send_mail(title, price)


#print(proper_price)
#print(title.strip())

def send_mail(title, price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email@mail.com', 'password')
    subject = f'{title} Price Dropped!!! to {price}'

    body = 'Click on link \n https://www.amazon.in/Acer-AN515-42-15-6-inch-Windows-Graphics/dp/B07GYF15LN/ref=sr_1_5?keywords=acer+nitro&qid=1584112808&sr=8-5'

    msg = f"Subject: {subject}\n\n {body}"

    server.send_message(msg, 'email@mail.com', 'to@mail.com')
    server.quit()

while True:
    check_price()
    time.sleep(60*60)# Check every hr
