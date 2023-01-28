from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                QLabel,QTextEdit, QListWidget, QLineEdit,
                QHBoxLayout, QVBoxLayout, QInputDialog)
app = QApplication([])
from notes_layout import *
import json

'''
notes = {
    "Каритан":{
        "текст" : "Є капітаном команди. Його мрія стати королем піратів і знайти Ван пис. Дуже ненажерливий, любить м'ясо. Любить повеселитися, часто веде себе як дитина, але в бою стає дуже серйозним.",
        "теги" : ["Текст","Сила","Мета"]
    },
    "Мечник":{
        "текст" : "Помічник капітана. Мріє стати найкращим мечником. Любить пити саке та спати. Він дуже суворий і серйозний. Терпіти не може Санджі (еро-кока, завитушку). ПОПЕРЕДЖЕННЯ: Страждає топографічним кретинізмом (часто втрачається навіть якщо йде прямою).",        
        "теги" : ["Текст","Ціна за голову","Мета"]
    },
    "Навігатор":{
        "текст" : "Навігатор, дуже любить мандарини та гроші. Хоче створити мапу світу. ПОПЕРЕДЖЕННЯ: Іноді може вдарити блискавкою, особливо коли злиться.",
        "теги" : ["Текст","Зріст","Мета"]
    },
    "Кананір":{
        "текст" : "Усопп снайпер команди Мугівар. Хоче стати хоробрим воїном моря, як його батько. Він часто бреше. Також він боягуз, але у критичних ситуаціях стає хоробрим.",
        "теги" : ["Текст","Батьки","Мета"]
    },
    "Кок":{
        "текст" : "Кок,любить курити, дівчат. Мріяв знайти Олл блю. Ніколи не вдарить дівчину (навіть якщо вона ворог). ПОПЕРЕДЖЕННЯ: може померти від втрати крові з носа, запальний, не переносить Зоро (Марімо).",
        "теги" : ["Текст","Хоббі","Мета"]
    },
    "Археолог":{
        "текст" : "Археолог. Ніко Робін хоче знайти все Ріо Понегліфи. Ніко Робіндуже спокійна та розумна, найчастіше вона читає книги. Дуже любить милих тварин. ПОПЕРЕДЖЕННЯ: У Робін іноді з'являються дивні думки і малюнки в голові.",
        "теги" : ["Текст","Зріст","Мета","Хоббі"]
    }

}
with open ("notes_data.json","w",encoding="utf-8") as file:
    json.dump(notes, file,sort_keys = True, ensure_ascii = False)
'''
with open ("notes_data.json","r",encoding = "utf-8") as file:
    notes = json.load(file)


window = QWidget()
window.resize(900,600)
window.setWindowTitle("розумниі замітки")
window.setLayout(hline)

def show_note():
    key = list_notes.selectedItems()[0].text()
    field_text.setText(notes[key]["текст"])
    list_tages.clear()
    list_tages.addItems(notes[key]["теги"])

def add_note():
    note_name, result = QInputDialog.getText(window,"Створити замітку","Назва замітки")
    if result == True and note_name != "":
        notes[note_name] = {"текст" : "","теги" : []}
        with open ("notes_data.json","w",encoding="utf-8") as file:
            json.dump(notes, file,sort_keys = True, ensure_ascii = False)
        list_notes.addItem(note_name)

def save_note():
    if list_notes.selectedItems():
        save_text = field_text.toPlainText()
        note_name = list_notes.selectedItems()[0].text()
        notes[note_name]["текст"] = save_text
        with open("note_datd.json","w",encoding = "utf-8") as file:
            json.dump(notes, file,sort_keys = True, ensure_ascii = False)
    else:
        print("Замітка не вибрана")

def del_note():
    if list_notes.selectedItems():
        note_name = list_notes.selectedItems()[0].text()
        del notes[note_name]
        with open("note_datd.json","w", encoding = "utf-8") as file:
            json.dump(notes, file,sort_keys = True, ensure_ascii = False)
        field_text.clear()
        list_tages.clear()
        list_notes.clear()
        list_notes.addItems(notes)
    else:
        print("Замітка не вибрана")
    
def add_tag():
    if list_notes.selectedItems() and field_tag.text() !="":
        note_name = list_notes.selectedItems()[0].text()
        tag_name = field_tag.text()
        if tag_name not in notes[note_name]["теги"]:
            notes[note_name]["теги"].append(tag_name)
            with open("notes_data.json","w",encoding = "utf-8") as file:
                json.dump(notes, file,sort_keys = True, ensure_ascii = False)
            list_tages.addItem(tag_name)

def del_tag():
    if list_notes.selectedItems() and list_tages.selectedItems():
        note_name = list_notes.selectedItems()[0].text()
        tag_name = list_tages.selectedItems()[0].text()
        notes[note_name]["теги"].remove(tag_name)
        with open("notes_data.json","w",encoding = "utf-8") as file:
            json.dump(notes, file,sort_keys = True, ensure_ascii = False)
        list_tages.clear()
        list_tages.addItems(notes[note_name]["теги"])

def search_tag():
    if field_tag.text() != "" and btn_tag_search.text() == "Шукати по тегу":
        tag = field_tag.text()
        filtred_tags = {}
        for note in notes:
            if tag in notes[note]["теги"]:
                filtred_tags[note] = notes[note]
        field_text.clear()
        list_tages.clear()
        list_notes.clear()
        list_notes.addItems(filtred_tags)
        btn_tag_search.setText("Скинути пошук")
    elif btn_tag_search.text() == "Скинути пошук":
        field_text.clear()
        list_tages.clear()
        list_notes.clear()
        list_notes.addItems(notes)
        btn_tag_search.setText("Шукати по тегу")


list_notes.addItems(notes)
list_notes.itemClicked.connect(show_note)

btn_note_new.clicked.connect(add_note)
btn_note_save.clicked.connect(save_note)
btn_note_del.clicked.connect(del_note)
btn_tag_add.clicked.connect(add_tag)
btn_tag_del.clicked.connect(del_tag)
btn_tag_search.clicked.connect(search_tag)


window.show()
app.exec_()