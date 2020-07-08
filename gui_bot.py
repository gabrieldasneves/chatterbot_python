from tkinter import *

root= Tk()
root.title("chat bot")
root.geometry('400x500')
root.configure(bg='#393e46')


chatWindow = Text(root, bd = 0, bg = '#222831', width = "50", height = "0", borderwidth = 0)
chatWindow.place(x=15, y=15, height = 385, width = 370) 

mensagemWindow = Text(root, bd = 0, bg = '#222831', width = "50", height = "0", borderwidth = 0)
mensagemWindow.place(x=120, y=415, height = 30, width = 260)

button = Button(root, text = "enviar", bg = '#679b9b', activebackground = '#32e0c4', width = 12, height = 5, fg = '#222831')
button.place(x = 15, y= 415, height = 30, width = 110)

scrollbar = Scrollbar(root, command  = chatWindow.yview())
scrollbar.place(x=375, y=15, height = 385)


root.mainloop()