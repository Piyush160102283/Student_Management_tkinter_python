#tkguifile for Student Management Project
import tkinter as tk
import databasefile
mainWindow = tk.Tk()
mainWindow.title("Student Management Project")

heading_label = tk.Label(mainWindow,text='STUDENT RECORDS', bg="red", fg="white", pady=10,width=100)
# heading_label.pack()


heading_label2 = tk.Label(mainWindow,text='')
# heading_label2.pack()

name_label = tk.Label(mainWindow,text='NAME OF THE STUDENT : ', bg="black", fg="white", pady=10)
name_field = tk.Entry(mainWindow)
# name_label.pack()
# name_field.pack(pady=10)

rollno_label = tk.Label(mainWindow,text='ROLL NUMBER : ', bg="black", fg="white", pady=10)
rollno_field = tk.Entry(mainWindow)
# rollno_label.pack()
# rollno_field.pack(pady=10)


sapid_label = tk.Label(mainWindow,text='SAP ID : ', bg="black", fg="white", pady=10)
sapid_field = tk.Entry(mainWindow)
# sapid_label.pack()
# sapid_field.pack(pady=10)

college_label = tk.Label(mainWindow,text='College : ', bg="black", fg="white", pady=10)
college_field = tk.Entry(mainWindow)
# college_label.pack()
# college_field.pack(pady=10)


address_label = tk.Label(mainWindow,text='Address : ', bg="black", fg="white", pady=10)
address_field = tk.Entry(mainWindow)
# address_label.pack()
# address_field.pack(pady=10)

emailid_label = tk.Label(mainWindow,text='EMAIL ID : ', bg="black", fg="white", pady=10)
emailid_field = tk.Entry(mainWindow)
# emailid_label.pack()
# emailid_field.pack(pady=10)


mobileno_label = tk.Label(mainWindow,text='MOBILE NUMBER : ', bg="black", fg="white", pady=10)
mobileno_field = tk.Entry(mainWindow)
# mobileno_label.pack()
# mobileno_field.pack(pady=10)

showall_button = tk.Button(mainWindow,text='SHOW ALL RECORD',command=lambda: databasefile.showall_data())
# showall_button.pack(padx=5, pady=10, side=tk.LEFT)
show_button = tk.Button(mainWindow,text='   fetch details',command=lambda: databasefile.show_data(rollno_field.get()))
# show_button.pack(padx=5, pady=10, side=tk.RIGHT)
insert_button = tk.Button(mainWindow,text='CREATE RECORD',command=lambda: databasefile.insert_data(name_field.get(),rollno_field.get(),sapid_field.get(),college_field.get(),address_field.get(),emailid_field.get(),mobileno_field.get()))
# insert_button.pack(padx=5, pady=10, side=tk.RIGHT)
delete_button = tk.Button(mainWindow,text='DELETE RECORD',command=lambda: databasefile.delete_data(rollno_field.get()))
# delete_button.pack(padx=5, pady=10, side=tk.LEFT)

heading_label.grid(row=0,column=0)
heading_label2.grid(row=1,column=0)
name_label.grid(row=2,column=0)
name_field.grid(row=2,column=1)
rollno_label.grid(row=3,column=0)
rollno_field.grid(row=3,column=1)
sapid_label.grid(row=4,column=0)
sapid_field.grid(row=4,column=1)
college_label.grid(row=5,column=0)
college_field.grid(row=5,column=1)
address_label.grid(row=6,column=0)
address_field.grid(row=6,column=1)
emailid_label.grid(row=7,column=0)
emailid_field.grid(row=7,column=1)
mobileno_label.grid(row=8,column=0)
mobileno_field.grid(row=8,column=1)

showall_button.grid(row=11,column=0)
show_button.grid(row=12,column=0)
insert_button.grid(row=11,column=1)
delete_button.grid(row=12,column=1)

mainWindow.mainloop()