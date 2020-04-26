from tkinter import *
import sqlite3
root = Tk()
root.geometry('900x700')
root.title("HomePage")
root.configure(bg='green')
# Homepage with Customer Sign Up linked with database
class customer(Toplevel):
    Fullname=StringVar()
    Email=StringVar()
    phonenum = IntVar()
    c=StringVar()
    mem= StringVar()
    pas = StringVar()
    coupid = IntVar()
    conn = sqlite3.connect('data.db')
    def database(self):
       name1=self.Fullname.get()
       email=self.Email.get()
       phone=self.phonenum.get()
       address=self.c.get()
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
        self.entry_4 = Entry(self,textvar=self.c)
        self.entry_4.place(x=240,y=280)

        self.label_5 = Label(self, text="Membership",width=20,font=("bold", 10))
        self.label_5.place(x=85,y=330)
        self.entry_5 = Entry(self,textvar=self.mem)
        self.entry_5.place(x=240,y=330)
        self.label_6 = Label(self, text="Password",width=20,font=("bold", 10))
        self.label_6.place(x=85,y=380)
        self.entry_6 = Entry(self,textvar=self.pas)
        self.entry_6.place(x=240,y=380)

        self.label_7 = Label(self, text="Coupon ID",width=20,font=("bold", 10))
        self.label_7.place(x=85,y=430)
        self.entry_7 = Entry(self,textvar=self.coupid)
        self.entry_7.place(x=240,y=430)
        Button(self, text='Submit',width=20,bg='brown',fg='white',command=self.database).place(x=180,y=480)

def cust():
    customer()

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
Button(root, text='Restraunt SignUp',width=20,bg='brown',fg='white').place(x=300,y=330)
Button(root, text='Complaint Executive SignUp',width=25,bg='brown',fg='white').place(x=500,y=330)
Button(root, text='Delivery Executive SignUp',width=20,bg='brown',fg='white').place(x=700,y=330)
root.mainloop()
