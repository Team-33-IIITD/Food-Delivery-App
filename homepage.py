from tkinter import *
import sqlite3
import time as tm
root = Tk()
root.geometry('900x700')
root.title("HomePage")
root.configure(bg='black')
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
       cursor.execute('SELECT COUNT(*) FROM Restaurant3 WHERE restemail = ?',(email,))
       records = cursor.fetchall()
       for row in records:
            n1 = int(row[0])
       cursor.execute('SELECT COUNT(*) FROM Restaurant3 WHERE restphone = ?',(phone,))
       records = cursor.fetchall()
       for row in records:
            n2 = int(row[0])
       #custid=str(n)
       if n1==0 and n2==0:
           cursor.execute('INSERT INTO Restaurant3 (RestID,restname,restemail,restphone,restadd,type,avgprice,password,closetime,opentime,available) VALUES(?,?,?,?,?,?,?,?,?,?,?)',(n,name1,email,phone,address,type1,avg_price,password,closetime,opentime,available_status))
           self.conn.commit()
           self.confirm = Label(self, text="Restaurant Registered!",width=20,font=("bold", 10))
           self.confirm.place(x=180,y=560)
       else:
           self.inv = Label(self, text="Email/Phone number already taken",width=20,font=("bold", 10))
           self.inv.place(x=180,y=560)
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
       cursor.execute('SELECT COUNT(*) FROM Customer3 WHERE Email = ?',(email,))
       records = cursor.fetchall()
       for row in records:
            n1 = int(row[0])
       
       if n1==0:
           cursor.execute('INSERT INTO Customer3 (CustID,FullName,Email,Phone,Address,Membership,Password,CouponID) VALUES(?,?,?,?,?,?,?,?)',(n,name1,email,phone,address,membership,password,cid))
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
    dprice = IntVar()
    davailability = StringVar()
    dsize = StringVar()
    rid=0
    conn = sqlite3.connect('data.db')
    def database(self):
        print("here")
        dname1=self.dname.get()
        dtype1=self.dtype.get()
        dprice1=self.dprice.get()
        dav=self.davailability.get()
        dsize1=self.dsize.get()
        
        with self.conn:
            cursor=self.conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Menu (DishID INT, dishname TEXT, dishtype TEXT, restid INT,price INT, availability TEXT, size TEXT)')
        cursor.execute('SELECT COUNT(*) FROM Menu')
        records = cursor.fetchall()
        for row in records:
             n = int(row[0])
        n=n+1
        cursor.execute('INSERT INTO Menu (DishID,dishname,dishtype,restid,price,availability,size) VALUES(?,?,?,?,?,?,?)',(n,dname1,dtype1,self.rid,dprice1,dav,dsize1))
        self.conn.commit()
        self.label_confirm = Label(self, text='Item Added Succesfully !',width=20,font=("bold", 10))
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
    conn = sqlite3.connect('data.db')
    def database(self):
        with self.conn:
                cursor=self.conn.cursor()
        if self.dcolumn.get() == 'DishID' or self.dcolumn.get() == 'dishname' or self.dcolumn.get() == 'dishtype' or self.dcolumn.get() == 'availability' or self.dcolumn.get() == 'size':
            
            cursor.execute('CREATE INDEX IF NOT EXISTS dish_rest ON Menu(restid,DishID)')
            if self.dcolumn.get() == 'DishID':
                cursor.execute('UPDATE Menu SET DishID = ? WHERE restid = ? AND DishID = ?',(self.dvalue.get(),self.rid,self.d_id.get()))
            if self.dcolumn.get() == 'dishname':
                cursor.execute('UPDATE Menu SET dishname = ? WHERE restid = ? AND DishID = ?',(self.dvalue.get(),self.rid,self.d_id.get()))
            if self.dcolumn.get() == 'dishtype':
                cursor.execute('UPDATE Menu SET dishtype = ? WHERE restid = ? AND DishID = ?',(self.dvalue.get(),self.rid,self.d_id.get()))
            if self.dcolumn.get() == 'availability':
                cursor.execute('UPDATE Menu SET availability = ? WHERE restid = ? AND DishID = ?',(self.dvalue.get(),self.rid,self.d_id.get()))
            if self.dcolumn.get() == 'size':
                cursor.execute('UPDATE Menu SET size = ? WHERE restid = ? AND DishID = ?',(self.dvalue.get(),self.rid,self.d_id.get()))
            self.conn.commit()
            self.label_confirm = Label(self, text='Item Edited Succesfully !',width=20,font=("bold", 10))
            self.label_confirm.place(x=180,y=460)
        elif self.dcolumn.get() == 'price':
            if self.dvalue.get().isdigit():
                cursor.execute('CREATE INDEX IF NOT EXISTS dish_rest ON Menu(restid,DishID)')
                cursor.execute('UPDATE Menu SET price = ? WHERE restid = ? AND DishID = ?',(int(self.dvalue.get()),self.rid, self.d_id.get()))
                self.conn.commit()
                self.label_confirm = Label(self, text='Item Edited Succesfully !',width=20,font=("bold", 10))
                self.label_confirm.place(x=180,y=460)
            else:
                self.label_notvalid = Label(self, text='Invalid Value',width=20,font=("bold", 10))
                self.label_notvalid.place(x=180,y=460)
        else:
            self.label_a = Label(self, text='Invalid column',width=20,font=("bold", 10))
            self.label_a.place(x=180,y=460)
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
        conn = sqlite3.connect('data.db')
        with conn:
            cursor=conn.cursor()
        cursor.execute('SELECT * FROM Menu WHERE restid = ?',(self.rid,))
        ind=0
        for row in cursor.fetchall():
            self.label_1 = Label(self, text=row,width=80,font=("bold", 10))
            self.label_1.place(x=200,y=20+ind)
            ind=ind+40

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
        conn = sqlite3.connect('data.db')
        with conn:
            cursor=conn.cursor()
        cursor.execute('SELECT * FROM Restaurant3 WHERE RestID = ?',(rowid,))
        records = cursor.fetchall()
        current_time = tm.strftime('%H:%M:%S')
        for row in records:
            opentime=row[9]
            closetime=row[8]
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
        
        cursor.execute('UPDATE Restaurant3 SET available = ? WHERE RestID = ?',(available_status,rowid))
        conn.commit()
        cursor.execute('SELECT * FROM Restaurant3 WHERE RestID = ?',(rowid,))
        records = cursor.fetchall()
        for row in records:
            if row[0]==rowid:
                welcmsg = "Welcome "+row[1];
                self.label_1 = Label(self, text=welcmsg,width=20,font=("bold", 30))
                self.label_1.place(x=200,y=20)
                self.label_2 = Label(self, text="User Details",width=50,font=("bold", 10))
                self.label_2.place(x=100,y=80)
                strname="Restaurant Name: "+row[1]
                stremail="Restaurant Email: "+row[2]
                strphone="Restaurant Phone: "+str(row[3])
                stradd="Restaurant Address: "+row[4]
                strtype="Restaurant Type: "+row[5]
                stravgp="Restaurant Avg Price: "+str(row[6])
                strstartend="Restaurant Start-End time: "+row[9]+"-"+row[8]
                stravailable="Restaurant Availability: "+row[10]

        self.label_1 = Label(self, text=strname,width=50,font=("bold", 10))
        self.label_1.place(x=100,y=100)
        self.label_2 = Label(self, text=stremail,width=50,font=("bold", 10))
        self.label_2.place(x=100,y=120)
        self.label_3 = Label(self, text=strphone,width=50,font=("bold", 10))
        self.label_3.place(x=100,y=140)
        self.label_4 = Label(self, text=stradd,width=50,font=("bold", 10))
        self.label_4.place(x=100,y=160)
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
        
