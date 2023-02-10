from tkinter import *
import tkinter.filedialog as fd
from random import randint
from datetime import datetime as d
import json
import os
import tkinter.messagebox as mb
import glob


def create_btn():
    note = {}
    title = note_title_text.get(1.0, END)
    body = body_text.get(1.0, END)
    note_id = randint(1, 1000)
    date = d.now().strftime("%m.%d.%Y %H:%M:%S")
    note = {"Id": note_id,
            "Date": date,
            "Title": title.strip(),
            "Body": body.strip()
            }
    filetypes = (("json-файл", "*.json"),)
    filename = fd.asksaveasfilename(
        filetypes=filetypes, defaultextension=json, initialdir='/Notes')
    try:
        with open(filename, '+w', encoding='utf-8') as f:
            json.dump(note, f, indent=3, ensure_ascii=False)
            msg = "Ваша заметка сохранена"
            mb.showinfo("Информация", msg)
            name_file_text.delete(0, END)
            note_title_text.delete(0.0, END)
            body_text.delete(0.0, END)
            show_notes()
    except FileNotFoundError:
        msg = "Сохранение отменено"
        mb.showinfo("Информация", msg)
    return note


def reformat():
    filename = 'Notes/' + name_file_text.get()
    with open(filename, 'r',  encoding='utf-8') as file:
        data = json.load(file)
    data['Date'] = d.now().strftime("%m.%d.%Y %H:%M:%S")
    data['Title'] = note_title_text.get(1.0, END).strip()
    data['Body'] = body_text.get(1.0, END).strip()
    with open(filename, '+w', encoding='utf-8') as f:
        json.dump(data, f, indent=3, ensure_ascii=False)
        msg = "Ваша заметка отредактирована"
        mb.showinfo("Информация", msg)
    name_file_text.delete(0, END)
    note_title_text.delete(1.0, END)
    body_text.delete(1.0, END)

def select():
    name_file_text.delete(0, END)
    select = notebox.curselection()
    selected_file = notebox.get(select[0])
    name_file_text.insert(END, selected_file)
    filename = 'Notes/' + name_file_text.get()
    with open(filename, 'r',  encoding='utf-8') as file:
        data = json.load(file)
    note_title_text.delete(1.0, END)
    body_text.delete(1.0, END)
    note_title_text.insert(END, data["Title"])
    body_text.insert(END, data["Body"])


def show_notes():
    notebox.delete(0, END)
    dirname = 'Notes'
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            notebox.insert(END, filename)


def delete_note():
    try:
        filename = 'Notes/' + name_file_text.get()
        os.remove(filename)
        msg = 'Заметка ' + f'{name_file_text.get()}' + ' удалена'
        mb.showinfo("Информация", msg)
        name_file_text.delete(0, END)
        note_title_text.delete(0.0, END)
        body_text.delete(0.0, END)
        show_notes()

    except FileNotFoundError:
        msg = 'Заметка ' + f'{name_file_text.get()}' + ' уже удалена'
        mb.showwarning("Ошибка", msg)


def sort_note():
    sorted_files = []
    notebox.delete(0, END)
    dir_name = 'Notes/'
    list_of_files = filter(os.path.isfile, glob.glob(dir_name + '*.json'))
    list_of_files = sorted(list_of_files, key=os.path.getmtime)
    for file_path in list_of_files:
        file = str(file_path)
        file = file.split('Notes\\').pop(1)
        sorted_files.append(file)
    for file in sorted_files:
        notebox.insert(END, file)
    msg = "Заметки отсортированы по дате"
    mb.showinfo("Информация", msg)


window = Tk()
window.title("NoteApp by MatveyKuznetsov")
window.geometry("600x550")

frame = Frame(window)
frame.grid(row=0, column=0)

note_title_frame = Frame(frame)
note_title_frame.grid(row=0, column=1)

note_title_label = Label(note_title_frame, text='Заголовок заметки')
note_title_label.grid(row=0, column=1, pady=5, padx=5)

note_title_text = Text(note_title_frame, height=5, width=50)
note_title_text.grid(row=1, column=1, pady=5, padx=5)


body_frame = Frame(frame)
body_frame.grid(row=1, column=1)

body_label = Label(body_frame, text='Тело заметки')
body_label.grid(row=0, column=1, pady=5, padx=5)

body_text = Text(body_frame, height=15, width=50)
body_text.grid(row=1, column=1, pady=5, padx=5)

button_frame = Frame(frame)
button_frame.grid(row=1, column=2)

list_notes_text = Label(button_frame, text='Список заметок')
list_notes_text.grid(row=7, column=0)

notebox = Listbox(button_frame)
notebox.grid(row=8, column=0)

select_btn = Button(button_frame, text='Выбрать', command=select)
select_btn.grid(row=9, column=0)

create_new_note_btn = Button(frame, text='Создать заметку', command=create_btn)
create_new_note_btn.grid(row=2, column=1)

reformat_note_btn = Button(
    frame, text='Редактировать заметку', command=reformat)
reformat_note_btn.grid(row=2, column=2)

name_file_text = Entry(button_frame)
name_file_text.grid(row=2, column=0, pady=5, padx=5)


delete_btn = Button(button_frame, text='Удалить заметку', command=delete_note)
delete_btn.grid(row=4, column=0, pady=5, padx=5)

sort_btn = Button(button_frame, text='Сортировать заметки', command=sort_note)
sort_btn.grid(row=5, column=0, pady=5, padx=5)

name_note_label = Label(button_frame, text="Название файла")
name_note_label.grid(row=1, column=0, padx=5, pady=5)


show_notes()
window.mainloop()
