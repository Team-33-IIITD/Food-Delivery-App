from tkinter import *
import mysql.connector 
from datetime import date
import time as tm

root = Tk()
root.geometry('900x700')
root.title("HomePage")
root.configure(bg='black')


class AddComplaint(Toplevel):
    c_type=IntVar()
    c_desc= StringVar()
    c_execid=-1
    order_id=StringVar()
    conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")

    def database(self):

        cursor=self.conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM Complaints')
        records = cursor.fetchall()
        for row in records:
            n = int(row[0])
        n=n+1
        com_id=str(n)

        cursor.execute('SELECT com_id,status FROM ComplaintExecutive')
        records=cursor.fetchall()
        
        for row in records:
            if row[1]=="Not Active":
                c_execid=row[0]
                cursor.execute(f"UPDATE ComplaintExecutive SET active='Active' WHERE ComId={row[0]}")
                self.conn.commit()
                break
        cursor.execute('INSERT INTO Complaints (com_id,com_type,description,cust_id,exec_id,order_id,status) VALUES (%s,"%s","%s",%s,%s,%s,"%s")' % (n,self.c_type,self.c_desc,self.cust_id,self.c_execid,self.order_id.get(),"OPEN"))
        self.conn.commit()
        self.conn.close()


    
    
    def __init__(self,cust_id):
        Toplevel.__init__(self)
        self.geometry('500x600')

        self.cust_id=cust_id

        self.label_0= Label(self,text="Complaint Center",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)

        self.label_1= Label(self,text=f"Registering Complaint for Order ID: ",width=20,font=("bold",15))
        self.label_1.place(x=90,y=100)

        self.entry_0 = Entry(self,textvar=self.order_id)
        self.entry_0.place(x=240,y=150)

        self.label_2= Label(self,text="Complaint Type",width=20,font=("bold", 10))
        self.label_2.place(x=80,y=150)

        self.entry_1 = Entry(self,textvar=self.c_type)
        self.entry_1.place(x=240,y=150)

        self.label_3= Label(self,text="Complaint Description",width=20,font=("bold", 10))
        self.label_3.place(x=80,y=230)
        
        self.entry_2 = Entry(self,textvar=self.c_desc)
        self.entry_2.place(x=240,y=230)

        Button(self,text='Submit',width=20,bg='brown',fg='white',command=self.database).place(x=180,y=300)


class complaintexec(Toplevel):
    comname = StringVar()
    comemail = StringVar()
    comph = StringVar()
    pas = StringVar()
    activestatus=StringVar()
    conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
    def database(self):
       name1=self.comname.get()
       email=self.comemail.get()
       phone=self.comph.get()
       password = self.pas.get()
       active_status = "active"
       cursor=self.conn.cursor()
       cursor.execute('SELECT COUNT(*) FROM ComplaintExecutive')
       records = cursor.fetchall()
       for row in records:
            n = int(row[0])
       n=n+1
       if phone.isdigit():
           cursor.execute('INSERT INTO ComplaintExecutive (exec_id,exec_name,active,email,password,phone) VALUES(%s,%s,%s,%s,%s,%s)' % (n,name1,active_status,email,password,phone))
           self.conn.commit()
           self.confirm = Label(self, text="Complaint Executive Registered!",width=30,font=("bold", 10))
           self.confirm.place(x=120,y=460)
           cursor.close()
           conn.close()
       else:
           self.inv = Label(self, text="Invalid phone",width=30,font=("bold", 10))
           self.inv.place(x=120,y=460)
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('500x600')
        self.label_0 = Label(self, text="Complaint Exec SignUp",width=20,font=("bold", 20))
        self.label_0.place(x=70,y=53)


        self.label_1 = Label(self, text="Complaint Executive Name",width=20,font=("bold", 10))
        self.label_1.place(x=60,y=130)

        self.entry_1 = Entry(self,textvar=self.comname)
        self.entry_1.place(x=240,y=130)

        self.label_2 = Label(self, text="Complaint Executive Email",width=20,font=("bold", 10))
        self.label_2.place(x=60,y=180)

        self.entry_2 = Entry(self,textvar=self.comemail)
        self.entry_2.place(x=240,y=180)

        self.label_3 = Label(self, text="Complaint Executive Phone Number",width=30,font=("bold", 10))
        self.label_3.place(x=10,y=230)
        self.entry_3 = Entry(self,textvar=self.comph)
        self.entry_3.place(x=240,y=230)
        self.label_5 = Label(self, text="Password",width=20,font=("bold", 10))
        self.label_5.place(x=70,y=320)
        self.entry_5 = Entry(self,show="*",textvar=self.pas)
        self.entry_5.place(x=240,y=320)
        Button(self, text='Submit',width=20,bg='brown',fg='white',command=self.database).place(x=180,y=420)


class deliveryexec(Toplevel):
    delname = StringVar()
    delemail = StringVar()
    delph = StringVar()
    delage = StringVar()
    pas = StringVar()
    activestatus=StringVar()
    conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
    def database(self):
       name1=self.delname.get()
       email=self.delemail.get()
       phone=self.delph.get()
       age=self.delage.get()
       password = self.pas.get()
       active_status = "free"
       cursor=self.conn.cursor()
       cursor.execute('SELECT COUNT(*) FROM DeliveryExecutive')
       records = cursor.fetchall()
       for row in records:
            n = int(row[0])
       n=n+1
       phot = "https://image.shutterstock.com/image-photo/casually-handsome-confident-young-man-260nw-439433326.jpg"
       ords=-1
       if delph.isdigit() and delage.isdigit():
           cursor.execute('INSERT INTO DeliveryExecutive (del_id,del_name,del_phone,del_age,del_image,activity_status,order_id,email,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)' % (n,name1,phone,age,phot,active_status,ords,email,password))
           self.conn.commit()
           self.confirm = Label(self, text="Delivery Executive Registered!",width=30,font=("bold", 10))
           self.confirm.place(x=120,y=460)
           cursor.close()
           conn.close()
       else:
           self.inv = Label(self, text="Invalid entries",width=30,font=("bold", 10))
           self.inv.place(x=120,y=460)
       
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('500x600')
        self.label_0 = Label(self, text="Delivery Executive SignUp",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)


        self.label_1 = Label(self, text="Delivery Executive Name",width=20,font=("bold", 10))
        self.label_1.place(x=80,y=130)

        self.entry_1 = Entry(self,textvar=self.delname)
        self.entry_1.place(x=240,y=130)

        self.label_2 = Label(self, text="Delivery Executive Email",width=20,font=("bold", 10))
        self.label_2.place(x=68,y=180)

        self.entry_2 = Entry(self,textvar=self.delemail)
        self.entry_2.place(x=240,y=180)

        self.label_3 = Label(self, text="Delivery Executive Phone Number",width=30,font=("bold", 10))
        self.label_3.place(x=15,y=230)
        self.entry_3 = Entry(self,textvar=self.delph)
        self.entry_3.place(x=240,y=230)
        self.label_4 = Label(self, text="Delivery Executive Age",width=30,font=("bold", 10))
        self.label_4.place(x=40,y=280)
        self.entry_4 = Entry(self,textvar=self.delage)
        self.entry_4.place(x=240,y=280)
        self.label_5 = Label(self, text="Password",width=20,font=("bold", 10))
        self.label_5.place(x=70,y=320)
        self.entry_5 = Entry(self,show="*",textvar=self.pas)
        self.entry_5.place(x=240,y=320)
        Button(self, text='Submit',width=20,bg='brown',fg='white',command=self.database).place(x=180,y=420)
        #cursor.close()
        #conn.close()


