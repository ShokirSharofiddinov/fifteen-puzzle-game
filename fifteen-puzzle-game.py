import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
import random

class window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.start()
        
    def start(self):
        self.lay1 = QVBoxLayout()
        self.v_lay = QVBoxLayout()
        self.buttns_lay = QHBoxLayout()
        self.grid = QGridLayout()
        self.lst = []
        for i in range(15):
            a = random.randint(1,15)
            while str(a) in self.lst:
                a = random.randint(1,15)

            self.lst.append(str(a))
        
        b = random.randint(1,13)
        self.lst.insert(b,'')
        self.bb = int(b)+1

        

        exit_btn = QPushButton('EXIT')
        exit_btn.clicked.connect(self.exit_method)
        self.buttns_lay.addWidget(exit_btn)
        restart_btn = QPushButton('RESTART')
        restart_btn.clicked.connect(self.restart_method)
        self.buttns_lay.addWidget(restart_btn)


        self.btn1 = QPushButton(self.lst[0])
        self.btn2 = QPushButton(self.lst[1])
        self.btn3 = QPushButton(self.lst[2])
        self.btn4 = QPushButton(self.lst[3])
        self.btn5 = QPushButton(self.lst[4])
        self.btn6 = QPushButton(self.lst[5])
        self.btn7 = QPushButton(self.lst[6])
        self.btn8 = QPushButton(self.lst[7])
        self.btn9 = QPushButton(self.lst[8])
        self.btn10 = QPushButton(self.lst[9])
        self.btn11 = QPushButton(self.lst[10])
        self.btn12 = QPushButton(self.lst[11])
        self.btn13 = QPushButton(self.lst[12])
        self.btn14 = QPushButton(self.lst[13])
        self.btn15 = QPushButton(self.lst[14])
        self.btn16 = QPushButton(self.lst[15])

        self.lst = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9, self.btn10, self.btn11, self.btn12, self.btn13, self.btn14, self.btn15, self.btn16]

        index = 0
        for i in range(4):
            for j in range(4):
                self.grid.addWidget(self.lst[index],i,j)   
                self.lst[index].setFixedSize(95,70)
                index+=1

        self.v_lay.addLayout(self.grid)
        self.v_lay.addLayout(self.buttns_lay)
        self.setLayout(self.v_lay)

        self.btn1.clicked.connect(self.clicker1)
        self.btn2.clicked.connect(self.clicker2)
        self.btn3.clicked.connect(self.clicker3)
        self.btn4.clicked.connect(self.clicker4)
        self.btn5.clicked.connect(self.clicker5)
        self.btn6.clicked.connect(self.clicker6)
        self.btn7.clicked.connect(self.clicker7)
        self.btn8.clicked.connect(self.clicker8)
        self.btn9.clicked.connect(self.clicker9)
        self.btn10.clicked.connect(self.clicker10)
        self.btn11.clicked.connect(self.clicker11)
        self.btn12.clicked.connect(self.clicker12)
        self.btn13.clicked.connect(self.clicker13)
        self.btn14.clicked.connect(self.clicker14)
        self.btn15.clicked.connect(self.clicker15)
        self.btn16.clicked.connect(self.clicker16)

    def exit_method(self):
        exit(1)

    def restart_method(self):
        self.lst = []
        for i in range(15):
            a = random.randint(1,15)
            while str(a) in self.lst:
                a = random.randint(1,15)

            self.lst.append(str(a))
        
        b = random.randint(1,13)
        self.lst.insert(b,'')
        self.bb = int(b)+1


        self.btn1 = QPushButton(self.lst[0])
        self.btn2 = QPushButton(self.lst[1])
        self.btn3 = QPushButton(self.lst[2])
        self.btn4 = QPushButton(self.lst[3])
        self.btn5 = QPushButton(self.lst[4])
        self.btn6 = QPushButton(self.lst[5])
        self.btn7 = QPushButton(self.lst[6])
        self.btn8 = QPushButton(self.lst[7])
        self.btn9 = QPushButton(self.lst[8])
        self.btn10 = QPushButton(self.lst[9])
        self.btn11 = QPushButton(self.lst[10])
        self.btn12 = QPushButton(self.lst[11])
        self.btn13 = QPushButton(self.lst[12])
        self.btn14 = QPushButton(self.lst[13])
        self.btn15 = QPushButton(self.lst[14])
        self.btn16 = QPushButton(self.lst[15])

        self.lst = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9, self.btn10, self.btn11, self.btn12, self.btn13, self.btn14, self.btn15, self.btn16]

        index = 0
        for i in range(4):
            for j in range(4):
                self.grid.addWidget(self.lst[index],i,j)   
                self.lst[index].setFixedSize(95,70)
                index+=1

        self.btn1.clicked.connect(self.clicker1)
        self.btn2.clicked.connect(self.clicker2)
        self.btn3.clicked.connect(self.clicker3)
        self.btn4.clicked.connect(self.clicker4)
        self.btn5.clicked.connect(self.clicker5)
        self.btn6.clicked.connect(self.clicker6)
        self.btn7.clicked.connect(self.clicker7)
        self.btn8.clicked.connect(self.clicker8)
        self.btn9.clicked.connect(self.clicker9)
        self.btn10.clicked.connect(self.clicker10)
        self.btn11.clicked.connect(self.clicker11)
        self.btn12.clicked.connect(self.clicker12)
        self.btn13.clicked.connect(self.clicker13)
        self.btn14.clicked.connect(self.clicker14)
        self.btn15.clicked.connect(self.clicker15)
        self.btn16.clicked.connect(self.clicker16)



    def check_win(self):
        if self.btn1.text() == '1' and self.btn2.text() == '2' and self.btn3.text() == '3' and self.btn4.text() == '4' and self.btn6.text() == '6' and self.btn5.text() == '5' and self.btn7.text() == '7' and self.btn8.text() == '8' and self.btn9.text() == '9' and self.btn10.text() == '10' and self.btn11.text() == '11' and self.btn12.text() == '12' and self.btn13.text() == '13' and self.btn14.text() == '14' and self.btn15.text() == '15' and self.btn16.text() == '':
            self.btn1.hide()
            self.btn2.hide()
            self.btn3.hide()
            self.btn4.hide()
            self.btn5.hide()
            self.btn6.hide()
            self.btn7.hide()
            self.btn8.hide()
            self.btn9.hide()
            self.btn10.hide()
            self.btn11.hide()
            self.btn12.hide()
            self.btn13.hide()
            self.btn14.hide()
            self.btn15.hide()
            self.btn16.hide()


    def clicker1(self):
        if self.bb == 2 or self.bb == 5:
            if self.bb == 2: self.btn2.setText(self.btn1.text())
            elif self.bb == 5: self.btn5.setText(self.btn1.text())
            self.btn1.setText('')
            self.bb = 1
            self.check_win()

    def clicker2(self):
        if self.bb == 1 or self.bb == 3 or self.bb == 6:
            if self.bb == 1: self.btn1.setText(self.btn2.text())
            elif self.bb == 3: self.btn3.setText(self.btn2.text())
            elif self.bb == 6: self.btn6.setText(self.btn2.text())
            self.btn2.setText('')   
            self.bb = 2
            self.check_win()
        

    def clicker3(self):
        if self.bb == 2 or self.bb == 4 or self.bb == 7:
            if self.bb == 2: self.btn2.setText(self.btn3.text())
            elif self.bb == 4: self.btn4.setText(self.btn3.text())
            elif self.bb == 7: self.btn7.setText(self.btn3.text())
            self.btn3.setText('')
            self.bb = 3
            self.check_win()


    def clicker4(self):
        if self.bb == 3 or self.bb == 8:
            if self.bb == 3: self.btn3.setText(self.btn4.text())
            elif self.bb == 8: self.btn8.setText(self.btn4.text())
            self.btn4.setText('')
            self.bb = 4
            self.check_win()

    def clicker5(self):
        if self.bb == 1 or self.bb == 6 or self.bb == 9:
            if self.bb == 1: self.btn1.setText(self.btn5.text())
            elif self.bb == 6: self.btn6.setText(self.btn5.text())
            elif self.bb == 9: self.btn9.setText(self.btn5.text())
            self.btn5.setText('')
            self.bb = 5
            self.check_win()

    def clicker6(self):
        if self.bb == 2 or self.bb == 7 or self.bb == 5 or self.bb == 10:
            if self.bb == 2: self.btn2.setText(self.btn6.text())
            elif self.bb == 7: self.btn7.setText(self.btn6.text())
            elif self.bb == 5: self.btn5.setText(self.btn6.text())
            elif self.bb == 10: self.btn10.setText(self.btn6.text())
            self.btn6.setText('')   
            self.bb = 6
            self.check_win()

    def clicker7(self):
        if self.bb == 3 or self.bb == 6 or self.bb == 11 or self.bb == 8:
            if self.bb == 3: self.btn3.setText(self.btn7.text())
            elif self.bb == 6: self.btn6.setText(self.btn7.text())
            elif self.bb == 11: self.btn11.setText(self.btn7.text())
            elif self.bb == 8: self.btn8.setText(self.btn7.text())
            self.btn7.setText('')
            self.bb = 7
            self.check_win()

    def clicker8(self):
        if self.bb == 7 or self.bb == 4 or self.bb == 12:
            if self.bb == 7: self.btn7.setText(self.btn8.text())
            elif self.bb == 4: self.btn4.setText(self.btn8.text())
            elif self.bb == 12: self.btn12.setText(self.btn8.text())
            self.btn8.setText('')
            self.bb = 8
            self.check_win()

    def clicker9(self):
        if self.bb == 5 or self.bb == 10 or self.bb == 13:
            if self.bb == 5: self.btn5.setText(self.btn9.text())
            elif self.bb == 10: self.btn10.setText(self.btn9.text())
            elif self.bb == 13: self.btn13.setText(self.btn9.text())
            self.btn9.setText('')
            self.bb = 9
            self.check_win()

    def clicker10(self):
        if self.bb == 9 or self.bb == 6 or self.bb == 11 or self.bb == 14:
            if self.bb == 9: self.btn9.setText(self.btn10.text())
            elif self.bb == 6: self.btn6.setText(self.btn10.text())
            elif self.bb == 11: self.btn11.setText(self.btn10.text())
            elif self.bb == 14: self.btn14.setText(self.btn10.text())
            self.btn10.setText('')   
            self.bb = 10
            self.check_win()

    def clicker11(self):
        if self.bb == 10 or self.bb == 12 or self.bb == 7 or self.bb == 15:
            if self.bb == 10: self.btn10.setText(self.btn11.text())
            elif self.bb == 12: self.btn12.setText(self.btn11.text())
            elif self.bb == 7: self.btn7.setText(self.btn11.text())
            elif self.bb == 15: self.btn15.setText(self.btn11.text())
            self.btn11.setText('')
            self.bb = 11
            self.check_win()

    def clicker12(self):
        if self.bb == 8 or self.bb == 11 or self.bb == 16:
            if self.bb == 8: self.btn8.setText(self.btn12.text())
            elif self.bb == 11: self.btn11.setText(self.btn12.text())
            elif self.bb == 16: self.btn16.setText(self.btn12.text())
            self.btn12.setText('')
            self.bb = 12
            self.check_win()
    
    def clicker13(self):
        if self.bb == 9 or self.bb == 14:
            if self.bb == 9: self.btn9.setText(self.btn13.text())
            elif self.bb == 14: self.btn14.setText(self.btn13.text())
            self.btn13.setText('')
            self.bb = 13
            self.check_win()

    def clicker14(self):
        if self.bb == 13 or self.bb == 10 or self.bb == 15:
            if self.bb == 13: self.btn13.setText(self.btn14.text())
            elif self.bb == 10: self.btn10.setText(self.btn14.text())
            elif self.bb == 15: self.btn15.setText(self.btn14.text())
            self.btn14.setText('')   
            self.bb = 14
            self.check_win()

    def clicker15(self):
        if self.bb == 11 or self.bb == 14 or self.bb == 16:
            if self.bb == 11: self.btn11.setText(self.btn15.text())
            elif self.bb == 14: self.btn14.setText(self.btn15.text())
            elif self.bb == 16: self.btn16.setText(self.btn15.text())
            self.btn15.setText('')
            self.bb = 15
            self.check_win()

    def clicker16(self):
        if self.bb == 15 or self.bb == 12:
            if self.bb == 15: self.btn15.setText(self.btn16.text())
            elif self.bb == 12: self.btn12.setText(self.btn16.text())
            self.btn16.setText('')
            self.bb = 16
            self.check_win()


app = QApplication([])
oyna = window()
oyna.show()
app.exec_()




