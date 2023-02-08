from datetime import datetime as d
import json

PATH_FILE = "C:/Users/ukeuk/Desktop/Note/note.json"


def create_notepad():
    name = input("Введите название файла: ")
    name = name + '.json'
    path = input("Укажите путь к файлу: ")
    notepad = {}
    with open(path + "/"+ name,'+w') as f:
        f.write(json.dumps(notepad, ensure_ascii=False))
        print('Файл создан!')
    return path + "/"+ name

def read_json(path):
    with open(path) as f:
        templates = json.load(f)
    return dict(templates)

def add_new_note(path):
    notes = read_json(path)
    title = input("Введите заголовок: ")
    body = input("Введите тело заметки: ")
    date = d.now().strftime("%Y-%m-%d %H:%M")
    notes[title] = [str(date), body]
    notes.update(notes)
    with open(path,'+w') as f:
        f.write(json.dumps(notes, ensure_ascii=False))
        print('Запись сделана!')

add_new_note(create_notepad())
# create_notepad()