class restaurant(Toplevel):
    restname=StringVar()
    #ownername=StringVar()
    restemail=StringVar()
    restph = StringVar()
    restadd=StringVar()
    pas = StringVar()
    rest_type=StringVar()
    open_time=StringVar()
    close_time=StringVar()
    availability=StringVar()
    conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
    def database(self):
       if not str(self.restph.get()).isdigit():
           self.label_0 = Label(self, text="Phone Invalid",width=10,font=("bold", 20))
           self.label_0.place(x=180,y=500)
       else:
           name1=self.restname.get()
           email=self.restemail.get()
           phone=self.restph.get()
           address=self.restadd.get()
           type1=self.rest_type.get()
           password = self.pas.get()
           opentime = self.open_time.get()
           closetime = self.close_time.get()
           #available_status = self.availablity.get()
           current_time = tm.strftime('%H:%M:%S')
           #print(current_time)
           hr = int(current_time[0:2])
           mins = int(current_time[3:5])
           hr1 = int(opentime[0:2])
           mins1 = int(opentime[3:5])
           hr2 = int(closetime[0:2])
           mins2 = int(closetime[3:5])
           #print(hr)
           #if hr>12:
              #dur='PM'
           #else:
              #dur='AM'
           #if hr>12:
              #print(str(hr-12)+":"+current_time[3:5]+" "+dur)
           #else:
              #print(str(hr)+current_time[3:5]+" "+dur)
           if hr<hr1:
               available_status="closed"
           elif hr==hr1 and mins<mins1:
               available_status="closed"
           elif hr>hr2:
               available_status="closed"
           elif hr==hr2 and mins>mins2:
               available_status="closed"
           else:
               available_status="open"
               
           #available_status = "available"
           avg_price=0
           rating1=0.0
           img1="https://image.shutterstock.com/image-photo/casually-handsome-confident-young-man-260nw-439433326.jpg"
           cursor=self.conn.cursor()
           cursor.execute('SELECT COUNT(*) FROM Restaurants')
           records = cursor.fetchall()
           for row in records:
                n = int(row[0])
           n=n+1
           cursor.execute('SELECT COUNT(*) FROM Restaurants WHERE email = %s' % (email))
           records = cursor.fetchall()
           for row in records:
                n1 = int(row[0])
           cursor.execute('SELECT COUNT(*) FROM Restaurants WHERE rest_phone = %s' % (phone))
           records = cursor.fetchall()
           for row in records:
                n2 = int(row[0])
           #custid=str(n)
           if n1==0 and n2==0:
               cursor.execute('INSERT INTO Restaurants (rest_id,rest_name,rest_phone,rest_add,rest_image,avg_price,rating,rest_type,availability,open_time,close_time,email,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' % (n,name1,phone,address,img1,avg_price,rating1,type1,available_status,opentime,closetime,email,password))
               self.conn.commit()
               self.confirm = Label(self, text="Restaurant Registered!",width=20,font=("bold", 10))
               self.confirm.place(x=180,y=560)
           else:
               self.inv = Label(self, text="Email/Phone number already taken",width=20,font=("bold", 10))
               self.inv.place(x=180,y=560)
           cursor.close()
           conn.close()
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('500x600')
        self.label_0 = Label(self, text="Restaurant SignUp",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)


        self.label_1 = Label(self, text="Name",width=20,font=("bold", 10))
        self.label_1.place(x=80,y=130)

        self.entry_1 = Entry(self,textvar=self.restname)
        self.entry_1.place(x=240,y=130)

        self.label_2 = Label(self, text="Email",width=20,font=("bold", 10))
        self.label_2.place(x=68,y=180)

        self.entry_2 = Entry(self,textvar=self.restemail)
        self.entry_2.place(x=240,y=180)

        self.label_3 = Label(self, text="Phone Number",width=20,font=("bold", 10))
        self.label_3.place(x=70,y=230)
        self.entry_3 = Entry(self,textvar=self.restph)
        self.entry_3.place(x=240,y=230)
        self.label_4 = Label(self, text="Address",width=20,font=("bold", 10))
        self.label_4.place(x=70,y=280)
        self.entry_4 = Entry(self,textvar=self.restadd)
        self.entry_4.place(x=240,y=280)

        self.label_5 = Label(self, text="Type",width=20,font=("bold", 10))
        self.label_5.place(x=85,y=330)
        self.entry_5 = Entry(self,textvar=self.rest_type)
        self.entry_5.place(x=240,y=330)
        self.label_6 = Label(self, text="Password",width=20,font=("bold", 10))
        self.label_6.place(x=85,y=380)
        self.entry_6 = Entry(self,show="*",textvar=self.pas)
        self.entry_6.place(x=240,y=380)

        self.label_7 = Label(self, text="Open Time (Enter in military-time)",width=20,font=("bold", 10))
        self.label_7.place(x=85,y=430)
        self.entry_7 = Entry(self,textvar=self.open_time)
        self.entry_7.place(x=240,y=430)

        self.label_8 = Label(self, text="Close Time (Enter in military-time)",width=20,font=("bold", 10))
        self.label_8.place(x=85,y=480)
        self.entry_8 = Entry(self,textvar=self.close_time)
        self.entry_8.place(x=240,y=480)
        Button(self, text='Submit',width=20,bg='brown',fg='white',command=self.database).place(x=180,y=520)
        


# Homepage with Customer Sign Up linked with database
class customer(Toplevel):
    Fullname=StringVar()
    Email=StringVar()
    phonenum = StringVar()
    add=StringVar()
    mem= StringVar()
    pas = StringVar()
    coupid = IntVar()
    conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
    def database(self):
       #print(str(self.phonenum.get()))
       if not str(self.phonenum.get()).isdigit():
           self.label_0 = Label(self, text="Phone Invalid",width=10,font=("bold", 20))
           self.label_0.place(x=180,y=500)
       else:     
           name1=self.Fullname.get()
           email=self.Email.get()
           phone=self.phonenum.get()
           address=self.add.get()
           membership=self.mem.get()
           password = self.pas.get()
           cid = self.coupid.get()
           cursor=self.conn.cursor()
           cursor.execute('SELECT COUNT(*) FROM Customers')
           records = cursor.fetchall()
           for row in records:
                n = int(row[0])
           n=n+1
           custid=str(n)
           cursor.execute('SELECT COUNT(*) FROM Customers WHERE cust_email = %s',(email,))
           records = cursor.fetchall()
           for row in records:
                n1 = int(row[0])
           
           if n1==0:
               cursor.execute('INSERT INTO Customers (cust_id,cust_name,cust_add,cust_email,cust_membership,password,cust_phone,coup_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',(n,name1,address,email,membership,password,phone,cid))
               self.conn.commit()
           else:
               #print("hello")
               self.label_inv = Label(self, text="Email already exists",width=20,font=("bold", 20))
               self.label_inv.place(x=180,y=500)

    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('500x600')
        self.label_0 = Label(self, text="Customer SignUp",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)


        self.label_1 = Label(self, text="FullName",width=20,font=("bold", 10))
        self.label_1.place(x=80,y=130)

        self.entry_1 = Entry(self,textvar=self.Fullname)
        self.entry_1.place(x=240,y=130)

        self.label_2 = Label(self, text="Email",width=20,font=("bold", 10))
        self.label_2.place(x=68,y=180)

        self.entry_2 = Entry(self,textvar=self.Email)
        self.entry_2.place(x=240,y=180)

        self.label_3 = Label(self, text="Phone Number",width=20,font=("bold", 10))
        self.label_3.place(x=70,y=230)
        self.entry_3 = Entry(self,textvar=self.phonenum)
        self.entry_3.place(x=240,y=230)
        
        self.label_4 = Label(self, text="Address",width=20,font=("bold", 10))
        self.label_4.place(x=70,y=280)
        self.entry_4 = Entry(self,textvar=self.add)
        self.entry_4.place(x=240,y=280)

        self.label_5 = Label(self, text="Membership",width=20,font=("bold", 10))
        self.label_5.place(x=85,y=330)
        self.cb1 = Checkbutton(self, text ='Gold', variable=self.mem, takefocus = 0).place(x = 240, y = 330) 

        self.label_6 = Label(self, text="Password",width=20,font=("bold", 10))
        self.label_6.place(x=85,y=380)
        self.entry_6 = Entry(self,show="*",textvar=self.pas)
        self.entry_6.place(x=240,y=380)

        self.label_7 = Label(self, text="Coupon ID",width=20,font=("bold", 10))
        self.label_7.place(x=85,y=430)
        self.entry_7 = Entry(self,textvar=self.coupid)
        self.entry_7.place(x=240,y=430)
        
        Button(self, text='Submit',width=20,bg='brown',fg='white',command=self.database).place(x=180,y=480)
        
        
        #Button(self, text='Restraunt SignUp',width=20,bg='brown',fg='white',command=self.rest).place(x=200,y=490)
