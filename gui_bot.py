from tkinter import *

root= Tk()
root.title("Jorge o robô")
root.geometry('400x500')
root.configure(bg='#393e46')

def send_message():
    message = 'voce: ' + mensagemWindow.get('1.0', END)
    chatWindow.insert( END,"\n" + message)

chatWindow = Text(root, bd = 0, bg = '#222831', width = "50", height = "0", borderwidth = 0, fg = "#32e0c4")
chatWindow.place(x=15, y=15, height = 385, width = 370) 

mensagemWindow = Text(root, bd = 0, bg = '#222831', width = "50", height = "0", borderwidth = 0, fg = "#32e0c4")
mensagemWindow.place(x=120, y=420, height = 30, width = 260)

button = Button(root,command = send_message,  text = "enviar", bg = '#679b9b', activebackground = '#32e0c4', width = 12, height = 5, fg = '#222831', borderwidth=1, )
button.place(x = 15, y= 420, height = 30, width = 105)

scrollbar = Scrollbar(root, command  = chatWindow.yview())
scrollbar.place(x=375, y=15, height = 385)





root.mainloop()
