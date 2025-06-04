import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from toddo import Ui_MainWindow

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        # Your custom logic here
        # self.pushButton.clicked.connect(self.handle_button)
        # self.pushButton.clicked.connect(lambda: self.label.setText("Changed!"))

        self.tasks = ['Buy a Guitar','Eat Sushi', 'Call mom',]
        self.pushButton.clicked.connect(self.add_list)
        self.pushButton_2.clicked.connect(self.delete_all)
        self.pushButton_3.clicked.connect(self.delete)
        self.pushButton_4.clicked.connect(self.sort_asc)
        self.pushButton_5.clicked.connect(self.sort_desc)
        self.pushButton_6.clicked.connect(self.choose_random)
        self.pushButton_7.clicked.connect(self.number_of_tasks)
        self.pushButton_8.clicked.connect(self.exit)


    def Update_list(self):
        for i in self.tasks:
            self.listWidget.addItem(i)

    def add_list(self):
        self.listWidget.clear()
        self.Update_list()
        if self.lineEdit.text() != "":
         self.listWidget.addItem(self.lineEdit.text())
         self.tasks.append(self.lineEdit.text())
        self.label_2.setText(self.lineEdit.text())
        self.lineEdit.clear()
    def delete_all(self):
        self.listWidget.clear()
        self.label_2.setText("")
        self.tasks = []
    def delete(self):
        row = self.listWidget.currentRow()
        if row != -1:
            item_text = self.listWidget.item(row).text()
            self.listWidget.takeItem(row)
            if item_text in self.tasks:
                self.tasks.remove(item_text)
            self.label_2.setText("")
    def sort_asc(self):
        self.listWidget.clear()
        for task in self.tasks:
            task.split()
        self.tasks.sort(key=str.lower)
        self.Update_list()
    def sort_desc(self):
        self.listWidget.clear()
        self.tasks.sort(key=str.lower, reverse=True)
        self.Update_list()
    def choose_random(self):
        task = random.choice(self.tasks)
        self.label_2.setText(task)
    def number_of_tasks(self):
        self.label_2.setText(f'Number Of Tasks {len(self.tasks)}')
    def exit(self):
        window.close()




app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())