class CustCurrentOrder(Toplevel):
    exists=False

    def __init__(self,order_id):
        Toplevel.__init__(self)
        self.geometry('500x600')

        conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
        cursor=conn.cursor()

        cursor.execute(f"SELECT * FROM Orders WHERE order_id= %s" % order_id)
        records=cursor.fetchall()

        self.label_0= Label(self,text="Current Order Details",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)

        if(len(records)==0):
            self.label_1= Label(self,text="No valid current order",width=20,font=("bold", 10))
            self.label_1.place(x=90,y=100)
        else:
            row=records[0]
            self.label_2= Label(self,text=f"order Number:{row[0]}",width=20,font=("bold", 10))
            self.label_2.place(x=90,y=100)

            cursor.execute(f"SELECT del_name from DeliveryExecutive WHERE del_id={row[2]}") 
            recs= cursor.fetchall()
            
            self.label_3= Label(self,text=f"Delivered by {recs[0][0]}",width=100,font=("bold", 10))
            self.label_3.place(x=90,y=130)

            cursor.execute(f"SELECT rest_name from Restaurants WHERE rest_id={row[3]}") 
            recs= cursor.fetchall()
            
            self.label_4= Label(self,text=f"Restaurant providing the food {recs[0][0]}",width=100,font=("bold", 10))
            self.label_4.place(x=90,y=160)

            cursor.execute(f"SELECT coup_code from Coupons WHERE coup_id={row[4]}") 
            recs= cursor.fetchall()
            
            self.label_5= Label(self,text=f"Coupon code applied {recs[0][0]}",width=100,font=("bold", 10))
            self.label_5.place(x=90,y=190)
            
            self.label_6= Label(self,text=f"Net Price: {row[5]}",width=100,font=("bold", 10))
            self.label_6.place(x=90,y=220)
            
            
            self.label_6= Label(self,text=f"Order Status: {row[6]}",width=100,font=("bold", 10))
            self.label_6.place(x=90,y=250)
            
            self.label_6= Label(self,text=f"Payment Status: {row[10]}",width=100,font=("bold", 10))
            self.label_6.place(x=90,y=280)

            self.label_7= Label(self,text="Dishes present in the order",width=100,font=("bold", 15))
            self.label_7.place(x=90,y=310)

            cursor.execute(f"select dish_name from Menu Natural Join Cart where Cart.order_id={row[0]};")
            recs = cursor.fetchall()

            self.labels=[]
            for x in range(len(recs)):
                self.labels.append( Label(self,text=f"{recs[x]}",width=100,font=("bold", 10)))
                self.labels[-1].place(x=90,y=310+30*x)
        conn.commit()
        conn.close()

class payment(Toplevel):
    itemid=StringVar()
    restid=""
    custid=""
    itemprice=""
    size=StringVar()
    quant=StringVar()
    r11=StringVar()
    address=StringVar()
    order_id=""
    netamount=""
    def confirm(self):
          conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
          cursor=conn.cursor()
          
          cursor.execute("Select net_price,coup_id from Orders where order_id=%s" % (self.order_id))
          recor=cursor.fetchall()
          self.netamount=float(recor[0][0])
          if(recor[0][1]==1):
            cursor.execute("Select count(order_id) from Orders where cust_id=%s and order_status not in ('Pending')" % (self.custid))
            rec=int(cursor.fetchall()[0][0])
            if(rec<=5):
                self.netamount=self.netamount*0.5
                self.label_1 = Label(self, text="Referral offer applied! 50 percent discount!",width=33,font=("bold", 25))
                self.label_1.place(x=300,y=500)
          cursor.execute("Select cust_membership from Customers where cust_id=%s" % (self.custid))
          rec=int(cursor.fetchall()[0][0])
          if(rec==1):
              self.netamount=self.netamount*0.8
              self.label_1 = Label(self, text="Referral offer applied! 20 percent discount!",width=33,font=("bold", 25))
              self.label_1.place(x=300,y=600)
         
          self.netamount=str(self.netamount)

          if(self.r11.get()=='1'):
            cursor.execute("Update Orders set destination='%s', payment_status='Paid Online' where order_id=%s" % (self.address.get(),self.order_id))
            cursor.execute("Insert into Payment (cust_id,order_id,mode,net_amount,confirmation) values('%s','%s','Online','%s','Payment Confirmed')" % (self.custid,self.order_id,self.netamount))
          else:
            cursor.execute("Update Orders set destination='%s', payment_status='COD' where order_id=%s" % (self.address.get(),self.order_id))
            cursor.execute("Insert into Payment (cust_id,order_id,mode,net_amount,confirmation) values('%s','%s','Cash','%s','Payment Pending')" % (self.custid,self.order_id,self.netamount))
          CustCurrentOrder(self.order_id)
          conn.commit()
          conn.close()
    def __init__(self,restid,custid,order_id):
          self.custid=custid
          self.restid=restid
          self.order_id=order_id
          Toplevel.__init__(self)
          # frm = Frame(root)
          # frm.pack(side=LEFT, padx=20) 
          self.geometry('1200x800')
          self.configure(bg='pink')
          conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
          cursor=conn.cursor()
          # print(restid)
          # print('SELECT * FROM Menu where rest_id='+restid)
          # # print('SELECT * FROM Menu where rest_id=%s',(str(restid)))
          # cursor.execute('SELECT * FROM Menu where rest_id='+restid)
          # records = cursor.fetchall()
          self.label_1 = Label(self, text="Payment Page",width=33,font=("bold", 25))
          self.label_1.place(x=300,y=50)
          self.label_1 = Label(self, text="Please select your preferred mode of payment",width=36,font=("bold", 23))
          self.label_1.place(x=300,y=120)
          self.r1=Radiobutton(self, text="Online: You'll be redirected to the bank page", padx = 50, pady=10, variable=self.r11, value=1)
          self.r2=Radiobutton(self, text="Cash", padx = 50, pady=10, variable=self.r11, value=0)
          # Radiobutton(master, text = text, variable = v, value = value).pack(side = TOP, ipady = 5) 
          self.r1.place(x=450,y=200)
          self.r2.place(x=550,y=270)
          self.label_1 = Label(self, text="Delivery Address",width=15,font=("bold", 13))
          self.label_1.place(x=560,y=350)
          self.entry_2 = Entry(self,textvar = self.address,width=60)
          self.entry_2.place(x=450,y=400)
          Button(self, text='Place Order',width=50,bg='brown',fg='white',command=self.confirm).place(x=450,y=500)
          conn.commit()
          conn.close()

          # Radiobutton(master, text = text, variable = v, 
          #     value = value).pack(side = TOP, ipady = 5) 
