from tkinter import *
import f2,f3

def show(root,f):
    f.destroy()
    root.title('Options')
    frame=Frame(root,height=600,width=800,bg='PeachPuff')
    frame.propagate(0)
    frame.pack()
    def select(num):
        if num==1:
            f2.Add_item_amazon(root,frame)
            
        elif num==2:
            f2.Add_item_flipkart(root,frame)
        elif num==3:
            f3.show_item(root,frame)
            
    
    
    b1=Button(frame,text='Add',height=2,width=15,bg='yellow',fg='blue',activebackground='red',activeforeground='black',command=lambda:select(1))
    b2=Button(frame,text='Add',height=2,width=15,bg='yellow',fg='blue',activebackground='red',activeforeground='black',command=lambda:select(2))
    b3=Button(frame,text='Back',height=2,width=15,bg='yellow',fg='blue',activebackground='red',activeforeground='black',command=lambda:select(3))
    b1.pack()
    b2.pack() 
    b3.pack()
    l1=Message(frame,text="Add Amazon Product: ",width=300,font=('Roman',20,'bold italic'),fg='green')
    l2=Message(frame,text="Add Flipkart Product: ",width=300,font=('Roman',20,'bold italic'),fg='green')
    l3=Label(frame,text="Choose your Cart",width=25,height=1,font=('Courier',-30,'bold'),fg='red',bg='AliceBlue')
    
    l1.place(x=100,y=150)
    b1.place(x=400,y=150)
    b3.place(x=500,y=400)
    l2.place(x=100,y=250)
    b2.place(x=400,y=250)
    l3.place(x=150,y=70)
    
    
    root.mainloop()
    