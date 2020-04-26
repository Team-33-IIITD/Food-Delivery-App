from tkinter import *
import sqlite3
import time as tm
root = Tk()
root.geometry('900x700')
root.title("HomePage")
root.configure(bg='green')
class complaintexec(Toplevel):
    comname = StringVar()
    comemail = StringVar()
    comph = IntVar()
    pas = StringVar()
    activestatus=StringVar()
    conn = sqlite3.connect('data.db')
    def database(self):
       name1=self.comname.get()
       email=self.comemail.get()
       phone=self.comph.get()
       password = self.pas.get()
       active_status = "active"
       with self.conn:
          cursor=self.conn.cursor()
       cursor.execute('CREATE TABLE IF NOT EXISTS ComplaintExec (ComID INT, comname TEXT, comemail TEXT, comphone INT,password TEXT, activestatus TEXT)')
       cursor.execute('SELECT COUNT(*) FROM ComplaintExec')
       records = cursor.fetchall()
       for row in records:
            n = int(row[0])
       n=n+1
       cursor.execute('INSERT INTO ComplaintExec (ComID,comname,comemail,comphone,password,activestatus) VALUES(?,?,?,?,?,?)',(n,name1,email,phone,password,active_status))
       self.conn.commit()
       self.confirm = Label(self, text="Complaint Executive Registered!",width=30,font=("bold", 10))
       self.confirm.place(x=120,y=460)
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('500x600')
        self.label_0 = Label(self, text="Complaint Executive SignUp",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)


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
    delph = IntVar()
    delage = IntVar()
    pas = StringVar()
    activestatus=StringVar()
    conn = sqlite3.connect('data.db')
    def database(self):
       name1=self.delname.get()
       email=self.delemail.get()
       phone=self.delph.get()
       age=self.delage.get()
       password = self.pas.get()
       active_status = "active"
       with self.conn:
          cursor=self.conn.cursor()
       cursor.execute('CREATE TABLE IF NOT EXISTS DeliveryExec (DelID INT, delname TEXT, delemail TEXT, delphone INT,delage TEXT,password TEXT, activestatus TEXT)')
       cursor.execute('SELECT COUNT(*) FROM DeliveryExec')
       records = cursor.fetchall()
       for row in records:
            n = int(row[0])
       n=n+1
       cursor.execute('INSERT INTO DeliveryExec (DelID,delname,delemail,delphone,delage,password,activestatus) VALUES(?,?,?,?,?,?,?)',(n,name1,email,phone,age,password,active_status))
       self.conn.commit()
       self.confirm = Label(self, text="Delivery Executive Registered!",width=30,font=("bold", 10))
       self.confirm.place(x=120,y=460)
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
class restaurant(Toplevel):
    restname=StringVar()
    #ownername=StringVar()
    restemail=StringVar()
    restph = IntVar()
    restadd=StringVar()
    pas = StringVar()
    rest_type=StringVar()
    open_time=StringVar()
    close_time=StringVar()
    availability=StringVar()
    conn = sqlite3.connect('data.db')
    def database(self):
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
           available_status="not open"
       elif hr==hr1 and mins<mins1:
           available_status="not open"
       elif hr>hr2:
           available_status="not open"
       elif hr==hr2 and mins>mins2:
           available_status="not open"
       else:
           available_status="open"
           
       #available_status = "available"
       avg_price=0
       with self.conn:
          cursor=self.conn.cursor()
       cursor.execute('CREATE TABLE IF NOT EXISTS Restaurant3 (RestID INT, restname TEXT,restemail TEXT,restphone INT,restadd TEXT,type TEXT, avgprice TEXT,password TEXT, closetime TEXT,opentime TEXT,available TEXT)')
       cursor.execute('SELECT COUNT(*) FROM Restaurant3')
       records = cursor.fetchall()
       for row in records:
            n = int(row[0])
       n=n+1
       #custid=str(n)
       cursor.execute('INSERT INTO Restaurant3 (RestID,restname,restemail,restphone,restadd,type,avgprice,password,closetime,opentime,available) VALUES(?,?,?,?,?,?,?,?,?,?,?)',(n,name1,email,phone,address,type1,avg_price,password,closetime,opentime,available_status))
       self.conn.commit()
       self.confirm = Label(self, text="Restaurant Registered!",width=20,font=("bold", 10))
       self.confirm.place(x=180,y=560)
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('500x600')
        self.label_0 = Label(self, text="Restaurant SignUp",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)


        self.label_1 = Label(self, text="Restaurant Name",width=20,font=("bold", 10))
        self.label_1.place(x=80,y=130)

        self.entry_1 = Entry(self,textvar=self.restname)
        self.entry_1.place(x=240,y=130)

        self.label_2 = Label(self, text="Restaurant Email",width=20,font=("bold", 10))
        self.label_2.place(x=68,y=180)

        self.entry_2 = Entry(self,textvar=self.restemail)
        self.entry_2.place(x=240,y=180)

        self.label_3 = Label(self, text="Restaurant Phone Number",width=20,font=("bold", 10))
        self.label_3.place(x=70,y=230)
        self.entry_3 = Entry(self,textvar=self.restph)
        self.entry_3.place(x=240,y=230)
        self.label_4 = Label(self, text="Restaurant Address",width=20,font=("bold", 10))
        self.label_4.place(x=70,y=280)
        self.entry_4 = Entry(self,textvar=self.restadd)
        self.entry_4.place(x=240,y=280)

        self.label_5 = Label(self, text="Restaurant Type",width=20,font=("bold", 10))
        self.label_5.place(x=85,y=330)
        self.entry_5 = Entry(self,textvar=self.rest_type)
        self.entry_5.place(x=240,y=330)
        self.label_6 = Label(self, text="Password",width=20,font=("bold", 10))
        self.label_6.place(x=85,y=380)
        self.entry_6 = Entry(self,show="*",textvar=self.pas)
        self.entry_6.place(x=240,y=380)

        self.label_7 = Label(self, text="Open Time",width=20,font=("bold", 10))
        self.label_7.place(x=85,y=430)
        self.entry_7 = Entry(self,textvar=self.open_time)
        self.entry_7.place(x=240,y=430)

        self.label_8 = Label(self, text="Close Time",width=20,font=("bold", 10))
        self.label_8.place(x=85,y=480)
        self.entry_8 = Entry(self,textvar=self.close_time)
        self.entry_8.place(x=240,y=480)
        Button(self, text='Submit',width=20,bg='brown',fg='white',command=self.database).place(x=180,y=520)