class custitems(Toplevel):
    itemid=StringVar()
    restid=""
    custid=""
    itemprice=""
    size=StringVar()
    quant=StringVar()
    order_id=""
    def add(self):

        conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
        cursor=conn.cursor()

        print("Select dish_price from Menu where dish_id= %s" % (self.itemid.get()))
        cursor.execute("Select dish_price from Menu where dish_id= %s" % (self.itemid.get()))
        rec=cursor.fetchall()
        print("REC[0][0]",rec[0][0])
        print(int(rec[0][0]))
        self.itemprice=str(int(rec[0][0])*int(self.quant.get()))
        cursor.execute("Select count(Order_id) from Orders where cust_id=%s and order_status='Pending';" % self.custid)
        records = cursor.fetchall()
        print("RECORDS[0][0]",records[0][0])
        cursor.execute("Select del_id from DeliveryExecutive where activity_status='Free';")
        rec2=""
        rec2=cursor.fetchall()
        print(type(rec2))
        print(len(rec2))
        print(*rec2, sep = ", ")  
        if(len(rec2)>0):
          rec2=str(rec2[0][0])
        else:
          rec2=str(-1)
        if(records[0][0]==0):
            cursor.execute("Select MAX(order_id) from Orders;")
            rec1=int(cursor.fetchall()[0][0])
            print(rec1)
            rec1=str(rec1+1)
            print(rec1)
            cursor.execute("Select coup_id from Customers where cust_id= %s;" % self.custid)
            rec111=cursor.fetchall()[0][0]
            if(rec111 is not None):
              rec111=str(rec111)
            else:
              rec111=3
            print("INSERT into Orders (order_id,cust_id,del_id,rest_id,coup_id,net_price,order_status) values (%s,%s,%s,%s,%s,%s,'Pending')" % (rec1,self.custid,rec2,self.restid,rec111,self.itemprice))
            print("INSERT INTO Cart (cust_id,dish_id,quantity,order_id,rest_id,size) values(%s,%s,%s,%s,%s,%s)" % (self.custid,self.itemid.get(),self.quant.get(),rec1,self.restid,self.size.get()))
            cursor.execute("INSERT into Orders (order_id,cust_id,del_id,rest_id,coup_id,net_price,order_status) values (%s,%s,%s,%s,%s,%s,'Pending')" % (rec1,self.custid,rec2,self.restid,rec111,self.itemprice)) #CHECK COUPON ID AND Net PRICE
            cursor.execute("INSERT INTO Cart (cust_id,dish_id,quantity,order_id,rest_id,size) values(%s,%s,%s,%s,%s,'%s')" % (self.custid,self.itemid.get(),self.quant.get(),rec1,self.restid,self.size.get()))
            self.order_id=rec1
            cursor.execute("Update DeliveryExecutive set activity_status='Delivering', order_id=%s where del_id= %s" % (self.order_id,rec2))
        elif(records[0][0]==1):
            cursor.execute("SELECT order_id from Orders where cust_id=%s and order_status='Pending'" % self.custid)
            rec1=str(cursor.fetchall()[0][0])
            self.order_id=rec1
            print("Update Orders set net_price=net_price+%s where cust_id=%s and order_status='Pending')" % (self.itemprice,self.custid))
            print("INSERT INTO Cart (cust_id,dish_id,quantity,order_id,rest_id,size) values(%s,%s,%s,(SELECT order_id from Orders cust_id=%s and order_status='Pending'),%s,%s)" % (self.custid,self.itemid.get(),self.quant.get(),self.custid,self.restid,self.size.get()))
            cursor.execute("Update Orders set net_price=net_price+%s where cust_id=%s and order_status='Pending';" % (self.itemprice,self.custid)) #Netprice            
            cursor.execute("INSERT INTO Cart (cust_id,dish_id,quantity,order_id,rest_id,size) values(%s,%s,%s,(SELECT order_id from Orders where cust_id=%s and order_status='Pending'),%s,'%s')" % (self.custid,self.itemid.get(),self.quant.get(),self.custid,self.restid,self.size.get()))


        conn.commit()
        # print("INSERT INTO Cart (cust_id,dish_id,quantity,rest_id,size) values(%s,%s,%s,-1,%s,%s)",(self.custid,self.itemid.get(),self.quant.get(),self.restid,self.size.get()))
        cursor.execute("Select order_id from Orders where cust_id=%s and order_status='Pending'" % self.custid)
        self.order_id=str(cursor.fetchall()[0][0])
        cursor.execute('SELECT * FROM Cart where order_id= %s' % self.order_id)
        currec=cursor.fetchall()
        cart_items=[]

        for row in currec:
          cursor.execute("Select dish_name,dish_price from Menu where dish_id= %s " % row[1])
          cart_items.append(cursor.fetchall()[0][0])
        self.label_1 = Label(self, text="Cart",width=33,font=("bold", 15))
        self.label_1.place(x=750,y=500)
        
        i=0
        columns=["Dish Name","Quantity","Size"]
        headings=""
        for j in columns:
          headings+=j
          headings+="  "
        print(headings)
        self.label_1 = Label(self, text=headings,width=30,font=("bold", 13))
        self.label_1.place(x=800,y=550)
        for j in range(len(currec)):
              temprow1=""
              temprow=[cart_items[j],currec[j][2],currec[j][5]]
              for j in temprow:
                  temprow1+=str(j)
                  temprow1+="    "
              print(temprow1)
              # temprow=str(row[0])+"      "+str(row[1])+"      "+str(row[7])+"      "+str(row[6])+"      "+str(row[5])+"      "+str(row[8])+"      "+str(row[9])+"      "+str(row[10])+"      "+str(row[2])+"      "+str(row[3])
              self.label_1 = Label(self, text=temprow1,width=30,font=("bold", 13))
              self.label_1.place(x=800,y=570+i)
              i+=30

        self.entry_2.delete(0,END)
        self.entry_3.delete(0,END)
        self.entry_4.delete(0,END)
        self.entry_2.insert(0,"")
        self.entry_2.insert(0,"")
        self.entry_2.insert(0,"")


        conn.commit()
        conn.close()
    def checkout(self):
        print("Checkout")
        conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
        cursor=conn.cursor()
        # print("Select dish_price from Menu where dish_id= %s" % (self.itemid.get()))
        # cursor.execute("Select dish_price from Menu where dish_id= %s" % (self.itemid.get()))
        # rec=cursor.fetchall()
        # print("REC[0][0]",rec[0][0])
        # print(int(rec[0][0]))
        # self.itemprice=str(int(rec[0][0])*int(self.quant.get()))

        cursor.execute("Select count(Order_id) from Orders where cust_id=%s and order_status='Pending';" % self.custid)
        records = cursor.fetchall()
        print("RECORDS[0][0]",records[0][0])

        if(records[0][0]==0):
            self.label_1 = Label(self, text="Please choose at least one item to order:",width=33,font=("bold", 12))
            self.label_1.place(x=400,y=750)

        elif(records[0][0]==1):
            today = date.today()
            current_date = str(today.strftime("%Y/%m/%d"))
            cursor.execute("Select rest_add from Restaurants where rest_id=%s" % self.restid)
            current_loc=str(cursor.fetchall()[0][0])
            cursor.execute("Select cust_add from Customers where cust_id=%s" % self.custid)
            destination=str(cursor.fetchall()[0][0])
            cursor.execute("Select order_id from Orders where cust_id=%s and order_status='Pending'" % (self.custid))
            self.order_id=str(int(cursor.fetchall()[0][0]))

            # print("Update Orders set order_status='Confirmed', where cust_id=%s and order_status='Pending'" % (self.custid,self.current_date))
            # print("INSERT INTO Cart (cust_id,dish_id,quantity,order_id,rest_id,size) values(%s,%s,%s,(SELECT order_id from Orders cust_id=%s and order_status='Pending'),%s,%s)" % (self.custid,self.itemid.get(),self.quant.get(),self.custid,self.restid,self.size.get()))
            cursor.execute("Update Orders set order_status='Confirmed',current_location='%s',destination='%s',date='%s' where order_id=%s" % (current_loc,destination,current_date,self.order_id))
            payment(self.restid,self.custid,self.order_id)
           
        conn.commit()
        conn.close()
    def __init__(self,restid,custid):
        self.custid=custid
        self.restid=restid
        Toplevel.__init__(self)
        # frm = Frame(root)
        # frm.pack(side=LEFT, padx=20) 
        self.geometry('1200x800')
        self.configure(bg='pink')
        conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
        cursor=conn.cursor()
        print(restid)
        print('SELECT * FROM Menu where rest_id='+restid)
        # print('SELECT * FROM Menu where rest_id=%s',(str(restid)))
        cursor.execute('SELECT * FROM Menu where rest_id='+restid)
        records = cursor.fetchall()
        self.label_1 = Label(self, text="Please choose items to order:",width=33,font=("bold", 25))
        self.label_1.place(x=300,y=50)
        i=0
        columns=["ID","Dish Name","Type","Availability","Size","Price","Review"]
        headings=""
        for j in columns:
          headings+=j
          headings+="      "
        print(headings)
        self.label_1 = Label(self, text=headings,width=90,font=("bold", 13))
        self.label_1.place(x=200,y=120)
        for row in records:
            temprow1=""
            if(row[4]==1):
                temprow=[row[0],row[1],row[2],"Available",row[5],row[6],row[7]]
            else:
                temprow=[row[0],row[1],row[2],"Unavailable",row[5],row[6],row[7]]

            for j in temprow:
                temprow1+=str(j)
                temprow1+="    "
            self.label_1 = Label(self, text=temprow1,width=90,font=("bold", 13))
            self.label_1.place(x=200,y=150+i)
            i+=28
            # temprow=[row[0],row[1],row[7],row[6],row[5],row[8],row[9],row[10],row[2],row[3]]
            # tab.addRow(row[1],row[6],row[4],row[7],row[8],row[9],row[5],row[10],row[2],row[3])
        self.label_2 = Label(self, text="Enter Item ID: ",width=17,font=("bold", 15))
        self.label_2.place(x=300,y=500)
        self.entry_2 = Entry(self,textvar = self.itemid)
        self.entry_2.place(x=500,y=505)
        self.label_3 = Label(self, text="Enter Size: ",width=17,font=("bold", 15))
        self.label_3.place(x=300,y=550)
        self.entry_3 = Entry(self,textvar = self.size)
        self.entry_3.place(x=500,y=555)
        self.label_4 = Label(self, text="Enter Quantity: ",width=17,font=("bold", 15))
        self.label_4.place(x=300,y=600)
        self.entry_4 = Entry(self,textvar = self.quant)
        self.entry_4.place(x=500,y=605)
        
        Button(self, text='Add to Cart',width=50,bg='brown',fg='white',command=self.add).place(x=400,y=650)
        Button(self, text='Checkout',width=50,bg='brown',fg='white',command=self.checkout).place(x=400,y=680)
        conn.commit()
        conn.close()
