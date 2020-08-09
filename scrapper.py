import requests
from bs4 import BeautifulSoup
import smtplib




URL='https://www.amazon.in/Philips-94-Portable-Wireless-Bluetooth/dp/B075YPH9YZ/ref=sr_1_2?crid=2MAIQGSXIYMSA&dchild=1&keywords=philips+bluetooth+speaker&qid=1596946046&sprefix=philips+blue%2Caps%2C331&sr=8-2'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36' }

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    print(soup.prettify())

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = int(price[1:5])


    if (price < 1200):
        send_mail()

    if (price > 1200):
        send_mail()



def send_mail():
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('*******@gmail.com','*******')


    subject ='Hey ! Price fell down !'
    body ='Check amazon link : https://www.amazon.in/Philips-94-Portable-Wireless-Bluetooth/dp/B075YPH9YZ/ref=sr_1_2?crid=2MAIQGSXIYMSA&dchild=1&keywords=philips+bluetooth+speaker&qid=1596946046&sprefix=philips+blue%2Caps%2C331&sr=8-2'

    msg= f"Subject : {subject}\n\n{body}"

    server.sendmail(
        '********@gmail.com',
        '********@outlook.com',
        msg)

    print('Email Has been sent !!')

    server.quit()


check_price()






