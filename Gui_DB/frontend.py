from tkinter import*
import backend

def show_all():
    list1.delete(0,END)
    for data in backend.view():
        list1.insert(END,data)

def search_entry():
    data = backend.search(title = title_txt.get(),author =author_txt.get(), year = year_txt.get(),isbn =isbn_txt.get())
    list1.delete(0,END)
    for row in data:
        list1.insert(END,row)

def add_entry():
    backend.insert(title = title_txt.get(),author =author_txt.get(), year = year_txt.get(),isbn =isbn_txt.get())
    list1.delete(0,END)
    list1.insert(END,(title_txt.get(),author_txt.get(), year_txt.get(),isbn_txt.get()))

def onselect(event):
    global selected
    index = int(list1.curselection()[0])
    selected = list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected[1])
    e2.delete(0,END)
    e2.insert(END,selected[2])    
    e3.delete(0,END)
    e3.insert(END,selected[3])
    e4.delete(0,END)
    e4.insert(END,selected[4])

def delete_entry():
    id = selected[0]
    backend.delete(id)
    show_all()

def update_entry():
    backend.update(selected[0],title_txt.get(),author_txt.get(),year_txt.get(),isbn_txt.get())    
    show_all()

window = Tk()

l1 = Label(window, text ="Title")
l1.grid(row =0, column =0)
l2 = Label(window, text ="Year")
l2.grid(row =1, column =0)
l3 = Label(window, text ="Author")
l3.grid(row =0, column =2)
l4 = Label(window, text ="ISBN")
l4.grid(row = 1, column =2)

title_txt = StringVar()
e1 =Entry(window,textvariable = title_txt)
e1.grid(row = 0, column=1)
year_txt = StringVar()
e2 =Entry(window,textvariable = year_txt)
e2.grid(row = 1, column=1)
author_txt = StringVar()
e3 =Entry(window,textvariable = author_txt)
e3.grid(row = 0, column=3)
isbn_txt = StringVar()
e4 =Entry(window,textvariable = isbn_txt)
e4.grid(row = 1, column=3)

list1 =Listbox(window,height =6, width=20)
list1.grid(row=2,column=0, rowspan=6, columnspan=3)
list1.bind('<<ListboxSelect>>', onselect)


scrl1 = Scrollbar(window)
scrl1.grid(row=2, column =2, rowspan=6)

list1.configure(yscrollcommand =scrl1.set)
scrl1.configure(command = list1.yview)

b1 = Button (window, text = "View All", width = 12, command=show_all)
b1.grid(row=2, column=3)
b2 = Button (window, text = "Search Entry", width = 12, command = search_entry)
b2.grid(row=3, column=3)
b3 = Button (window, text = "Add Entry", width = 12, command = add_entry)
b3.grid(row=4, column=3)
b4 = Button (window, text = "Update", width = 12, command = update_entry)
b4.grid(row=5, column=3)
b5 = Button (window, text = "Delete", width = 12, command = delete_entry)
b5.grid(row=6, column=3)
b6 = Button (window, text = "Close", width = 12,command = window.destroy)
b6.grid(row=7, column=3)

window.mainloop()