import requests
from bs4 import BeautifulSoup
import smtplib


def check_price_amazon(url,u_agent,price,email,name):
    page = requests.get(url,headers=u_agent)
    soup = BeautifulSoup(page.content,'html.parser')
    lprice=soup.find(id="priceblock_ourprice")
    if not lprice:
        print("no price available")
    else:
        lprice=lprice.getText() 
        l=[]
        for i in lprice:
            if i=='.':
                break
            elif i.isnumeric():
                l.append(i)
        converted_price=float(''.join(l))
        if converted_price<=price:
            send_mail(url,email,name,converted_price)
            print('mail sent amazon')
        
        
def check_price_flipkart(url,u_agent,price,email,name):
    page = requests.get(url,headers=u_agent)
    soup = BeautifulSoup(page.content,'html.parser')
   
    price=soup.find("div",attrs={'class':"_1vC4OE _3qQ9m1"})
    
    l=[]
    if not price:
        print('No price available')
    else:
        price=price.getText()
        for i in price:
            if i=='.':
                break
            
            elif i.isnumeric():
                l.append(i)
        converted_price=float(''.join(l))
        if converted_price<11000:
            send_mail(url,email,name,converted_price)
            print('mail sent flipkart')
        


def send_mail(url,email,name,price):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('myselfsubha99@gmail.com','snxlfhcgullrffwx')
    subject="Price fell Down"
    body='Price fall down..\n Check the link\n'+url
    body='Price Fall Down for :'+name+'\n\n New Price is: '+str(price)+'\n\nCheck the below link:\n'+url
    msg=f"Subject: {subject}\n\n{body}"
    server.sendmail('myselfsubha99@gmail.com',email,msg) 
    print("Hey ..email has been sent")
    server.quit()
    


    
