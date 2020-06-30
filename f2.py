import f1,pickle,add_items2,f3
from tkinter import *



def Registration(root,f):
    
    f.destroy()
    root.title('Registration')
    frame=Frame(root,height=600,width=800,bg='SeaGreen')
    frame.propagate(0)
    frame.pack()
    
    def store(event):
        name=name1.get()
        email=email1.get()
        password=password1.get()
        u_agent=u_agent1.get()
        
        f=open('registration.txt','wb')
        e=f1.Register(name,email,password,u_agent)
        pickle.dump(e,f)
        f.close()
        print("Submit Done")
        add_items2.show(root,frame)
    
    
    
    name=Label(frame,text="Enter name: ",font=('Courier',-20,'bold'))
    email=Label(frame,text="Enter Email: ",font=('Courier',-20,'bold'))
    password=Label(frame,text="Email's password: ",font=('Courier',-20,'bold'))
    u_agent=Label(frame,text="Enter user agent: ",font=('Courier',-20,'bold')) 
    l=Label(frame,text="Register Here",width=25,height=2,font=('Courier', -30, 'bold underline'),fg='red',bg='yellow')
    
    
    
    name1=Entry(frame,width=25,fg='blue',bg='yellow',font=('Arial',14))
    email1=Entry(frame,width=25,fg='blue',bg='yellow',font=('Arial',14))
    password1=Entry(frame,width=45,fg='blue',bg='yellow',show='*')
    u_agent1=Entry(frame,width=25,fg='blue',bg='yellow',font=('Arial',14))
    
    
    
    name.place(x=100,y=150)
    name1.place(x=340,y=150)
    email.place(x=100,y=200)
    email1.place(x=340,y=200)
    password.place(x=100,y=250)
    password1.place(x=340,y=250)
    u_agent.place(x=100,y=300)
    u_agent1.place(x=340,y=300)
    l.place(x=200,y=20)
    
    u_agent1.bind("<Return>",store)
    
    root.mainloop()
    #add_items2.show(root,frame)

def Add_item_amazon(root,f):
    f.destroy()
    root.title('amazon item')
    frame=Frame(root,height=600,width=800,bg='ivory')
    frame.propagate(0)
    frame.pack()
    
    def gonext(num):
            if num==1:
                add_items2.show(root,frame) 
            elif num==2:
                f3.show_item(root,frame)
          
    def store(event):
        
        f=open('additem_amazon.txt','ab')
        p_name=p_name1.get()
        url=url1.get()
        price=float(price1.get())
        e=f1.Product(p_name,url,price)
        pickle.dump(e,f)
        f.close()
        print("Product added")
        b1=Button(frame,text='Add More',bg='yellow',fg='blue',activebackground='red',activeforeground='black',command=lambda:gonext(1))
        b1.pack()
        b1.place(x=500,y=300)
        b2=Button(frame,text='View Items',bg='yellow',fg='blue',activebackground='red',activeforeground='black',command=lambda:gonext(2))
        b2.pack()
        b2.place(x=500,y=350)
    p_name=Label(frame,text="Enter product name: ",font=('Courier',-20,'bold'))
    url=Label(frame,text="Enter product url: ",font=('Courier',-20,'bold'))
    price=Label(frame,text="Enter your price: ",font=('Courier',-20,'bold'))
    l=Label(frame,text="Enter all the details",width=25,height=2,font=('Courier', -30, 'bold underline'),fg='red',bg='yellow')
    
    p_name1=Entry(frame,width=25,fg='blue',bg='yellow',font=('Arial',14))
    url1=Entry(frame,width=25,fg='blue',bg='yellow',font=('Arial',14))
    price1=Entry(frame,width=25,fg='blue',bg='yellow',font=('Arial',14))
    
    l.place(x=200,y=20)
    p_name.place(x=100,y=150)
    p_name1.place(x=350,y=150)
    url.place(x=100,y=200)
    url1.place(x=350,y=200)
    price.place(x=100,y=250)
    price1.place(x=350,y=250)
    price1.bind("<Return>",store)
    root.mainloop()
    
        
def Add_item_flipkart(root,f):
    f.destroy()
    root.title('flipkart Item')
    frame=Frame(root,height=600,width=800,bg='DeepSkyBlue')
    frame.propagate(0)
    frame.pack()
    
    def gonext(num):
            if num==1:
                add_items2.show(root,frame)
            elif num==2:
                f3.show_item(root,frame)
    def store(event):
        f=open('additem_flipkart.txt','ab')
        p_name=p_name1.get()
        url=url1.get()
        price=float(price1.get())
        e=f1.Product(p_name,url,price)
        pickle.dump(e,f)
        f.close()
        b2=Button(frame,text='View Items',bg='yellow',fg='blue',activebackground='red',activeforeground='black',command=lambda:gonext(2))
        b2.pack()
        b2.place(x=500,y=350)
        print("Product added")
        
        b1=Button(frame,text='Add More',bg='yellow',fg='blue',activebackground='red',activeforeground='black',command=lambda:gonext(1))
        b1.pack()
        b1.place(x=500,y=300)
    p_name=Label(frame,text="Enter product name: ",font=('Courier',-20,'bold'))
    url=Label(frame,text="Enter product url: ",font=('Courier',-20,'bold'))
    price=Label(frame,text="Enter your price: ",font=('Courier',-20,'bold'))
    l=Label(frame,text="Enter all the details",width=25,height=2,font=('Courier', -30, 'bold underline'),fg='red',bg='yellow')
    
    p_name1=Entry(frame,width=25,fg='blue',bg='yellow',font=('Arial',14))
    url1=Entry(frame,width=25,fg='blue',bg='yellow',font=('Arial',14))
    price1=Entry(frame,width=25,fg='blue',bg='yellow',font=('Arial',14))
    
    l.place(x=200,y=20)
    p_name.place(x=100,y=150)
    p_name1.place(x=350,y=150)
    url.place(x=100,y=200)
    url1.place(x=350,y=200)
    price.place(x=100,y=250)
    price1.place(x=350,y=250)
    price1.bind("<Return>",store)
    root.mainloop()

    
    