# Homepage with Customer Sign Up linked with database
class customer(Toplevel):
    Fullname=StringVar()
    Email=StringVar()
    phonenum = IntVar()
    add=StringVar()
    mem= StringVar()
    pas = StringVar()
    coupid = IntVar()
    conn = sqlite3.connect('data.db')
    def database(self):
       name1=self.Fullname.get()
       email=self.Email.get()
       phone=self.phonenum.get()
       address=self.add.get()
       membership=self.mem.get()
       password = self.pas.get()
       cid = self.coupid.get()
       with self.conn:
          cursor=self.conn.cursor()
       cursor.execute('CREATE TABLE IF NOT EXISTS Customer3 (CustID INT, Fullname TEXT,Email TEXT,Phone INT,Address TEXT,Membership TEXT, Password TEXT, CouponID INT)')
       cursor.execute('SELECT COUNT(*) FROM Customer3')
       records = cursor.fetchall()
       for row in records:
            n = int(row[0])
       n=n+1
       custid=str(n)
       cursor.execute('INSERT INTO Customer3 (CustID,FullName,Email,Phone,Address,Membership,Password,CouponID) VALUES(?,?,?,?,?,?,?,?)',(n,name1,email,phone,address,membership,password,cid))
       self.conn.commit()
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
        self.entry_5 = Entry(self,textvar=self.mem)
        self.entry_5.place(x=240,y=330)
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

def cust():
    customer()

def rest():
    restaurant()
def delexec():
    deliveryexec()
def comexec():
    complaintexec()


label_title = Label(root, text="Zomiggy",width=20,font=("bold", 20))
label_title.place(x=290,y=50)
s1="Welcome to Zomiggy! We have a collection of restraunts and dishes available."
s2="Place an order and a delivery man will get it delivered on your door step!"
s3="We provide you with the provision of lodging complaint about any restraunt and"
s4="dish or even a delivery boy and our complaint executives will handle them as their topmost priority. Enjoy!!"
label_desc1 = Label(root, text=s1,width=100,font=("bold", 10))
label_desc2 = Label(root, text=s2,width=100,font=("bold", 10))
label_desc3 = Label(root, text=s3,width=100,font=("bold", 10))
label_desc4 = Label(root, text=s4,width=100,font=("bold", 10))
label_desc1.place(x=60,y=100)
label_desc2.place(x=60,y=120)
label_desc3.place(x=60,y=140)
label_desc4.place(x=60,y=160)
Button(root, text='Sign In Now!',width=20,bg='brown',fg='white').place(x=380,y=200)
label_signup = Label(root, text="Don't have an account? Sign Up Now!",width=100,font=("bold", 10))
label_signup.place(x=60,y=280)
Button(root, text='Customer SignUp',width=20,bg='brown',fg='white',command=cust).place(x=100,y=330)
Button(root, text='Restraunt SignUp',width=20,bg='brown',fg='white',command=rest).place(x=300,y=330)
Button(root, text='Complaint Executive SignUp',width=25,bg='brown',fg='white',command=comexec).place(x=500,y=330)
Button(root, text='Delivery Executive SignUp',width=20,bg='brown',fg='white',command=delexec).place(x=700,y=330)
root.mainloop()
