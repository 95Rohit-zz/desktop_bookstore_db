from tkinter import *
import backend
window = Tk()

window.wm_title("BookStore Manager")
def view_c():
    l1.delete(0,END)
    store =backend.view()
    for i in store:
        l1.insert(END,i)

def search_c():
    l1.delete(0,END)
    store = backend.Search(e1_v.get(),e2_v.get(),e3_v.get(),e4_v.get())
    for i in store:
        l1.insert(END,i)

def add_c():
    backend.Add(e1_v.get(),e2_v.get(),e3_v.get(),e4_v.get())
    l1.delete(0,END)
    l1.insert(END,(e1_v.get(),e2_v.get(),e3_v.get(),e4_v.get()))

def cool(event):
    global q
    index = l1.curselection()
    q = l1.get(index)
    e1.delete(0,END)
    e1.insert(END,q[1])
    e2.delete(0,END)
    e2.insert(END,q[2])
    e3.delete(0,END)
    e3.insert(END,q[3])
    e4.delete(0,END)
    e4.insert(END,q[4])

def delete_c():
    backend.Delete(q[0])

def update_c():
    backend.Update(q[0],e1_v.get(),e2_v.get(),e3_v.get(),e4_v.get())
    l1.delete(0,END)

l1 = Label(window,text="Title")
l1.grid(row =0,column = 0)

l2 = Label(window,text="Author")
l2.grid(row =0,column = 2)

l3 = Label(window,text="Year")
l3.grid(row =1,column = 0)

l4 = Label(window,text="ISBN")
l4.grid(row =1,column = 2)

e1_v =StringVar()
e1 = Entry(window,textvariable=e1_v)
e1.grid(row =0,column = 1)

e2_v =StringVar()
e2 = Entry(window,textvariable=e2_v)
e2.grid(row =0,column = 3)

e3_v =StringVar()
e3 = Entry(window,textvariable=e3_v)
e3.grid(row =1,column = 1)

e4_v =StringVar()
e4 = Entry(window,textvariable=e4_v)
e4.grid(row =1,column = 3)

l1 = Listbox(window, height=6,width=30)
l1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb = Scrollbar(window)
sb.grid(row=4,column=2,rowspan =2)

l1.configure(yscrollcommand=sb.set)
sb.configure(command=l1.yview)

l1.bind('<<ListboxSelect>>', cool)

b1 = Button(window,text="View",height=1,width=10, command=view_c)
b1.grid(row =2 ,column =3)

b2 = Button(window,text="Search Entry",height=1,width=10, command = search_c)
b2.grid(row =3 ,column =3)

b3 = Button(window,text="Add Entry",height=1,width=10, command = add_c)
b3.grid(row =4 ,column =3)

b4 = Button(window,text="Update Selected",height=1,width=10, command = update_c)
b4.grid(row =5 ,column =3)

b5 = Button(window,text="Delete Selected",height=1,width=10, command = delete_c)
b5.grid(row =6 ,column =3)

b6 = Button(window,text="Close",height=1,width=10, command = window.destroy)
b6.grid(row =7 ,column =3)
window.mainloop()
