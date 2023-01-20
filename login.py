from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import os

def login():
    
    user=username.get()
    code=password.get()
    
    if user=="gkp" and code=="1234":
        
        win=Toplevel(root)       
        win.configure(bg="#d7dae2")
        win.resizable(False,False)
        win.title("Management Of System")
        win.state('zoomed')
        
      # Copy and past another page

        def spd():
        
                if e1.get()=="" or e2.get()=="":
                        messagebox.showerror("Error","All Fields required")
                else:
                    conn=mysql.connector.connect(host='localhost', username="root", password="mk1234", database="mydata")
                    my_cursor = conn.cursor()
                    my_cursor.execute("insert into hospital values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                            nameoftablets.get(),
                            ref.get(),
                            dose.get(),
                            nooftablets.get(),
                            issuedate.get(),
                            expdate.get(),
                            dailydose.get(),
                            sideeffect.get(),
                            nameofpatient.get(),
                            dob.get(),
                            patientaddress.get()   
                        ))
                    conn.commit()
                    fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Record inserted") 
                    clr() 
            
        def fetch_data():
                conn=mysql.connector.connect(host='localhost', username="root", password="mk1234", database="mydata")
                my_cursor = conn.cursor()
                my_cursor.execute('select * from hospital')
                rows = my_cursor.fetchall()
                if len(rows)!=0:
                        table.delete(* table.get_children())
                        for item in rows:
                                table.insert('',END,values=item)
                        conn.commit()
                        conn.close() 
                clr()  

        def get_data(event=''):
                cursor_row = table.focus()
                data = table.item(cursor_row)
                row = data['values']
                nameoftablets.set(row[0])
                ref.set(row[1])
                dose.set(row[2])
                nooftablets.set(row[3])
                issuedate.set(row[4])
                expdate.set(row[5])
                dailydose.set(row[6])
                sideeffect.set(row[7])
                nameofpatient.set(row[8])
                dob.set(row[9])
                patientaddress.set(row[10])   
#_________prescription Data________
        def presc():
                txt_frme.insert(END,'\tName Of Tablets\t\t:\t'+ nameoftablets.get()+'\n')
                txt_frme.insert(END,'\tReference No\t\t:\t'+ref.get()+'\n')
                txt_frme.insert(END,'\tDose\t\t:\t'+dose.get()+'\n')
                txt_frme.insert(END,'\tNo. Of Tablets\t\t:\t'+nooftablets.get()+'\n')
                txt_frme.insert(END,'\tIssue Date\t\t:\t'+issuedate.get()+'\n')
                txt_frme.insert(END,'\tExpiry Date\t\t:\t'+expdate.get()+'\n')
                txt_frme.insert(END,'\tDaily Dose\t\t:\t'+dailydose.get()+'\n')
                txt_frme.insert(END,'\tSide Effect\t\t:\t'+sideeffect.get()+'\n')
                txt_frme.insert(END,'\tBlood Pressure\t\t:\t'+bloodpressure.get()+'\n')
                txt_frme.insert(END,'\tStorage Device\t\t:\t'+storage.get()+'\n')
                txt_frme.insert(END,'\tMedication\t\t:\t'+medication.get()+'\n')
                txt_frme.insert(END,'\tPatient_ID\t\t:\t'+patientid.get()+'\n')
                txt_frme.insert(END,'\tName of Patient\t\t:\t'+nameofpatient.get()+'\n')
                txt_frme.insert(END,'\tDate OF Birth\t\t:\t'+dob.get()+'\n')
                txt_frme.insert(END,'\tPatient Address\t\t:\t'+patientaddress.get()+'\n')
#-----Delete button------
        def delete():
                conn=mysql.connector.connect(host="LocalHost",username="root",password="mk1234",database='mydata')
                my_cursor=conn.cursor()
        
                querry=('delete from hospital where Reference = %s')
                value = (ref.get(),)
                confirm = messagebox.askyesno('Confirmmation','Are you sure! Want to Delete')
                if confirm>0:
                        my_cursor.execute(querry,value)
                        messagebox.showinfo('Deleted','Patient Record Has Deleted')
                
                else:
                      messagebox.showinfo('Save','Record not Deleted')
                conn.commit()
                conn.close()
                fetch_data()
       
