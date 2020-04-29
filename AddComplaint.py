from tkinter import *
import sqlite3
import time as tm

class AddComplaint(Toplevel):
    c_type=IntVar()
    c_desc= StringVar()
    c_execid=-1
    conn=sqlite3.connect('data.db')

    def database(self):

        with self.conn:
            cursor=self.conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Complaints (com_id INT, com_type TEXT,description TEXT,cust_id INT,exec_id INT,status TEXT, order_id INT)')
        cursor.execute('SELECT COUNT(*) FROM Complaints')
        records = cursor.fetchall()
        for row in records:
            n = int(row[0])
        n=n+1
        com_id=str(n)

        cursor.execute('SELECT ComId,activestatus FROM ComplaintExec')
        records=cursor.fetchall()
        
        for row in records:
            if row[1]=="Not Active":
                c_execid=row[0]
                cursor.execute(f"UPDATE ComplaintExec SET activestatus='Active' WHERE ComId={row[0]}")
                self.conn.commit()
                break
        cursor.execute('INSERT INTO Complaints (com_id,com_type,description,cust_id,exec_id,order_id,status) VALUES (?,?,?,?,?,?,?)',(n,self.c_type,self.c_desc,self.cust_id,self.c_execid,self.order_id,"OPEN"))
        self.conn.commit()


    
    
    def __init__(self,cust_id,order_id):
        Toplevel.__init__(self)
        self.geometry('500x600')

        self.cust_id=cust_id
        self.order_id=order_id

        self.label_0= Label(self,text="Complaint Center",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)

        self.label_1= Label(self,text=f"Registering Complaint for Order #{order_id} ",width=20,font=("bold",15))
        self.label_1.place(x=90,y=100)

        self.label_2= Label(self,text="Complaint Type",width=20,font=("bold", 10))
        self.label_2.place(x=80,y=150)

        self.entry_1 = Entry(self,textvar=self.c_type)
        self.entry_1.place(x=240,y=150)

        self.label_3= Label(self,text="Complaint Description",width=20,font=("bold", 10))
        self.label_3.place(x=80,y=230)
        
        self.entry_2 = Entry(self,textvar=self.c_desc)
        self.entry_2.place(x=240,y=230)

        Button(self,text='Submit',width=20,bg='brown',fg='white',command=self.database).place(x=180,y=300)


    