class custRest(Toplevel):
    restid=StringVar();  
    custid=""
    def items(self):
      custitems(self.restid.get(),self.custid)
      # try:
      #     cursor.execute('SELECT * FROM Menu where rest_id='+rid)
      # except:
      #     self.label_1 = Label(self, text="Wrong Restaurant ID, please try again!",width=20,font=("bold", 10))
      # #     self.label_1.place(x=330,y=720)
    def __init__(self,custid):
        Toplevel.__init__(self)
        # frm = Frame(root)
        # frm.pack(side=LEFT, padx=20) 
        self.custid=custid
        self.geometry('1200x800')
        self.configure(bg='pink')
        conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM Restaurants')
        records = cursor.fetchall()
        self.label_1 = Label(self, text="Please choose a restaurant to order from:",width=33,font=("bold", 25))
        self.label_1.place(x=250,y=50)
      
        i=0
        columns=["ID","Restaurant Name","Type","Rating","Avg Price","Availability","Open Time","Close Time","Phone","Address"]
        headings=""
        for j in columns:
          headings+=j
          headings+="  "
        print(headings)
        self.label_1 = Label(self, text=headings,width=90,font=("bold", 13))
        self.label_1.place(x=200,y=120)
        for row in records:
            # print(row)
            print("TYPE:  ",type(row[8]))
            if(str(row[8])=="Open"):
              temprow1=""
              temprow=[row[0],row[1],row[7],row[6],row[5],row[8],row[9],row[10],row[2],row[3]]
              for j in temprow:
                  temprow1+=str(j)
                  temprow1+="    "
              # temprow=str(row[0])+"      "+str(row[1])+"      "+str(row[7])+"      "+str(row[6])+"      "+str(row[5])+"      "+str(row[8])+"      "+str(row[9])+"      "+str(row[10])+"      "+str(row[2])+"      "+str(row[3])
              self.label_1 = Label(self, text=temprow1,width=90,font=("bold", 13))
              self.label_1.place(x=200,y=150+i)
              i+=28
              # temprow=[row[0],row[1],row[7],row[6],row[5],row[8],row[9],row[10],row[2],row[3]]
              # tab.addRow(row[1],row[6],row[4],row[7],row[8],row[9],row[5],row[10],row[2],row[3])
        self.label_1 = Label(self, text="Enter Restaurant ID: ",width=17,font=("bold", 15))
        self.label_1.place(x=400,y=600)
        self.entry_1 = Entry(self,textvar = self.restid)
        self.entry_1.place(x=600,y=605)
        conn.commit()
        conn.close()
        Button(self, text='Choose items',width=20,bg='brown',fg='white',command=self.items).place(x=500,y=700)
        
class sigin(Toplevel):
  def __init__(self):
    Toplevel.__init__(self)
    self.geometry('700x300')
    Button(self, text='Sign in as a Restaurant',width=20,bg='brown',fg='white',command=restsign).place(x=180,y=100)
    Button(self, text='Sign in as a customer',width=20,bg='brown',fg='white',command=custsign).place(x=370,y=100)
    Button(self, text='Sign in as a Complaint executive',width=25,bg='brown',fg='white',command=compsign).place(x=160,y=150)
    Button(self, text='Sign in as a Delivery executive',width=25,bg='brown',fg='white',command=delsign).place(x=360,y=150)


class addItem(Toplevel):
    dname = StringVar()
    dtype = StringVar()
    dprice = StringVar()
    davailability = StringVar()
    dsize = StringVar()
    rid=0
    conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
    def database(self):
        print("here")
        dname1=self.dname.get()
        dtype1=self.dtype.get()
        dprice1=self.dprice.get()
        dav=self.davailability.get()
        dsize1=self.dsize.get()
        dreview = "-"
        if dav.isdigit() and (dsize1.lower() in ['small','regular','medium','large']) and dprice1.isdigit():
            cursor=self.conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM Menu')
            records = cursor.fetchall()
            for row in records:
                 n = int(row[0])
            n=n+1
            cursor.execute('INSERT INTO Menu (dish_id,dish_name,type,rest_id,available_status,dish_size,reviews,dish_price) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)' % (n,dname1,dtype1,self.rid,int(dav),dsize1,dreview,int(dprice1)))
            self.conn.commit()
            self.label_confirm = Label(self, text='Item Added Succesfully !',width=20,font=("bold", 10))
            self.label_confirm.place(x=180,y=460)
            cursor.close()
            conn.close()
        else:
            self.label_confirm = Label(self, text='Invalid Entries!',width=20,font=("bold", 10))
            self.label_confirm.place(x=180,y=460)
        
    def __init__(self,restid):
        Toplevel.__init__(self)
        self.geometry('500x600')
        self.rid = restid
        self.label_0 = Label(self, text="Add Item",width=20,font=("bold", 20))
        self.label_0.place(x=70,y=53)


        self.label_1 = Label(self, text="Name",width=20,font=("bold", 10))
        self.label_1.place(x=60,y=130)

        self.entry_1 = Entry(self,textvar=self.dname)
        self.entry_1.place(x=240,y=130)

        self.label_2 = Label(self, text="Type",width=20,font=("bold", 10))
        self.label_2.place(x=60,y=180)

        self.entry_2 = Entry(self,textvar=self.dtype)
        self.entry_2.place(x=240,y=180)

        self.label_3 = Label(self, text="Price",width=20,font=("bold", 10))
        self.label_3.place(x=60,y=230)
        
        self.entry_3 = Entry(self,textvar=self.dprice)
        self.entry_3.place(x=240,y=230)
        
        self.label_5 = Label(self, text="Availability",width=20,font=("bold", 10))
        self.label_5.place(x=60,y=280)
        
        self.entry_5 = Entry(self,textvar=self.davailability)
        self.entry_5.place(x=240,y=280)
        
        self.label_6 = Label(self, text="Size",width=20,font=("bold", 10))
        self.label_6.place(x=60,y=320)
        
        self.entry_6 = Entry(self,textvar=self.dsize)
        self.entry_6.place(x=240,y=320)
        
        Button(self, text='Submit',width=20,bg='brown',fg='white',command=self.database).place(x=180,y=400)
        

