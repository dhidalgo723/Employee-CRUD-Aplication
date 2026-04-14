from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()
window.geometry("600x270")
window.title("Employee CRUD App")

empld = Label(window, text="Employee ID", font=("Seriff", 12))
empld.place(x=20, y=60)

empDept = Label(window, text="Employee Dept", font=("Seriff", 12))
empDept.place(x=20, y=90)

enterId = Entry(window)
enterId.place(x=170, y=30)

enterName = Entry(window)
enterName.place(x=170, y=60)

enterDept = Entry(window)
enterDept.place(x=170, y=90)

insertBtn = Button(window, text="Insert", font=("Seriff", 12), bg="white", command=insertData)
insertBtn.place(x=20, y=160)

updateBtn = Button(window, text="Update", font=("Seriff", 12), bg="white", command=updateData)
updateBtn.place(x=80, y=160)

getBtn = Button(window, text="Fetch", font=("Seriff", 12), bg="white", command=getData)
getBtn.place(x=150, y=160)

deleteBtn = Button(window, text="Delete", font=("Seriff", 12), bg="white", command=deleteData)
deleteBtn.place(x=210, y=160)

resetBtn = Button(window, text="Reset", font=("Seriff", 12), bg="white", command=resetFields)
resetBtn.place(x=20, y=210)

showData = Listbox(window)
showData.place(x=330, y=30)

def insertData():
    id = enterId.get()
    name = enterName.get()
    dept = enterDept.get()
    
    if(id == "" or name == "" or dept == ""):
        messagebox.showerror("Cannot Insert", "All the fields are required")
    else:
        myDB = mysql.connector.connect(host="localhost", user="root", password="YOUR_PASSWORD", database="employee")
        myCur = myDB.cursor()
        myCur.execute("insert into empDetails values('"+id+"', '"+name+"', '"+dept+"')")
        myDB.commit()
        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end")
        messagebox.showinfo("Data Inserted", "Data has been inserted successfully")
        myDB.close()

def updateData():
    id = enterId.get()
    name = enterName.get()
    dept = enterDept.get()

    if(id == "" or name == "" or dept == ""):
        messagebox.showerror("Cannot Update", "All the fields are required")
    else:
        myDB = mysql.connector.connect(host="localhost", user="root", password="YOUR_PASSWORD", database="employee")
        myCur = myDB.cursor()
        myCur.execute("UPDATE empDetails SET name='"+name+"', dept='"+dept+"' WHERE id='"+id+"'")
        myDB.commit()
        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end")
        messagebox.showinfo("Data Updated", "Data has been updated successfully")
        myDB.close()

def getData():
    if(enterId.get() == ""):
        messagebox.showwarning("Fetch Status", "Please provide the Emp ID to fetch the data")
    else:
        myDB = mysql.connector.connect(host="localhost", user="root", password="YOUR_PASSWORD", database="employee")
        myCur = myDB.cursor()
        myCur.execute("SELECT * FROM empDetails WHERE id='"+enterId.get()+"'")
        rows = myCur.fetchall()
        for row in rows:
            enterName.insert(0, row[1])
            enterDept.insert(0, row[2])
        myDB.close()

def deleteData():
    if(enterId.get() == ""):
        messagebox.showwarning("Delete Status", "Please provide the Emp ID to delete the data")
    else:
        myDB = mysql.connector.connect(host="localhost", user="root", password="YOUR_PASSWORD", database="employee")
        myCur = myDB.cursor()
        myCur.execute("DELETE FROM empDetails WHERE id='"+enterId.get()+"'")
        myDB.commit()
        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end")
        
        messagebox.showinfo("Data Deleted", "Data has been deleted successfully")
        myDB.close()

def show():
    myDB = mysql.connector.connect(host="localhost", user="root", password="YOUR_PASSWORD", database="employee")
    myCur = myDB.cursor()
    myCur.execute("SELECT * FROM empDetails")
    rows = myCur.fetchall()
    showData.delete(0, showData.size)
    
    for row in rows:
        addData = str(row[0]) + '  ' + row[1] + '  ' + row[2]
        showData.insert(showData.size() + 1, addData)
    
    myDB.close()

def resetFields():
    enterId.delete(0, "end")
    enterName.delete(0, "end")
    enterDept.delete(0, "end")

window.mainloop()