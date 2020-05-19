from tkinter import Tk, Listbox, SINGLE, END
root = Tk()
listbox = Listbox(root,height=5,width=15,selectmode=SINGLE)
list_of_countries = ["Ukraine", "Moldova", "Poland"] * 3

for country in list_of_countries:
    listbox.insert(END, country)

listbox.pack()
root.mainloop()