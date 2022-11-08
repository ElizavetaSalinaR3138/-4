import tkinter
from tkinter import *
window = Tk()
window.title('bombit6')
window.geometry('960x720')

# Генерация ключа
import random
kit1 = []
kit2 = []
kit_ = '1234567890'
for i in kit_:
    kit1.append(i)
kit_= 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'
for i in kit_:
    kit2.append(i)

def generator_key():
    key1_array = []
    for i in range(2):
        key1_array.append(random.choice(kit1))
    for i in range(3):
        key1_array.append(random.choice(kit2))
    random.shuffle(key1_array)
    key1 = ''
    for i in key1_array:
        key1 += i
    key2_array = []
    for i in range(2):
        key2_array.append(random.choice(kit1))
    for i in range(3):
        key2_array.append(random.choice(kit2))
    random.shuffle(key1_array)
    key2 = ''
    for i in key2_array:
        key2 += i
    key3_array = []
    for i in range(2):
        key3_array.append(random.choice(kit1))
    for i in range(3):
        key3_array.append(random.choice(kit2))
    random.shuffle(key1_array)
    key3 = ''
    for i in key3_array:
        key3 += i
    return key1 + '-' + key2 + '-' + key3

def gen_key():
    field_key.configure(text = generator_key(), font = ('Arial', 16))

# Добавление картинки на фон
Image = tkinter.PhotoImage(file = 'бомбит.png')
label_im = tkinter.Label(window, image = Image)
label_im.place(relx = 0, rely = 0)

frame = tkinter.Frame(window, background='#FFC0CB')
frame.place(relx= 0.5, rely = 0.5, anchor ='center')

field_key = tkinter.Label(frame, width= 20)
field_key.grid(column=1, row = 2, padx= 0, pady = 0)

enter_key = tkinter.Button(frame, text ='Сгенерировать ключ', font = ('Arial', 16), command = gen_key, bg = '#C71585')
enter_key.grid(column=20, row = 3)

window.mainloop()