#---------clear button---------------
        def clr():
                nameoftablets.set('')
                ref.set('')
                dose.set('')
                nooftablets.set('')
                issuedate.set('')
                expdate.set('')
                dailydose.set('')
                sideeffect.set('')
                bloodpressure.set('')
                storage.set('')
                medication.set('')
                patientid.set('')
                nameofpatient.set('')
                dob.set('')
                patientaddress.set('')
                txt_frme.delete(1.0,END)
#-------------EXIT BUTTON----------------
        def ext():
                confirm=messagebox.askyesno('confirmation','Are You sure want to Exit')
                if confirm>0:
                        win.destroy()
                        return
#------update_btn-----------------
        def update():     
                       
                    nameoftab=e1.get()
                    ref=e2.get()
                    dos=e3.get()
                    nooftab=e4.get()
                    issdate=e5.get()
                    exdate=e6.get()
                    dailydos=e7.get()
                    sideeff=e8.get()
                    nameofpat=e13.get()
                    dobp=e14.get()
                    pataddress=e15.get()
                    if(ref==""):
                        messagebox.showinfo("update","First Field is required")
                    else:
                        conn=mysql.connector.connect(host="Localhost",username="root", password="mk1234",database="mydata")
                        my_cursor=conn.cursor()
                        querry = "update hospital set NameofTablets=%s,Doses=%s,NoofTablets=%s,IssuedDate=%s,ExpiryDate=%s,DailyDose=%s,SideEffect=%s,PatientName=%s,DateOfBirth=%s,PatientAddress=%s where Reference=%s"
                        data=(nameoftab,dos,nooftab,issdate,exdate,dailydos,sideeff,nameofpat,dobp,pataddress,ref)
               
                        try:
                           my_cursor.execute(querry,data)         
                           conn.commit ()                   
                           messagebox.showinfo('Update','Record Updated')
                           fetch_data()
                           conn.close()  
                        except:
                           messagebox.showinfo('Warning','eRROR')
#--------------Searching button-----------------
        def search():
                sref=str(e2.get())
                if(sref==""):
                        messagebox.showinfo("Alert","Enter Reference Number")
                else:
                        conn=mysql.connector.connect(host="Localhost",username="root", password="mk1234",database="mydata")
                        my_cursor=conn.cursor()
                
                        try:
                           my_cursor.execute(" select * from hospital where Reference='"+sref+"' ")
                           row=my_cursor.fetchall()
                           for x in row:
                             txt_frme2.insert(END,'\tName of Tablets\t\t:\t'+x[0]+'\n\n')
                             txt_frme2.insert(END,'\tReference\t\t:\t'+x[1]+'\n\n')
                             txt_frme2.insert(END,'\tDose\t\t:\t'+x[2]+'\n\n')
                             txt_frme2.insert(END,'\tNo of Tablets\t\t:\t'+x[3]+'\n\n')
                             txt_frme2.insert(END,'\tIssue Date\t\t:\t'+x[4]+'\n\n')
                             txt_frme2.insert(END,'\tExpiry Date\t\t:\t'+x[5]+'\n\n')
                             txt_frme2.insert(END,'\tDaily Dose\t\t:\t'+x[6]+'\n\n')
                             txt_frme2.insert(END,'\tSide Effect\t\t:\t'+x[7]+'\n\n')
                             txt_frme2.insert(END,'\tName of Patient\t\t:\t'+x[8]+'\n\n')
                             txt_frme2.insert(END,'\tDate of Birth\t\t:\t'+x[9]+'\n\n')
                             txt_frme2.insert(END,'\tAddress\t\t:\t'+x[10]+'\n\n')                              
                             conn.commit()
                             conn.close()
                        except:
                           messagebox.showinfo('warning','somthing wrong')
                
#Heading
        Label(win,text='Hospital Management System',font='impack 31 bold',bg='cyan',fg='white').pack(fill=X)
#Frame1
        frame1=Frame(win,bd=15,relief=RIDGE)
        frame1.place(x=0,y=50,width=1920,height=510)
#Label Frame for patient info
        lf1=LabelFrame(frame1,text='Patient Information',font='ariel 12 bold',bd=10,bg='pink')
        lf1.place(x=10,y=0,width=950,height=480)
#label frame for prescription
        lf2=LabelFrame(frame1,text='Prescription',font='ariel 12 bold',bd=10,bg='#7F7FFF')
        lf2.place(x=960,y=0,width=460,height=480)
