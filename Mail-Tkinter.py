from tkinter import *
import smtplib,ssl
password=''
sender_email=''
reciver_email=''
msg=''
m = Tk()
m.geometry('500x500')
m.title("Registration Form")
def SUBMIT():
    global sender_email
    global reciver_email
    global msg
    global password
    sender_email=entry_1.get()
    password=entry_2.get()
    reciver_email=entry_3.get()
    msg='Subject: '+entry_4.get()

label_0 = Label(m, text="MAIL-SERVICE",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(m, text="From",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(m)
entry_1.place(x=240,y=130)

label_2 = Label(m, text="Password",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(m)
entry_2.place(x=240,y=180)

label_3 = Label(m, text="To",width=20,font=("bold", 10))
label_3.place(x=68,y=230)

entry_3 = Entry(m)
entry_3.place(x=240,y=230)

label_4 = Label(m, text="Subject",width=20,font=("bold", 10))
label_4.place(x=68,y=280)

entry_4 = Entry(m)
entry_4.place(x=240,y=280)

Button(m, text='Submit',width=20,bg='brown',fg='white',command=SUBMIT).place(x=180,y=380)

m.mainloop()
