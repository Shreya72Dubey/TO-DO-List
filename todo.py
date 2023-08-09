from tkinter import *
root=Tk()
root.geometry("644x444")
root.title("TO DO LIST")
root.minsize(800,300)
def AddTasks():
    content=userentry.get(1.0,END)
    listtask.insert(END,content)
    with open('task.txt',"a") as file:
        file.write(content)
        file.seek(0)
        file.close()
    userentry.delete(1.0,END)
def DeleteTasks():
    delete=listtask.curselection()
    look=listtask.get(delete)
    listtask.delete(delete)
    with open("task.txt","r") as f:
        nf=f.readlines()
    with open("task.txt","w") as f:
        for line in nf:
            if line.strip() not in look:
                f.write(line)
        f.truncate()


label=Label(root,text="Welcome to TO DO LIST",bg="cyan", padx=1000, pady=3,font=("TimesNewRoman",20,"bold"))
label.pack()

entervalue=Label(root,text="Enter Tasks",font=("TimesNewRoman",15),bg="black",fg="white")
entervalue.place(x=10,y=60)

userentry=Text(root,height=1,width=20)
userentry.place(x=10,y=106)

Button(text="Add Tasks",command=AddTasks,bg="cyan").place(x=10,y=150)

enteredtask=Label(root,text="List of Tasks",font=("TimesNewRoman",15),bg="black",fg="white")
enteredtask.place(x=500,y=60)

listtask=Listbox(root,width=30,height=10)
listtask.place(x=500,y=106)

Button(text="Delete Tasks",command=DeleteTasks,bg="cyan").place(x=500,y=290)

root.mainloop()