#Start
class editItem(Toplevel):
    d_id = IntVar()
    dcolumn = StringVar()
    dvalue = StringVar()
    rid=0
    conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
    def database(self):
        cursor=self.conn.cursor()
        if self.dcolumn.get() == 'dish_id' or self.dcolumn.get() == 'dish_name' or self.dcolumn.get() == 'type' or self.dcolumn.get() == 'available_status' or self.dcolumn.get() == 'dish_size':
            
            #cursor.execute('CREATE INDEX IF NOT EXISTS dish_rest ON Menu(restid,DishID)')
            if self.dcolumn.get() == 'dish_id':
                cursor.execute('UPDATE Menu SET dish_id = %s WHERE rest_id = %s AND dish_id = %s' % (int(self.dvalue.get()),self.rid,self.d_id.get()))
            if self.dcolumn.get() == 'dishname':
                cursor.execute('UPDATE Menu SET dish_name = %s WHERE rest_id = %s AND dish_id = %s' % (self.dvalue.get(),self.rid,self.d_id.get()))
            if self.dcolumn.get() == 'dishtype':
                cursor.execute('UPDATE Menu SET type = %s WHERE rest_id = %s AND dish_id = %s' % (self.dvalue.get(),self.rid,self.d_id.get()))
            if self.dcolumn.get() == 'availability':
                if dvalue.get().isdigit():
                    cursor.execute('UPDATE Menu SET available_status = %s WHERE rest_id = %s AND dish_id = %s' % (int(self.dvalue.get()),self.rid,self.d_id.get()))
                else:
                    self.label_notvalid = Label(self, text='Invalid Value',width=20,font=("bold", 10))
                    self.label_notvalid.place(x=180,y=460)
            if self.dcolumn.get() == 'size':
                if dvalue.get().lower() in ['small','regular','medium','large']:
                    cursor.execute('UPDATE Menu SET dish_size = %s WHERE rest_id = %s AND dish_id = %s' % (self.dvalue.get(),self.rid,self.d_id.get()))
                else:
                    self.label_notvalid = Label(self, text='Invalid Value',width=20,font=("bold", 10))
                    self.label_notvalid.place(x=180,y=460)
            self.conn.commit()
            self.label_confirm = Label(self, text='Item Edited Succesfully !',width=20,font=("bold", 10))
            self.label_confirm.place(x=180,y=460)
        elif self.dcolumn.get() == 'dish_price':
            if self.dvalue.get().isdigit():
                #cursor.execute('CREATE INDEX IF NOT EXISTS dish_rest ON Menu(restid,DishID)')
                cursor.execute('UPDATE Menu SET dish_price = %s WHERE rest_id = %s AND dish_id = %s' % (int(self.dvalue.get()),self.rid, self.d_id.get()))
                self.conn.commit()
                self.label_confirm = Label(self, text='Item Edited Succesfully !',width=20,font=("bold", 10))
                self.label_confirm.place(x=180,y=460)
            else:
                self.label_notvalid = Label(self, text='Invalid Value',width=20,font=("bold", 10))
                self.label_notvalid.place(x=180,y=460)
        else:
            self.label_a = Label(self, text='Invalid column',width=20,font=("bold", 10))
            self.label_a.place(x=180,y=460)
        cursor.close()
        conn.close()
    def __init__(self,restid):
        Toplevel.__init__(self)
        self.geometry('500x600')
        self.rid = restid
        self.label_0 = Label(self, text="Edit Item",width=20,font=("bold", 20))
        self.label_0.place(x=70,y=53)


        self.label_1 = Label(self, text="Enter Dish ID",width=20,font=("bold", 10))
        self.label_1.place(x=60,y=130)

        self.entry_1 = Entry(self,textvar=self.d_id)
        self.entry_1.place(x=240,y=130)

        self.label_2 = Label(self, text="Enter Column Value to Update",width=20,font=("bold", 10))
        self.label_2.place(x=60,y=180)

        self.entry_2 = Entry(self,textvar=self.dcolumn)
        self.entry_2.place(x=240,y=180)

        self.label_3 = Label(self, text="Enter New Value",width=20,font=("bold", 10))
        self.label_3.place(x=60,y=230)
        self.entry_3 = Entry(self,textvar=self.dvalue)
        self.entry_3.place(x=240,y=230)
        Button(self, text='Submit',width=20,bg='brown',fg='white',command=self.database).place(x=180,y=400)
        
             

class viewItem(Toplevel):
    rid = 0
    def __init__(self,restid):
        self.rid = restid
        Toplevel.__init__(self)
        self.geometry('900x700')
        self.configure(bg='pink')
        conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM Menu WHERE rest_id = %s' % (self.rid))
        ind=0
        for row in cursor.fetchall():
            self.label_1 = Label(self, text=row,width=80,font=("bold", 10))
            self.label_1.place(x=200,y=20+ind)
            ind=ind+40
        cursor.close()
        conn.close()

#end        
class restDash(Toplevel):
    restid=0
    def additems(self):
        addItem(self.restid)
    def edititems(self):
        editItem(self.restid)
    def viewitems(self):
        viewItem(self.restid)
    def __init__(self,rowid):
        self.restid = rowid
        Toplevel.__init__(self)
        self.geometry('900x700')
        self.configure(bg='pink')
        conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM Restaurants WHERE rest_id = %s' % (rowid))
        records = cursor.fetchall()
        current_time = tm.strftime('%H:%M:%S')
        for row in records:
            opentime=row[9]
            closetime=row[10]
        hr = int(current_time[0:2])
        mins = int(current_time[3:5])
        hr1 = int(opentime[0:2])
        mins1 = int(opentime[3:5])
        hr2 = int(closetime[0:2])
        mins2 = int(closetime[3:5])
        if hr<hr1:
           available_status="not open"
        elif hr==hr1 and mins<mins1:
           available_status="not open"
        elif hr>hr2:
           available_status="not open"
        elif hr==hr2 and mins>mins2:
           available_status="not open"
        else:
           available_status="open"
        
        cursor.execute('UPDATE Restaurants SET availability = %s WHERE rest_id = %s' % (available_status,rowid))
        conn.commit()
        cursor.execute('SELECT * FROM Restaurants WHERE rest_id = %s' % (rowid))
        records = cursor.fetchall()
        for row in records:
            if row[0]==rowid:
                welcmsg = "Welcome "+row[1];
                self.label_1 = Label(self, text=welcmsg,width=20,font=("bold", 30))
                self.label_1.place(x=200,y=20)
                self.label_2 = Label(self, text="User Details",width=50,font=("bold", 10))
                self.label_2.place(x=100,y=80)
                strname="Restaurant Name: "+row[1]
                stremail="Restaurant Phone: "+row[2]
                strphone="Restaurant Address: "+str(row[3])
                #stradd="Restaurant Address: "+row[4]
                strtype="Restaurant Type: "+row[7]
                stravgp="Restaurant Avg Price: "+str(row[5])
                strstartend="Restaurant Start-End time: "+row[9]+"-"+row[10]
                stravailable="Restaurant Availability: "+row[8]

        self.label_1 = Label(self, text=strname,width=50,font=("bold", 10))
        self.label_1.place(x=100,y=100)
        self.label_2 = Label(self, text=stremail,width=50,font=("bold", 10))
        self.label_2.place(x=100,y=120)
        self.label_3 = Label(self, text=strphone,width=50,font=("bold", 10))
        self.label_3.place(x=100,y=140)
        
        self.label_5 = Label(self, text=strtype,width=50,font=("bold", 10))
        self.label_5.place(x=100,y=180)
        self.label_6 = Label(self, text=stravgp,width=50,font=("bold", 10))
        self.label_6.place(x=100,y=200)
        self.label_7 = Label(self, text=strstartend,width=50,font=("bold", 10))
        self.label_7.place(x=100,y=220)
        self.label_8 = Label(self, text=stravailable,width=50,font=("bold", 10))
        self.label_8.place(x=100,y=240)
        Button(self, text='Add Item',width=20,bg='brown',fg='white',command=self.additems).place(x=180,y=270)
        Button(self, text='Edit an Item',width=20,bg='brown',fg='white',command=self.edititems).place(x=180,y=300)
        Button(self, text='View Items',width=20,bg='brown',fg='white',command=self.viewitems).place(x=180,y=330)
        cursor.close()
        conn.close()
        
