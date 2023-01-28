from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                QLabel,QTextEdit, QListWidget, QLineEdit,
                QHBoxLayout, QVBoxLayout)
#Створення віджетів
field_text = QTextEdit()
lb_list_notes = QLabel("Список заліток")
list_notes = QListWidget()
btn_note_new = QPushButton("Створити замітку")
btn_note_del = QPushButton("Видалити замітку")
btn_note_save = QPushButton("Зберегти замінку")

lb_list_tages = QLabel("Список тегів")
list_tages = QListWidget()
field_tag = QLineEdit()
field_tag.setPlaceholderText("Введіть тег")
btn_tag_add = QPushButton("Додати до заміток")
btn_tag_del = QPushButton("Відкріпити замітку")
btn_tag_search = QPushButton("Шукати по тегу")

#розташування віджетів
hline = QHBoxLayout()

vline_left = QVBoxLayout()
vline_left.addWidget(field_text)

vline_right = QVBoxLayout()
vline_right.addWidget(lb_list_notes)
vline_right.addWidget(list_notes)

small_hline1 = QHBoxLayout()
small_hline1.addWidget(btn_note_new)
small_hline1.addWidget(btn_note_del)
vline_right.addLayout(small_hline1)
vline_right.addWidget(btn_note_save)
vline_right.addWidget(lb_list_tages)
vline_right.addWidget(list_tages)
vline_right.addWidget(field_tag)

small_hline2 = QHBoxLayout()
small_hline2.addWidget(btn_tag_add)
small_hline2.addWidget(btn_tag_del)
vline_right.addLayout(small_hline2)
vline_right.addWidget(btn_tag_search)

hline.addLayout(vline_left,stretch = 2)
hline.addLayout(vline_right, stretch = 1)




