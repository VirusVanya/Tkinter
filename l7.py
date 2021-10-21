from tkinter import* 
window = Tk()  
window.title("Welcome to application PythonRu")  
window.geometry('400x250')
def setText():
    arr = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    s = text.get()
    bg = background.get()
    fg = fontColor.get()
    rezult['text'] = s
    rezult['bg'] = bg
    rezult['fg'] = fg
def clear():
    text.delete(0, END)
    fontColor.delete(0, END)
    background.delete(0, END)
    rezult['text'] = "Rezult"
    rezult['bg'] = "white"
    rezult['fg'] = "black"
rezult = Button(window, height=2, width=20, text="Rezult", fg="black", bg="white", activebackground="#a8a8a8")  
rezult.place(x=100, y=150)
lbl1 = Label(window, text="Text")
lbl1.place(x=50, y=12)
text = Entry(window, width=20)
text.place(x=142, y=10)
lbl2 = Label(window, text="Font color")
lbl2.place(x=50, y=42)
fontColor = Entry(window, width=20)
fontColor.place(x=142, y=40)
lbl3 = Label(window, text="Background")
lbl3.place(x=50, y=72)
background = Entry(window, width=20)
background.place(x=142, y=70)
btnSet = Button(window, height=1, width=10, text="Set", command=setText)
btnSet.place(x=80, y=105)
btnSet = Button(window, height=1, width=10, text="Clear", command=clear)
btnSet.place(x=200, y=105)
window.mainloop()