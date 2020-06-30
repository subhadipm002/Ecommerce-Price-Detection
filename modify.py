from tkinter import *
import pickle,f1,f3
import os


updateprice=-10
def show_list(root,f):
    f.destroy()
    root.title('Modify')
    frame=Frame(root,height=600,width=800,bg='yellow')
    frame.propagate(0)
    frame.pack()

    
    
    f11=open('additem_amazon.txt','rb')
    f12=open('additem_flipkart.txt','rb')
    rows_amazon=0
    rows_flipkart=0
    while True:
        try:
            obj=pickle.load(f11)
            rows_amazon+=1
        except EOFError:
            break
    f11.close()  
    while True:
        try:
            obj=pickle.load(f12)
            rows_flipkart+=1
        except EOFError:
            break
    f12.close()
    def on_select(event):
        index1=''
        index2=''
        index1=lb.curselection()
        index2=lb1.curselection()
        value1=[]
        value2=[]
        val=''
        if index1:
            value1.append(int(index1[0]))
            val=value1[0]
        
        elif index2:
            value2.append(int(index2[0]))
            val=value2[0]
        def click(num):
            if num==1:
                
                if value1:
                    print('selection done')
                    f=open('additem_amazon.txt','rb')
                elif value2:
                    print('selection done')
                    f=open('additem_flipkart.txt','rb')
                print('selection cancel')
                print(value2)
                for i in range(val+1):
                    obj1=pickle.load(f)
                s=obj1.send_name()
                print(s)
                f.seek(0)
                f13=open('file1.txt','wb')
                while(True):
                    try:
                        obj2=pickle.load(f)
                        p_name=obj2.send_name()
                        if p_name!=s:
                            pickle.dump(obj2,f13)
                    except EOFError:
                        break
                f.close()
                f13.close()
                if value1:
                    os.remove('additem_amazon.txt')
                    os.rename('file1.txt','additem_amazon.txt')
                elif value2:
                    os.remove('additem_flipkart.txt')
                    os.rename('file1.txt','additem_flipkart.txt')
                    
                        
            elif num==2:
                
                def store(event):
                    price=float(price1.get())
                    print("inside updateprice is: ",price)
                    if value1:
                        f=open('additem_amazon.txt','rb')
                    elif value2:
                        f=open('additem_flipkart.txt','rb')
                    f13=open('file2.txt','wb')
                    i=0
                    while(True):
                        try:
                            i+=1
                            print(i)
                            obj=pickle.load(f)
                            if i==val+1:
                                name=obj.send_name()
                                url=obj.send_url()
                                e=f1.Product(name,url,price)
                                pickle.dump(e,f13)
                                print('dumping done')
                                
                            else:
                                pickle.dump(obj,f13)
                           
                        except EOFError:
                            break
                    f.close()
                    f13.close()
                    if value1:
                        os.remove('additem_amazon.txt')
                        os.rename('file2.txt','additem_amazon.txt')
                    elif value2:
                        os.remove('additem_flipkart.txt')
                        os.rename('file2.txt','additem_flipkart.txt')
                    f3.show_item(root,frame)
                
                price1=Entry(frame,width=25,fg='blue',bg='red',font=('Arial',14))
                price1.place(x=400,y=500)
                t1=Message(frame,text='Enter Price:',width=200,font=('Verdana',14,'bold'),fg='blue')
                t1.place(x=200,y=495)
                price1.bind("<Return>",store)
                print('update price: ',updateprice)
                
                
                
                
        b1=Button(frame,text="Remove",fg='white',bg='red',command=lambda:click(1))
        b2=Button(frame,text="Update Price",bg='red',fg='white',command=lambda:click(2))
        b1.pack()
        b2.pack()
        b1.place(x=650,y=300)
        b2.place(x=650,y=350)  
        
        
    
    lb=Listbox(frame, font="Arial 12 bold",fg='red',bg='blue',height=rows_amazon,selectmode=SINGLE)
    lb.place(x=100,y=100)
    l1=Label(frame,text="AMAZON",width=20,height=1,font=('Courier', -30),fg='red',bg='yellow')
    l1.place(x=10,y=50)
    f=open('additem_amazon.txt','rb')
    while True:
        try:
            obj=pickle.load(f)
            p_name=obj.send_name()
            print(p_name)
            lb.insert(END,p_name)
        except EOFError:
            break
    f.close()
    lb1=Listbox(frame, font="Arial 12 bold",fg='red',bg='blue',height=rows_flipkart,selectmode=SINGLE)
    lb1.place(x=350,y=100)
    l2=Label(frame,text="FLIPKART",width=20,height=1,font=('Courier', -30),fg='red',bg='yellow')
    l2.place(x=250,y=50)
    f=open('additem_flipkart.txt','rb')
    while True:
        try:
            obj=pickle.load(f)
            p_name=obj.send_name()
            print(p_name)
            lb1.insert(END,p_name)
        except EOFError:
            break
    f.close()
    lb.bind('<<ListboxSelect>>',on_select)
    lb1.bind('<<ListboxSelect>>',on_select)
    def buttonclick():
        f3.show_item(root,frame)
    b4=Button(frame,text="Back",fg='white',bg='red',command=buttonclick)
    b4.pack()
    b4.place(x=650,y=400)
    root.mainloop()
    

