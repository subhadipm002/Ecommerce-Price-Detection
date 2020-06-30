import pickle

class Register:
    def __init__(self,name,email,password,u_agent):
        self.name=name
        self.email=email
        self.password=password
        self.u_agent=u_agent
    def send_uagent(self):
        return self.u_agent
    def send_mail(self):
        return self.email
        
class Product:
    def __init__(self,p_name,url,price):
        self.p_name=p_name
        self.url=url
        self.price=price
        
    def send_name(self):
        return self.p_name
    def send_url(self):
        return self.url
    def send_price(self):
        return self.price
        

        
        
    
        
