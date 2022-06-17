from tkinter import *


def botReply():
    question = questionField.get()
    textarea.insert(END, "\n" + 'You: ' + question)
    questionField.delete(0, END)
    if questionField.get() == "hi" or questionField.get() == "hello":
        textarea.insert(END, "\n" + "Bot:Hi,Nice to meet you")
    elif questionField.get() == "how are you?":
        textarea.insert(END, "\n" + "Bot:Fine and you")
    elif questionField.get() == "fine":
        textarea.insert(END, "\n" + "Bot:Nice to hear")
    elif questionField.get() == "" or questionField.get() == "hello":
        textarea.insert(END, "\n" + "Bot:Hi,Nice to meet you")
    else:
        textarea.insert(END, "\n" + "sorry,we will meet next time")


root = Tk()
root.title('Chat Bot by kesa')
root.geometry('500x570+100+30')
root.config(bg='deep pink')

LogoPic = PhotoImage(file='pic.png')
LogoPicLabel = Label(root, image=LogoPic, bg='deep pink')
LogoPicLabel.pack()

centreFrame = Frame(root)
centreFrame.pack()

scrollbar = Scrollbar(centreFrame)
scrollbar.pack(side=RIGHT)

textarea = Text(centreFrame, font=('times new roman', 20, 'bold'), height=10, yscrollcommand=scrollbar.set
                , wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)

questionField = Entry(root, font=('verdona', 20, 'bold'))
questionField.pack(pady=15, fill=X)

askPic = PhotoImage(file='ask.png')

askButton = Button(root, image=askPic, command=botReply)
askButton.pack()
root.mainloop()
