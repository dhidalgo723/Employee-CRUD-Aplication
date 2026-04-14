from tkinter import *

window = Tk()
window.geometry("600x270")
window.title("Employee CRUD App")
window.mainloop()

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

getBtn = Button(window, text="Get", font=("Seriff", 12), bg="white", command=getData)
getBtn.place(x=150, y=160)

deleteBtn = Button(window, text="Delete", font=("Seriff", 12), bg="white", command=deleteData)
deleteBtn.place(x=210, y=160)

resetBtn = Button(window, text="Reset", font=("Seriff", 12), bg="white", command=resetFields)
resetBtn.place(x=20, y=210)

showData = Listbox(window)
showData.place(x=330, y=30)