class custDash(Toplevel):
    def __init__(self,rowid):
        Toplevel.__init__(self)
        self.geometry('900x700')
        self.configure(bg='pink')
        conn = sqlite3.connect('data.db')
        with conn:
            cursor=conn.cursor()
        cursor.execute('SELECT * FROM Customer3')
        records = cursor.fetchall()
        for row in records:
            if row[0]==rowid:
                welcmsg = "Welcome "+row[1];
                self.label_1 = Label(self, text=welcmsg,width=20,font=("bold", 30))
                self.label_1.place(x=200,y=20)
                self.label_2 = Label(self, text="User Details",width=50,font=("bold", 10))
                self.label_2.place(x=100,y=80)
                strname="Name: "+row[1]
                stremail="Email: "+row[2]
                strphone="Phone: "+str(row[3])
                stradd="Address: "+row[4]
                strmem="Membership: "+row[5]
                strcoupid="Coupon ID: "+str(row[6])

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
        self.label_6 = Label(self, text=strcoupid,width=50,font=("bold", 10))
        self.label_6.place(x=100,y=200)

class comDash(Toplevel):
    def __init__(self,rowid):
        Toplevel.__init__(self)
        self.geometry('900x700')
        self.configure(bg='pink')
        conn = sqlite3.connect('data.db')
        with conn:
            cursor=conn.cursor()
        cursor.execute('SELECT * FROM ComplaintExec')
        records = cursor.fetchall()
        for row in records:
            if row[0]==rowid:
                welcmsg = "Welcome "+row[1];
                self.label_1 = Label(self, text=welcmsg,width=20,font=("bold", 30))
                self.label_1.place(x=200,y=20)
                self.label_2 = Label(self, text="User Details",width=50,font=("bold", 10))
                self.label_2.place(x=100,y=80)
                strname="Name: "+row[1]
                stremail="Email: "+row[2]
                strphone="Phone: "+str(row[3])
                stradd="Active status: "+row[5]

        self.label_1 = Label(self, text=strname,width=50,font=("bold", 10))
        self.label_1.place(x=100,y=100)
        self.label_2 = Label(self, text=stremail,width=50,font=("bold", 10))
        self.label_2.place(x=100,y=120)
        self.label_3 = Label(self, text=strphone,width=50,font=("bold", 10))
        self.label_3.place(x=100,y=140)
        self.label_4 = Label(self, text=stradd,width=50,font=("bold", 10))
        self.label_4.place(x=100,y=160)
