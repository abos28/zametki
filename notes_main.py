from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import json

notes = {
    "Добро пожаловать !": {
        "текст" : "всем привет, а мы поехали",
        "теги" : ["добро ","инструкция"]
    }
}
# with open ("notes_data.json", "w", encoding='UTF-8') as file:
#     json.dump(notes , file, ensure_ascii=False, indent=4)


app = QApplication([])
ui = uic.loadUi("zametki1.html")
ui.show()

def add_note():
    note_name, ok=QInputDialog.getText(ui,"Добавить заметку","Название заметки:")
    if ok and note_name != "":
        notes[note_name]={"текст":"","теги":[]}
        ui.list_notes.addItem(note_name)
        ui.list_tags.addItems(notes[note_name]["теги"])
        print(notes)

def save_note():
    if ui.list_notes.selectedItems():
        key = ui.list_notes.selectedItems()[0].text()
        notes[key]["текст"] = ui.field_text.toPlainText()
        with open ("notes_data.json", "w", encoding='UTF-8') as file:
          json.dump(notes , file, ensure_ascii=False, indent=4)
        print(notes)
    else:
        print("Заметки для сохранение не выбрана!")

def del_note():
  if ui.list_notes.selectedItems():
    key = ui.list_notes.selectedItems()[0].text()
    del notes[key]
    ui.list_notes.clear()
    ui.list_tags.clear()
    ui.field_text.clear()
    ui.list_notes.addItems(notes)
    with open ("notes_data.json", "w", encoding='UTF-8') as file:
       json.dump(notes , file, ensure_ascii=False, indent=4)
    print(notes)
  else:
        print("Заметки для удаление не выбрана!")


def show_note():
    key = ui.list_notes.selectedItems()[0].text()
    print(key)
    ui.field_text.setText(notes[key]["текст"])
    ui.list_tags.clear()
    ui.list_tags.addItems(notes[key]["теги"])

ui. list_notes.itemClicked.connect(show_note)

with open("notes_data.json","r", encoding='UTF-8') as file:
    notes = json.load(file)

ui.list_notes.addItems(notes)
ui.button_note_create.clicked.connect(add_note)
ui.button_note_save.clicked.connect(save_note)
ui.button_note_del.clicked.connect(del_note)

app.exec_()