#label frame for search
        lf3=LabelFrame(frame1,text='Search Record',font='ariel 12 bold',bd=10,bg='cyan')
        lf3.place(x=1430,y=0,width=460,height=480)
#textbox for prescription
        txt_frme=Text(lf2,font='impack 10 bold',width=40,height=30,bg='#FFFFD3')
        txt_frme.pack(fill=BOTH)
#text box for search
        txt_frme2=Text(lf3,font='impack 10 bold',width=40,height=30,bg='white')
        txt_frme2.pack(fill=BOTH)
#Label for patient information
        Label(lf1,text='Name of tablets',bg='pink').place(x=5,y=10)
        Label(lf1,text='Reference No.',bg='pink').place(x=5,y=40)
        Label(lf1,text='Dose',bg='pink',).place(x=5,y=70)
        Label(lf1,text='No. Of Tablets',bg='pink').place(x=5,y=100)
        Label(lf1,text='Issue Date',bg='pink').place(x=5,y=130)
        Label(lf1,text='Expiry Date',bg='pink').place(x=5,y=160)
        Label(lf1,text='Daily Dose',bg='pink').place(x=5,y=190)
        Label(lf1,text='Side Effect',bg='pink').place(x=5,y=220)
#Label(lf1,text='No Of Teblets',bg='Pink').place(x=350,y=10)
        Label(lf1,text='Blood Pressure',bg='pink').place(x=350,y=40)
        Label(lf1,text='Storage Device',bg='pink').place(x=350,y=70)
        Label(lf1,text='Medication',bg='pink').place(x=350,y=100)
        Label(lf1,text='Patient_ID',bg='Pink').place(x=350,y=130)
        Label(lf1,text='Name OF Patient',bg='pink').place(x=350,y=160)
        Label(lf1,text='DOB',bg='Pink').place(x=350,y=200)
        Label(lf1,text='Patient Address',bg='Pink').place(x=350,y=230)
# Text variable for every entry field
        nameoftablets = StringVar()
        ref = StringVar()
        dose = StringVar()
        nooftablets = StringVar()
        issuedate = StringVar()
        expdate = StringVar()
        dailydose = StringVar()
        sideeffect = StringVar()
        bloodpressure = StringVar()
        storage = StringVar()
        medication = StringVar()
        patientid = StringVar()
        nameofpatient = StringVar()
        dob = StringVar()
        patientaddress = StringVar()

#Entry Field for all Label
        e1=Entry(lf1,bd=4,textvariable=nameoftablets)
        e1.place(x=100,y=10,width=200)
        e2=Entry(lf1,bd=4,textvariable=ref)
        e2.place(x=100,y=40,width=200)
        e3=Entry(lf1,bd=4,textvariable=dose)
        e3.place(x=100,y=70,width=200)
        e4=Entry(lf1,bd=4,textvariable=nooftablets)
        e4.place(x=100,y=100,width=200)
        e5=Entry(lf1,bd=4,textvariable=issuedate)
        e5.place(x=100,y=130,width=200)
        e6=Entry(lf1,bd=4,textvariable=expdate)
        e6.place(x=100,y=160,width=200)
        e7=Entry(lf1,bd=4,textvariable=dailydose)
        e7.place(x=100,y=190,width=200)
        e8=Entry(lf1,bd=4,textvariable=sideeffect)
        e8.place(x=100,y=220,width=200)
        e9=Entry(lf1,bd=4,textvariable=bloodpressure)
        e9.place(x=460,y=40,width=200)
        e10=Entry(lf1,bd=4,textvariable=storage)
        e10.place(x=460,y=70,width=200)
        e11=Entry(lf1,bd=4,textvariable=medication)
        e11.place(x=460,y=100,width=200)
        e12=Entry(lf1,bd=4,textvariable=patientid)
        e12.place(x=460,y=130,width=200)
        e13=Entry(lf1,bd=4,textvariable=nameofpatient)
        e13.place(x=460,y=160,width=200)
        e14=Entry(lf1,bd=4,textvariable=dob)
        e14.place(x=460,y=190,width=200)
        e15=Entry(lf1,bd=4,textvariable=patientaddress)
        e15.place(x=460,y=230,width=200)
#frame2
        frame2=Frame(win,bd=15,relief=RIDGE)
        frame2.place(x=0,y=560,width=1920,height=400)