class delDash(Toplevel):
    def __init__(self,rowid):
        Toplevel.__init__(self)
        self.geometry('900x700')
        self.configure(bg='pink')
        conn = sqlite3.connect('data.db')
        with conn:
            cursor=conn.cursor()
        cursor.execute('SELECT * FROM DeliveryExec')
        records = cursor.fetchall()
        for row in records:
            if row[0]==rowid:
                welcmsg = "Welcome "+row[1];
                self.label_1 = Label(self, text=welcmsg,width=20,font=("bold", 30))
                self.label_1.place(x=200,y=20)
                self.label_2 = Label(self, text="User Details",width=50,font=("bold", 10))
                self.label_2.place(x=100,y=80)
                strname="Name: "+row[1]
                stremail="Email: "+row[2]
                strphone="Phone: "+str(row[3])
                stradd="Age: "+str(row[5])
                stractivestatus="Active Status: "+row[6]

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
class restsignin(Toplevel):
  restemail=StringVar()
  Password=StringVar()
  
  def database(self):
      conn = sqlite3.connect('data.db')
      with conn:
            cursor=conn.cursor()
      strrest = self.restemail.get()
      cursor.execute('CREATE INDEX IF NOT EXISTS rest_email ON Restaurant3(restemail)')
      conn.commit()
      cursor.execute('SELECT COUNT(*) FROM Restaurant3 WHERE restemail = ?',(strrest,))
      records = cursor.fetchall()
      for row in records:
          cnt = row[0]
      if cnt == 0:
          self.label_1 = Label(self, text="Email Address does not exist",width=20,font=("bold", 10))
          self.label_1.place(x=110,y=200)
      else:
          cursor.execute('SELECT * FROM Restaurant3 WHERE restemail = ?',(strrest,))
          records = cursor.fetchall()
          for row in records:
              if row[7]!=self.Password.get():
                  self.label_pass = Label(self, text="Wrong Password",width=20,font=("bold", 10))
                  self.label_pass.place(x=140,y=200)
              else:
                  restDash(row[0]) 
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
      conn = sqlite3.connect('data.db')
      with conn:
            cursor=conn.cursor()
      strcust = self.Email

      cursor.execute('SELECT * FROM Customer3')
      records = cursor.fetchall()
      flag=0
      flag2=0
      for row in records:
          if row[2] == self.Email.get():
              flag=1
              if row[6] == self.pas.get():
                     flag2=1
                     custDash(row[0])
              break
      if flag==0:
          self.label_1 = Label(self, text="Email Address does not exist",width=20,font=("bold", 10))
          self.label_1.place(x=110,y=200)
      if flag2==0:
          self.label_pass = Label(self, text="Wrong Password",width=20,font=("bold", 10))
          self.label_pass.place(x=140,y=200)
  def __init__(self):
    Toplevel.__init__(self)
    self.geometry('500x500')
    self.label_1 = Label(self, text="Enter your email",width=20,font=("bold", 10))
    self.label_1.place(x=50,y=53)
    
    self.entry_1 = Entry(self,textvar=self.Email)
    self.entry_1.place(x=270,y=53)

    self.label_2 = Label(self, text="Enter Password",width=20,font=("bold", 10))
    self.label_2.place(x=50,y=93)
    
    self.entry_2 = Entry(self,textvar=self.pas)
    self.entry_2.place(x=270,y=93)
    Button(self, text='Submit',width=20,bg='brown',fg='white',command=self.database).place(x=180,y=150)

