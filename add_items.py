import f1,pickle,price_detect

def start():
    f=open('registration.txt','rb')
    while True:
        try:
            obj=pickle.load(f)
            u_agent=obj.send_uagent()
            u_agent={"User-Agent":u_agent}
            email=obj.send_mail()
        except EOFError:
            break
    
    f.close()
    # opening amazon file
    f=open('additem_amazon.txt','rb')
    while True:
        try:
            obj=pickle.load(f)
            url=obj.send_url()
            price=obj.send_price()
            name=obj.send_name()
            price_detect.check_price_amazon(url,u_agent,price,email,name)
        
        except EOFError:
            print("End of file-amazon")
            break
    f.close()
    
    # opening flipkart file
    f=open('additem_flipkart.txt','rb')
    while True:
        try:
            obj=pickle.load(f)
            url=obj.send_url()
            price=obj.send_price()
            name=obj.send_name()
            price_detect.check_price_flipkart(url,u_agent,price,email,name)
        
        except EOFError:
            print("End of file-flipkart")
            break
    f.close()


