import tkinter
from tkinter import *
window = Tk()
window.title('bombit6')
window.geometry('960x720')

# Генерация ключа
import random
kit1 = list('1234567890')
kit2= list('ABCDEFGHIGKLMNOPQRSTUVWXYZ')

def key_generator():
    key1_parts = []
    for i in range(2):
        key1_parts.append(random.choice(kit1))
    for i in range(3):
        key1_parts.append(random.choice(kit2))
    random.shuffle(key1_parts)
    key1 = ''.join(key1_parts)
    key2_parts = []
    for i in range(2):
        key2_parts.append(random.choice(kit1))
    for i in range(3):
        key2_parts.append(random.choice(kit2))
    random.shuffle(key2_parts)
    key2 = ''.join(key2_parts)
    key3_parts = []
    for i in range(2):
        key3_parts.append(random.choice(kit1))
    for i in range(3):
        key3_parts.append(random.choice(kit2))
    random.shuffle(key3_parts)
    key3 = ''.join(key3_parts)
    return key1 + '-' + key2 + '-' + key3

def key_output():
    field_key.configure(text = key_generator(), font = ('Arial', 16))

# Добавление картинки на фон
Image = tkinter.PhotoImage(file = 'бомбит.png')
label_im = tkinter.Label(window, image = Image)
label_im.place(relx = 0, rely = 0)

frame = tkinter.Frame(window, background='#FFC0CB')
frame.place(relx= 0.5, rely = 0.5, anchor ='center')

field_key = tkinter.Label(frame, width= 20)
field_key.grid(column=1, row = 2, padx= 0, pady = 0)

enter_key = tkinter.Button(frame, text ='Сгенерировать ключ', font = ('Arial', 16),
                           command = key_output, bg = '#C71585')
enter_key.grid(column=20, row = 3)

window.mainloop()