class custDash(Toplevel):
    custid=""
    def database(self):
        custRest(self.custid)
    def database1(self):
        AddComplaint(self.custid)
    def __init__(self,rowid):
        Toplevel.__init__(self)
        self.geometry('900x700')
        self.configure(bg='pink')
        conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM Customers')
        records = cursor.fetchall()
        for row in records:
            if row[0]==rowid:
                self.custid=row[0]
                welcmsg = "Welcome "+row[1];
                self.label_1 = Label(self, text=welcmsg,width=20,font=("bold", 30))
                self.label_1.place(x=200,y=20)
                self.label_2 = Label(self, text="User Details",width=50,font=("bold", 10))
                self.label_2.place(x=100,y=80)
                strname="Name: "+row[1]
                stremail="Email: "+row[2]
                strphone="Phone: "+str(row[6])
                stradd="Address: "+row[3]
                if(row[4]==1):
                  strmem="Membership: Gold"
                else:
                  strmem="Membership: Standard"

        conn.close()
        Button(self, text='Place a new order',width=20,bg='brown',fg='white',command=self.database).place(x=150,y=400)
        Button(self, text='Raise an issue',width=20,bg='brown',fg='white',command=self.database1).place(x=150,y=500)
        self.label_1 = Label(self, text=strname,width=50,font=("bold", 10))
        self.label_1.place(x=100,y=100)
        self.label_2 = Label(self, text=stremail,width=50,font=("bold", 10))
        self.label_2.place(x=100,y=120)
        self.label_3 = Label(self, text=strphone,width=50,font=("bold", 10))
        self.label_3.place(x=100,y=140)
        self.label_4 = Label(self, text=stradd,width=50,font=("bold", 10))
        self.label_4.place(x=100,y=160)
        self.label_5 = Label(self, text=strmem,width=50,font=("bold", 10))
        self.label_5.place(x=100,y=180)
        self.label_6 = Label(self, text=str(coupid),width=50,font=("bold", 10))
        self.label_6.place(x=100,y=200)
     

        

class comDash(Toplevel):
    def __init__(self,rowid):
        Toplevel.__init__(self)
        self.geometry('900x700')
        self.configure(bg='pink')
        conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM ComplaintExecutive')
        records = cursor.fetchall()
        for row in records:
            if row[0]==rowid:
                welcmsg = "Welcome "+row[1];
                self.label_1 = Label(self, text=welcmsg,width=20,font=("bold", 30))
                self.label_1.place(x=200,y=20)
                self.label_2 = Label(self, text="User Details",width=50,font=("bold", 10))
                self.label_2.place(x=100,y=80)
                strname="Name: "+row[1]
                stremail="Email: "+row[3]
                strphone="Phone: "+str(row[5])
                stradd="Active status: "+row[2]

        self.label_1 = Label(self, text=strname,width=50,font=("bold", 10))
        self.label_1.place(x=100,y=100)
        self.label_2 = Label(self, text=stremail,width=50,font=("bold", 10))
        self.label_2.place(x=100,y=120)
        self.label_3 = Label(self, text=strphone,width=50,font=("bold", 10))
        self.label_3.place(x=100,y=140)
        self.label_4 = Label(self, text=stradd,width=50,font=("bold", 10))
        self.label_4.place(x=100,y=160)
        # Button(self, text='',width=20,bg='brown',fg='white',command=self.database).place(x=150,y=300)
        cursor.close()
        conn.close()

class CurrentOrder(Toplevel):
    exists=False

    def __init__(self,order_id):
        Toplevel.__init__(self)
        self.geometry('500x600')

        conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
        cursor=conn.cursor()

        cursor.execute(f"SELECT * FROM Orders WHERE order_id={order_id} AND order_status NOT IN ('Cancelled','Delivered')")
        records=cursor.fetchall()

        self.label_0= Label(self,text="Current Order Details",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)

        if(len(records)==0):
            self.label_1= Label(self,text="No valid current order",width=20,font=("bold", 10))
            self.label_1.place(x=90,y=100)
        else:
            row=records[0]
            self.label_2= Label(self,text=f"order Number:{row[0]}",width=100,font=("bold", 10))
            self.label_2.place(x=90,y=100)

            cursor.execute(f"SELECT del_name from DeliveryExecutive WHERE del_id={row[2]}") 
            recs= cursor.fetchall()
            
            self.label_3= Label(self,text=f"Delivered by {recs[0][0]}",width=100,font=("bold", 10))
            self.label_3.place(x=90,y=130)

            cursor.execute(f"SELECT rest_name from Restaurants WHERE rest_id={row[3]}") 
            recs= cursor.fetchall()
            
            self.label_4= Label(self,text=f"Restaurant providing the food {recs[0][0]}",width=100,font=("bold", 10))
            self.label_4.place(x=90,y=160)

            cursor.execute(f"SELECT coup_code from Coupons WHERE coup_id={row[4]}") 
            recs= cursor.fetchall()
            
            self.label_5= Label(self,text=f"Coupon code applied {recs[0][0]}",width=100,font=("bold", 10))
            self.label_5.place(x=90,y=190)
            
            self.label_6= Label(self,text=f"Net Price: {row[5]}",width=100,font=("bold", 10))
            self.label_6.place(x=90,y=220)
            
            
            self.label_6= Label(self,text=f"Order Status: {row[6]}",width=100,font=("bold", 10))
            self.label_6.place(x=90,y=250)
            
            self.label_6= Label(self,text=f"Payment Status: {row[10]}",width=100,font=("bold", 10))
            self.label_6.place(x=90,y=280)

            self.label_7= Label(self,text="Dishes present in the order",width=100,font=("bold", 15))
            self.label_7.place(x=90,y=310)

            cursor.execute(f"select dish_name from Menu Natural Join Cart where Cart.order_id={row[0]};")
            recs = cursor.fetchall()

            self.labels=[]
            for x in range(len(recs)):
                self.labels.append( Label(self,text=f"{recs[x]}",width=100,font=("bold", 10)))
                self.labels[-1].place(x=90,y=310+30*x)
        cursor.close()
        conn.close()
class delDash(Toplevel):
    ord_id=0
    del_id=""
    def database(self):
        CustCurrentOrder(self.ord_id)
    def database1(self):
        cursor.execute('SELECT * FROM DeliveryExecutive where del_id=%s ' % self.del_id)
        records = cursor.fetchall()
        self.ord_id=records[0][6]
        if self.ord_id >0:
            Button(self, text='Current Orders',width=20,bg='brown',fg='white',command=self.database).place(x=180,y=300)
            stractivestatus="Active Status: "+records[0][5]
    def __init__(self,rowid):
        self.del_id=rowid
        Toplevel.__init__(self)
        self.geometry('900x700')
        self.configure(bg='pink')
        conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM DeliveryExecutive')
        records = cursor.fetchall()
        for row in records:
            if row[0]==rowid:
                welcmsg = "Welcome "+row[1];
                self.label_1 = Label(self, text=welcmsg,width=20,font=("bold", 30))
                self.label_1.place(x=200,y=20)
                self.label_2 = Label(self, text="User Details",width=50,font=("bold", 10))
                self.label_2.place(x=100,y=80)
                strname="Name: "+row[1]
                stremail="Email: "+row[7]
                strphone="Phone: "+str(row[2])
                stradd="Age: "+str(row[3])
                stractivestatus="Active Status: "+row[5]
                self.ord_id=row[6]

        self.label_1 = Label(self, text=strname,width=50,font=("bold", 10))
        self.label_1.place(x=100,y=100)
        self.label_2 = Label(self, text=stremail,width=50,font=("bold", 10))
        self.label_2.place(x=100,y=120)
        self.label_3 = Label(self, text=strphone,width=50,font=("bold", 10))
        self.label_3.place(x=100,y=140)
        self.label_4 = Label(self, text=stradd,width=50,font=("bold", 10))
        self.label_4.place(x=100,y=160)
        self.label_5 = Label(self, text=stractivestatus,width=50,font=("bold", 10))
        self.label_5.place(x=100,y=160)
        if self.ord_id >0:
            Button(self, text='Current Orders',width=20,bg='brown',fg='white',command=self.database).place(x=180,y=300)
        else:
            Button(self, text='Refresh',width=20,bg='brown',fg='white',command=self.database1).place(x=180,y=400)
        cursor.close()
        conn.close()