#Button
#deleteB
        d_btn=Button(win,text='Delete',font='ariel 15 bold', bg='brown',fg='white',bd=6,cursor='hand2',command=delete)
        d_btn.place(x=0,y=955,width=180)
#prescription
        p_btn=Button(win,text='Prescription',font='ariel 15 bold',bg='blue',fg='white',bd=6,cursor='hand2',command = presc)
        p_btn.place(x=180,y=955,width=190)
#save_prescription_Data
        pd_btn=Button(win,text='Save Prescription Data',font='ariel 15 bold',bg='green',fg='white',bd=6,cursor='hand2',command=spd)
        pd_btn.place(x=370,y=955,width=250)
#clearB
        c_btn=Button(win,text='Clear',font='ariel 15 bold',bg='blue',fg='white',bd=6,cursor='hand2',command=clr)
        c_btn.place(x=620,y=955,width=190)
#Exit_B
        e_btn=Button(win,text='Exit',font='ariel 15 bold',bg='pink',fg='white',bd=6,cursor='hand2',command=ext)
        e_btn.place(x=810,y=955,width=170)
#update_B
        e_btn=Button(win,text='UPDATE RECORD',font='ariel 15 bold',bg='blue',fg='white',bd=6,cursor='hand2',command=update)
        e_btn.place(x=980,y=955,width=200)
        e_btn=Button(win,text='Search',font='ariel 15 bold',bg='pink',fg='white',bd=6,cursor='hand2',command=search)
        e_btn.place(x=1180,y=955,width=200)
