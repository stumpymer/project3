from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QWidget, QTextEdit, QPushButton, QTableWidget,QTableWidgetItem
import sys
from library import*

app = QtWidgets.QApplication([])
win = uic.loadUi("студенты.ui")

Gr = Grup()
Gr.read_data_from_file("text.txt")

def btnLoadTable():
    win.tableWidget.setRowCount(Gr.count)
    row = 0
    for x in Gr.A:
        # Фамилия
        win.tableWidget.setItem(row, 0, QTableWidgetItem(Gr.A[x].fam))
        # Имя
        win.tableWidget.setItem(row, 1, QTableWidgetItem(Gr.A[x].name))
        # Отчество
        win.tableWidget.setItem(row, 2, QTableWidgetItem(Gr.A[x].otchestvo))
        # Номер
        win.tableWidget.setItem(row, 3, QTableWidgetItem(str(Gr.A[x].number)))
        # Дни
        win.tableWidget.setItem(row, 4, QTableWidgetItem(str(Gr.A[x].days)))
        # Деньги
        win.tableWidget.setItem(row, 5, QTableWidgetItem(str(Gr.A[x].moneys)))
        row += 1

def btnAppendPerson():
    
    List = [str(win.lineEdit_2.text()),str(win.lineEdit_3.text()),str(win.lineEdit_4.text()),\
            str(win.lineEdit_5.text()),str(win.lineEdit_6.text()),str(win.lineEdit_7.text())]
   
    Gr.appendPerson(List)
  
    win.tableWidget.clear()
    btnLoadTable()
   
 
def btnEditPerson():
  
    if win.lineEdit_8.text() == '' :
        win.lineEdit_8.setText('1')

    if win.lineEdit_9.text() == '':    
        win.lineEdit_9.setText('1')
    
    x = int(win.lineEdit_8.text())-1
    y = int(win.lineEdit_9.text())-1

    if x <= win.tableWidget.rowCount() and y <= win.tableWidget.columnCount(): 
         
        List = [str(win.tableWidget.item(x,0).text()),\
            str(win.tableWidget.item(x,1).text()),\
            str(win.tableWidget.item(x,2).text()),\
            str(win.tableWidget.item(x,3).text()),\
            str(win.tableWidget.item(x,4).text()),\
            str(win.tableWidget.item(x,5).text())]
   
        key = Gr.find_keyPerson(List)
         
        if key != -1 :

            win.tableWidget.setItem(x,y,QTableWidgetItem(str(win.lineEdit.text())))

            List = [str(win.tableWidget.item(x,0).text()),\
            str(win.tableWidget.item(x,1).text()),\
            str(win.tableWidget.item(x,2).text()),\
            str(win.tableWidget.item(x,3).text()),\
            str(win.tableWidget.item(x,4).text()),\
            str(win.tableWidget.item(x,5).text())]
             
            print(List)     
            Gr.editPerson( key,List ) 

def btnDelPerson():
    
    List = [str(win.lineEdit_2.text()),str(win.lineEdit_3.text()),str(win.lineEdit_4.text()),\
            str(win.lineEdit_5.text()),str(win.lineEdit_6.text()),str(win.lineEdit_7.text())]

    Gr.delPerson(List)
  
    win.tableWidget.clear()
    
    btnLoadTable()
  
win.pushButton.clicked.connect(btnLoadTable)
win.pushButton_3.clicked.connect(btnAppendPerson)
win.pushButton_4.clicked.connect(btnEditPerson)
win.pushButton_5.clicked.connect(btnDelPerson)       


win.show()
sys.exit(app.exec())