class restsignin(Toplevel):
  restemail=StringVar()
  Password=StringVar()
  
  def database(self):
      conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
      cursor=conn.cursor()
      strrest = self.restemail.get()
      #cursor.execute('CREATE INDEX IF NOT EXISTS rest_email ON Restaurants(restemail)')
      #conn.commit()
      cursor.execute('SELECT COUNT(*) FROM Restaurants WHERE email = "%s"' % (strrest))
      records = cursor.fetchall()
      for row in records:
          cnt = row[0]
      if cnt == 0:
          self.label_1 = Label(self, text="Email Address does not exist",width=20,font=("bold", 10))
          self.label_1.place(x=110,y=200)
      else:
          cursor.execute('SELECT * FROM Restaurants WHERE email = "%s"' % (strrest))
          records = cursor.fetchall()
          for row in records:
              if row[12]!=self.Password.get():
                  self.label_pass = Label(self, text="Wrong Password",width=20,font=("bold", 10))
                  self.label_pass.place(x=140,y=200)
              else:
                  restDash(row[0])
      cursor.close()
      conn.close()
  def __init__(self):
    Toplevel.__init__(self)
    self.geometry('500x500')
    self.label_1 = Label(self, text="Enter Restaurant email",width=20,font=("bold", 10))
    self.label_1.place(x=50,y=53)
    
    self.entry_1 = Entry(self,textvar = self.restemail)
    self.entry_1.place(x=270,y=53)

    self.label_2 = Label(self, text="Enter Password",width=20,font=("bold", 10))
    self.label_2.place(x=50,y=93)
    
    self.entry_2 = Entry(self,show='*',textvar = self.Password)
    self.entry_2.place(x=270,y=93)
    Button(self, text='Submit',width=20,bg='brown',fg='white',command=self.database).place(x=180,y=150)
    


class custsignin(Toplevel):
  Email=StringVar()
  pas = StringVar()
  def database(self):
      conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
      cursor=conn.cursor()
      strcust = self.Email

      cursor.execute('SELECT * FROM Customers')
      records = cursor.fetchall()
      flag=0
      flag2=0
      for row in records:
          if row[3] == self.Email.get():
              flag=1
              if row[5] == self.pas.get():
                     flag2=1
                     custDash(row[0])
              break
      if flag==0:
          self.label_1 = Label(self, text="Email Address does not exist",width=20,font=("bold", 10))
          self.label_1.place(x=110,y=200)
      if flag2==0:
          self.label_pass = Label(self, text="Wrong Password",width=20,font=("bold", 10))
          self.label_pass.place(x=140,y=200)
      cursor.close()
      conn.close()

  def __init__(self):
    Toplevel.__init__(self)
    self.geometry('500x500')
    self.label_1 = Label(self, text="Enter your email",width=20,font=("bold", 10))
    self.label_1.place(x=50,y=53)
    
    self.entry_1 = Entry(self,textvar=self.Email)
    self.entry_1.place(x=270,y=53)

    self.label_2 = Label(self, text="Enter Password",width=20,font=("bold", 10))
    self.label_2.place(x=50,y=93)
    
    self.entry_2 = Entry(self,show="*",textvar=self.pas)
    self.entry_2.place(x=270,y=93)
    Button(self, text='Submit',width=20,bg='brown',fg='white',command=self.database).place(x=180,y=150)


class complaintsignin(Toplevel):
  comemail = StringVar()
  pas = StringVar()
  def database(self):
      conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
      cursor=conn.cursor()
      strrest = self.comemail.get()
      #cursor.execute('CREATE INDEX IF NOT EXISTS com_email ON ComplaintExec(comemail)')
      #conn.commit()
      cursor.execute('SELECT COUNT(*) FROM ComplaintExecutive WHERE email = %s' % (strrest))
      records = cursor.fetchall()
      for row in records:
          cnt = row[0]
      if cnt == 0:
          self.label_1 = Label(self, text="Email Address does not exist",width=20,font=("bold", 10))
          self.label_1.place(x=110,y=200)
      else:
          cursor.execute('SELECT * FROM ComplaintExecutive WHERE email = %s' % (strrest))
          records = cursor.fetchall()
          for row in records:
              if row[4]!=self.pas.get():
                  self.label_pass = Label(self, text="Wrong Password",width=20,font=("bold", 10))
                  self.label_pass.place(x=140,y=200)
              else:
                  comDash(row[0]) 
  def __init__(self):
    Toplevel.__init__(self)
    self.geometry('500x500')
    self.label_1 = Label(self, text="Enter your email",width=20,font=("bold", 10))
    self.label_1.place(x=50,y=53)
    
    self.entry_1 = Entry(self,textvar=self.comemail)
    self.entry_1.place(x=270,y=53)

    self.label_2 = Label(self,text="Enter Password",width=20,font=("bold", 10))
    self.label_2.place(x=50,y=93)
    
    self.entry_2 = Entry(self,show="*",textvar=self.pas)
    self.entry_2.place(x=270,y=93)
    Button(self, text='Submit',width=20,bg='brown',fg='white',command=self.database).place(x=180,y=150)
    cursor.close()
    conn.close()


class deliveryexecsignin(Toplevel):
  delemail = StringVar()
  pas = StringVar()
  def database(self):
      conn =  mysql.connector.connect(host="remotemysql.com",database="agLYMKsBsZ",user="agLYMKsBsZ",password="LxpU9sdeQn")
      cursor=conn.cursor()
      strrest = self.delemail.get()
      conn.commit()
      cursor.execute('SELECT COUNT(*) FROM DeliveryExecutive WHERE email = "%s"' % (strrest))
      records = cursor.fetchall()
      for row in records:
          cnt = row[0]
      if cnt == 0:
          self.label_1 = Label(self, text="Email Address does not exist",width=20,font=("bold", 10))
          self.label_1.place(x=110,y=200)
      else:
          cursor.execute('SELECT * FROM DeliveryExecutive WHERE email = "%s"' % strrest)
          records = cursor.fetchall()
          for row in records:
              if row[8]!=self.pas.get():
                  self.label_pass = Label(self, text="Wrong Password",width=20,font=("bold", 10))
                  self.label_pass.place(x=140,y=200)
              else:
                  delDash(row[0])
          cursor.close()
          conn.close()
  def __init__(self):
    Toplevel.__init__(self)
    self.geometry('500x500')
    self.label_1 = Label(self, text="Enter your email",width=20,font=("bold", 10))
    self.label_1.place(x=50,y=53)
    
    self.entry_1 = Entry(self,textvar = self.delemail)
    self.entry_1.place(x=270,y=53)

    self.label_2 = Label(self, text="Enter Password",width=20,font=("bold", 10))
    self.label_2.place(x=50,y=93)
    
    self.entry_2 = Entry(self,show="*",textvar = self.pas)
    self.entry_2.place(x=270,y=93)
    Button(self, text='Submit',width=20,bg='brown',fg='white',command=self.database).place(x=180,y=150)
    


def cust():
    customer()

def rest():
    restaurant()
def delexec():
    deliveryexec()
def comexec():
    complaintexec()
def restsign():
  restsignin()

def custsign():
  custsignin()

def compsign():
  complaintsignin()

def delsign():
  deliveryexecsignin()

def sign():
  sigin()

label_title = Label(root, text="Zomiggy",width=20,font=("bold", 20))
label_title.place(x=290,y=50)
s1="Welcome to Zomiggy! We have a collection of restaurants and dishes available."
s2="Place an order and a delivery man will get it delivered on your door step!"
s3="We provide you with the provision of lodging complaint about any restaurant and"
s4="dish or even a delivery boy and our complaint executives will handle them as their topmost priority. Enjoy!!"
label_desc1 = Label(root, text=s1,width=100,font=("bold", 10))
label_desc2 = Label(root, text=s2,width=100,font=("bold", 10))
label_desc3 = Label(root, text=s3,width=100,font=("bold", 10))
label_desc4 = Label(root, text=s4,width=100,font=("bold", 10))
label_desc1.place(x=60,y=100)
label_desc2.place(x=60,y=120)
label_desc3.place(x=60,y=140)
label_desc4.place(x=60,y=160)
Button(root, text='Sign In Now!',width=20,bg='brown',fg='white',command=sign).place(x=380,y=200)
label_signup = Label(root, text="Don't have an account? Sign Up Now!",width=100,font=("bold", 10))
label_signup.place(x=60,y=280)
Button(root, text='Customer SignUp',width=20,bg='brown',fg='white',command=cust).place(x=100,y=330)
Button(root, text='Restaurant SignUp',width=20,bg='brown',fg='white',command=rest).place(x=300,y=330)
Button(root, text='Complaint Executive SignUp',width=25,bg='brown',fg='white',command=comexec).place(x=500,y=330)
Button(root, text='Delivery Executive SignUp',width=20,bg='brown',fg='white',command=delexec).place(x=700,y=330)
root.mainloop()
