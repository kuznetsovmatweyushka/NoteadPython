from datetime import datetime as d
import json
import random
from random import randint
from tkinter import *
import tkinter.filedialog as fd
NOTEPAD = {}


def create_note():
    path = create_file()
    with open(path, '+w', encoding='utf-8') as f:
        json.dump(NOTEPAD, f, indent=3, ensure_ascii=False)


def notepad():
    title = str(title_tf.get(1.0, 2.0))
    body = str(body_tf.get(1.0, 2.0))
    note_id = list(range(1, 1001))
    random.shuffle(note_id)
    date = d.now().strftime("%Y-%m-%d %H:%M")
    note_id = randint(1, 1000)
    NOTEPAD[note_id] = {"Id": note_id,
                        "Date": date,
                        "Title": title,
                        "Body": body
                        }
    print(NOTEPAD)
    return NOTEPAD


def create_file():
    filetypes = (("json-файл", "*.json"),)
    file_name = fd.asksaveasfilename(
        filetypes=filetypes, defaultextension=json)
    notes = {}
    if file_name != "":
        with open(file_name, "+w") as file:
            file.write(str(notes))
    return file_name


def read_file():
    filetypes = (("json-файл", "*.json"),)
    file_name = fd.askopenfilename(filetypes=filetypes, defaultextension=json)
    with open(file_name, encoding='utf-8') as file:
        data = json.load(file)
    return data


def reader():
    data = read_file()
    title_lb = Label(
        frame,
        text="Заголовок заметки: "
    )
    title_lb.grid(row=3, column=1)
    title_tf = Text(
        frame, height=10, width=30,
    )
    title_tf.grid(row=3, column=2)
    title_tf.insert(END, data[id_tf.get()]["Title"])
    body_lb = Label(
        frame,
        text="Тело заметки: ",
    )
    body_lb.grid(row=4, column=1)
    body_tf = Text(
        frame, height=10, width=30,
    )
    body_tf.insert(END, data[id_tf.get()]["Body"])
    body_tf.grid(row=4, column=2, pady=5)

def show_id():
    data = read_file()
    for k,i in data.items():
        show_notes_id_tf.insert(END, k + "\n")



window = Tk()
window.title("Заметки")
window.geometry('1280x720')

frame = Frame(
    window,
    padx=2,
    pady=2)

frame.pack(expand=True)

title_lb = Label(
    frame,
    text="Заголовок заметки: "
)
title_lb.grid(row=3, column=1)

body_lb = Label(
    frame,
    text="Тело заметки: ",
)
body_lb.grid(row=4, column=1)

title_tf = Text(
    frame, height=10, width=30,
)
title_tf.grid(row=3, column=2)

body_tf = Text(
    frame, height=10, width=30,
)
body_tf.grid(row=4, column=2, pady=2)

show_notes_id_lb = Label(
    frame,
    text="Доступные ID: "
)
show_notes_id_lb.grid(row=3,column=3)
show_notes_id_tf = Text(
    frame, height=10, width=10,
)
show_notes_id_tf.grid(row=4, column=3)
id_lb = Label(
    frame,
    text="Введите ID заметки для чтения: "
)
id_lb.grid(row=6, column=3)
id_tf = Entry(
    frame,
)
id_tf.grid(row=7, column=3)

save_btn = Button(
    frame,
    text='Cохранить',
    command=create_note
)
save_btn.grid(row=5, column=2)

add_btn = Button(
    frame,
    text='Добавить заметку',
    command=notepad
)
add_btn.grid(row=6, column=2)

read_btn = Button(
    frame,
    text='Прочитать заметки',
    command=reader
)
read_btn.grid(row=7, column=2)
showid_btn = Button(
    frame,
    text='Доступные ID',
    command=show_id
)
showid_btn.grid(row=7, column=4)

window.mainloop()