#scroll Bar for prescription Data
        scroll_x=ttk.Scrollbar(frame2,orient=HORIZONTAL)
        scroll_x.pack(side='bottom',fill='x')
        scroll_y=ttk.Scrollbar(frame2,orient=VERTICAL)
        scroll_y.pack(side='right',fill='y')
        table=ttk.Treeview(frame2,columns=('not','ref','dose','nots','issd','expd','dd','se','pn','dob','pa'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
        scroll_x=ttk.Scrollbar(command=table.xview)
        scroll_y=ttk.Scrollbar(command=table.yview)
#Heading for prescription data
        table.heading('not',text='Name of Tablets')
        table.column('not',width=100)
        table.heading('ref',text='Reference')
        table.column('ref',width=100)
        table.heading('dose',text='Dose')
        table.column('dose',width=100)
        table.heading('nots',text='No of Tablets')
        table.column('nots',width=100)
        table.heading('issd',text='Issued Date')
        table.column('issd',width=100)
        table.heading('expd',text='Expiry Date')
        table.column('expd',width=100)
        table.heading('dd',text='Daily Dose')
        table.column('dd',width=100)
        table.heading('se',text='Side Effect')
        table.column('se',width=100)
        table.heading('pn',text='Patient Name')
        table.column('pn',width=100)
        table.heading('dob',text='Date Of Birth')
        table.column('dob',width=100)
        table.heading('pa',text='Patient Address')
        table.column('pa',width=100)
        table['show']='headings'
        table.pack(fill=BOTH,expand=1)
        table.bind('<ButtonRelease-1>',get_data)
        fetch_data()
      #end of code
      #alert if wrong user pass
    elif user=="" and code=="":
        messagebox.showerror("invalid","please Enter User and Pass")
    elif user=="":
        messagebox.showerror("invalid","plase enter user")
    elif code=="":
        messagebox.showerror("invalid","please enter pass")
    elif user!="gkp" and code!="1234":
        messagebox.showerror("invalid","wrong user and pass")
    elif user!="gkp":
        messagebox.showerror("invalid","wrong user")
    elif code!="1234":
        messagebox.showerror("invalid","wrong Pass")
    
def main_screen():
    global root
    global username
    global password
    
    root=Tk()
    root.geometry("750x560+150+80")
    root.resizable(False,False)
    root.attributes("-toolwindow",True)
    root.config(bg='white',bd=5)
    root.title('Login Page')
   #icon
    lbltitle=Label(text="Login System",font=("arial",40, 'bold'),fg="black",bg="white")
    lbltitle.pack(pady=0)
    img=PhotoImage(name="img1",file="logig.png")
    img1=img.subsample(2,2)
    Label(root,image=img1).pack()
    bordercolor=Frame(root,bg="black",width=700,height=300)
    bordercolor.pack()
    mainfrm=Frame(bordercolor,bg="#9898F5",width=700,height=300)
    mainfrm.pack(padx=20,pady=20)
    
    Label(mainfrm,text="USER NAME:",font=("arial",30,"bold"),bg="#9898F5").place(x=100,y=50)
    Label(mainfrm,text="PASSWORD:",font=("arial",30,"bold"),bg="#9898F5").place(x=100,y=150)
    username=StringVar()
    password=StringVar()
    entry_username=Entry(mainfrm,textvariable=username,width=12,bd=2,font=("arial", 30))
    entry_username.place(x=400,y=50)
    entry_pass=Entry(mainfrm,textvariable=password,width=12,bd=2,font=("arial",30),show="*")
    entry_pass.place(x=400,y=150)
    
    def reset():
           
        entry_username.delete(0,END)
        entry_pass.delete(0,END)
    def signup():
            wsign=Toplevel(root)
            wsign.title("Signup User")
            wsign.geometry("350x550")
            wsign.config(bg="#FFFFB9",bd=4)
            
            def userregister():
                        if ftname.get()=="" or empid.get()=="" or email_id.get()=="" or mobileNo.get()=="" :
                                 messagebox.showerror("Alert","Name, Emp_id,email_id and mobileNo is required")
                        else:
                                 conn=mysql.connector.connect(host='localhost', username='root',password='mk1234',database='mydata')
                                 mycursor=conn.cursor()
                                 try:
                                        mycursor.execute("insert into emplogin values(%s,%s,%s,%s)",(
                                                 ftname.get(),
                                                 empid.get(),
                                                 email_id.get(),
                                                 mobileNo.get()
                                         ))
                                        conn.commit()
                                        conn.close()
                                        messagebox.showinfo("Welcome","Registration Done")
                                 except:
                                       messagebox.showerror("Alert","Something is Wrong!")
    
            Label(wsign,text="SIGN UP",font=("arial",25,"bold"),bg="cyan").pack(fill=X)
            signfrm=Frame(wsign,bg="black",width=500,height=600)
            signfrm.pack(padx=5,pady=5)
            outfrm=Frame(signfrm,bg="gray",width=450,height=600)
            outfrm.pack(padx=20,pady=20)
            
            Label(outfrm,text="Full Name",font=("arial",10,"bold"),bg="#9898F5").place(x=25,y=80)
            Label(outfrm,text="EMP_ID",font=("arial",10,"bold"),bg="#9898F5").place(x=25,y=120)
            Label(outfrm,text="Email",font=("arial",10,"bold"),bg="#9898F5").place(x=25,y=160)
            Label(outfrm,text="Mobile No",font=("arial",10,"bold"),bg="#9898F5").place(x=25,y=200)
            firstname=StringVar()
            emp_id=StringVar()
            email=StringVar()
            mobilno=StringVar()
            ftname=Entry(outfrm,textvariable=firstname,width=20,bd=2,font=("arial",10))
            ftname.place(x=120,y=80)
            empid=Entry(outfrm,textvariable=emp_id,width=20,bd=2,font=("arial",10))
            empid.place(x=120,y=120)
            email_id=Entry(outfrm,textvariable=email,width=20,bd=2,font=("arial",10))
            email_id.place(x=120,y=160)
            mobileNo=Entry(outfrm,textvariable=mobilno,width=20,bd=2,font=("arial",10))
            mobileNo.place(x=120,y=200)
            Button(outfrm,text="Register",height=2,width=15,bg="#1089ff",fg="white",bd=2,command=userregister).place(x=15,y=300)
            Button(outfrm,text="Cancel",height=2,width=15,bg="#00bd56",fg="white",bd=2,command=wsign.destroy).place(x=170,y=300)
    #Button
    Button(mainfrm,text="LOGIN",height=2,width=15,bg="#ed3833",fg="white",bd=2,command=login).place(x=250,y=250)
    Button(mainfrm,text="RESET",height=2,width=15,bg="#1089ff",fg="white",bd=2,command=reset).place(x=400,y=250)
    Button(mainfrm,text="EXIT",height=2,width=15,bg="#00bd56",fg="white",bd=2,command=root.destroy).place(x=550,y=250)
    Button(mainfrm,text="NEW USER",height=2,width=15,bg="#E9E996",fg="#8F8FBC",bd=2,command=signup).place(x=50,y=250)
    root.mainloop()
main_screen()
