import pickle
from tkinter import *
import modify,add_items2



def create_table(f,s,r,frame):
    rows=0
    while True:
        try:
            obj=pickle.load(f)
            rows+=1
        except EOFError:
            break
    f.seek(0)
    e=Entry(frame,width=20,fg='red',bg='green',font=('Arial',16,'bold'))
    e.place(x=50,y=100+r*30)
    e.insert(END,s)
    e=Entry(frame,width=20,fg='red',bg='green',font=('Arial',16,'bold'))
    e.place(x=300,y=100+r*30)
    e.insert(END,'Set Price')
    i=0
    for i in range(r+1,r+rows+1):    
        obj=pickle.load(f)
        p_name=obj.send_name()
        price=obj.send_price()
        
        e=Entry(frame,width=20,fg='blue',font=('Arial',16,'bold'))
        e.place(x=50,y=100+i*30)
        e.insert(END,p_name)
        e=Entry(frame,width=20,fg='blue',font=('Arial',16,'bold'))
        e.place(x=300,y=100+i*30)
        e.insert(END,price)     
        print(p_name)
    return i
  


def show_item(root,f):
    f.destroy()
    root.title('show item')
    frame=Frame(root,height=600,width=800,bg='orange')
    frame.propagate(0)
    frame.pack()
    def click(num):
        if num==1:
            modify.show_list(root,frame)
        elif num==2:
            add_items2.show(root,frame)
    l=Label(frame,text="Added Items",width=20,height=1,font=('Courier', -30, 'bold underline'),fg='red',bg='yellow')
    l.place(x=100,y=30)
    r=0
    f=open('additem_amazon.txt','rb')
    s='Amazon Product'
    r=create_table(f,s,r,frame)
    f.close()
    f=open('additem_flipkart.txt','rb')
    s='Flipkart Product'
    r=create_table(f,s,r+1,frame)
    f.close() 
    b1=Button(frame,text="Modify",bg='yellow',fg='blue',command=lambda:click(1))
    b2=Button(frame,text="Add New Item",bg='yellow',fg='blue',command=lambda:click(2))
    b1.pack()
    b2.pack()
    b1.place(x=600,y=500)
    b2.place(x=600,y=550)
   
    root.mainloop()