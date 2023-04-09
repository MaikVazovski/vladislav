from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox 
# оформление окна
window = Tk()
window['bg'] = 'white'
window.title('Программа')
window.geometry('400x400')
# функция
def button_click():
    login = loginInput.get()
    password = passField.get()
    
    info = f'Данные : {str(login)}, {str(password)}'
    messagebox.showinfo(title='Название', message=info)
    
    # messagebox.showerror(title='', message='Error')

# # canvas (не знаю зачем)
canvas = Canvas(window, height=400, width=400, bg='magenta')
canvas.pack()
# frame
frame = Frame(window, bg='cyan')
frame.place(relx=0.150, rely=0.20, relwidth=0.7, relheight=0.7)
# combobox
combo = Combobox(frame)
combo['values'] = ([i for i in range(1, 101)])
combo.current(0)
combo.pack()
# label
label = Label(frame, text='привет', font=40)
label.pack()
# button
button = Button(frame, text='кнопка', command=button_click)
button.pack()

# entry
label = Label(frame, text='Введи ФИО', font=40)
label.pack()
loginInput = Entry(frame, bg='white', width=50 )
loginInput.focus()
loginInput.pack()

label = Label(frame, text='Введи пароль', font=40)
label.pack()
passField = Entry(frame, bg='white',width=50, show='*')
passField.pack()

window.mainloop()