class complaintsignin(Toplevel):
  comemail = StringVar()
  pas = StringVar()
  def database(self):
      conn = sqlite3.connect('data.db')
      with conn:
            cursor=conn.cursor()
      strrest = self.comemail.get()
      cursor.execute('CREATE INDEX IF NOT EXISTS com_email ON ComplaintExec(comemail)')
      conn.commit()
      cursor.execute('SELECT COUNT(*) FROM ComplaintExec WHERE comemail = ?',(strrest,))
      records = cursor.fetchall()
      for row in records:
          cnt = row[0]
      if cnt == 0:
          self.label_1 = Label(self, text="Email Address does not exist",width=20,font=("bold", 10))
          self.label_1.place(x=110,y=200)
      else:
          cursor.execute('SELECT * FROM ComplaintExec WHERE comemail = ?',(strrest,))
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

class deliveryexecsignin(Toplevel):
  delemail = StringVar()
  pas = StringVar()
  def database(self):
      conn = sqlite3.connect('data.db')
      with conn:
            cursor=conn.cursor()
      strrest = self.delemail.get()
      cursor.execute('CREATE INDEX IF NOT EXISTS del_email ON DeliveryExec(delemail)')
      conn.commit()
      cursor.execute('SELECT COUNT(*) FROM DeliveryExec WHERE delemail = ?',(strrest,))
      records = cursor.fetchall()
      for row in records:
          cnt = row[0]
      if cnt == 0:
          self.label_1 = Label(self, text="Email Address does not exist",width=20,font=("bold", 10))
          self.label_1.place(x=110,y=200)
      else:
          cursor.execute('SELECT * FROM DeliveryExec WHERE delemail = ?',(strrest,))
          records = cursor.fetchall()
          for row in records:
              if row[5]!=self.pas.get():
                  self.label_pass = Label(self, text="Wrong Password",width=20,font=("bold", 10))
                  self.label_pass.place(x=140,y=200)
              else:
                  delDash(row[0]) 
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
