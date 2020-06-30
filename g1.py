f=open('additem_flipkart.txt','ab')
f1=open('additem_amazon.txt','ab')
f2=open('registration.txt','ab')
f.close()
f1.close()
f2.close()
from tkinter import *
import f2,add_items2,f3,add_items



add_items.start()  # to check price and sent email
root=Tk()
f=Frame(root,height=600,width=800,bg='orchid')
root.title("Start")
f.propagate(0)
f.pack()

l=Label(f,text="Welcome to Price Detection",width=30,height=1,font=('Courier',-30,'bold'),fg='red',bg='yellow')
l.place(x=130,y=30)
t1=Message(f,text='Register Here:',width=200,font=('Verdana',14,'bold'),fg='blue')
t1.place(x=200,y=125)
t2=Message(f,text='Add Product:',width=200,font=('Verdana',14,'bold'),fg='blue')
t2.place(x=215,y=190)

t3=Message(f,text='View Added Items:',width=300,font=('Verdana',14,'bold'),fg='blue')
t3.place(x=145,y=255)
def click(num):
    if num==1:
        f2.Registration(root,f)
    elif num==2:
        add_items2.show(root,f)
    elif num==3:
         f3.show_item(root,f)
        
        
b1=Button(f,text='Register',width=17,height=2,bg='yellow',fg='blue',activebackground='red',activeforeground='black',command=lambda:click(1))
b2=Button(f,text='Add Items',width=17,height=2,bg='yellow',fg='blue',activebackground='red',activeforeground='black',command=lambda:click(2))
b3=Button(f,text='View',bg='yellow',width=17,height=2,fg='blue',activebackground='red',activeforeground='black',command=lambda:click(3))
b1.pack()
b2.pack()
b3.pack()
b1.place(x=400,y=125)
b2.place(x=400,y=190)
b3.place(x=400,y=255)

print("Success")
root.mainloop()