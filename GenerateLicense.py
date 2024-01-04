from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, 
    QComboBox, QGridLayout, QApplication)

import json

from common import  load_json
import os
#os.environ['REQUESTS_CA_BUNDLE'] =  os.path.join(os.path.dirname(sys.argv[0]), 'cacert.pem')

# from keygen import Generate_key
from GeneratKey import generate_key

import time

import sys

# from ConstValue import ENDTIME,PHONENUM,BIOS
from ClientInfo import Client



            
class Example_Label(QWidget):
    def __init__(self):
        super().__init__()
        self.keys = ''
        self.values = ''
        self.clientinfo = Client()
        self.ver = ""
        self.initUI()

    def getLicense(self):
        data =  load_json("WRBalance.json")
        i = 0
        for key, value in data.items():
            if "License" in key:
                print("new vluae", value)
                return value
        return ""

    def save_settings(self):
        settings={'time': int(self.EndtimeEdit.text()),'pc': self.editBios.text(),'app': self.editApp.text(),'version':float(self.editversion.text()),'edition':self.editedition.text(),'mobile':int(self.editphoneNum.text()),'MINUTESGAP':int(self.editMINUTESGAP.text()),'STOCKNUM':int(self.editSTOCKNUM.text()),'STOCKNUM2':int(self.editSTOCKNUM2.text())}
        with open(self.edit0.text(), 'w') as f:
            json.dump(settings, f)

    
    
    def SetLicense_sign(self):
        from datetime import datetime, timedelta
        fileName = self.edit0.text()
        generaName = self.GenrerateLicEdit.text()
        bios = self.editBios.text()

        generate_key(generaName,fileName)
        print("0000000000000",generaName,fileName)

        
    def onDropdownSelection(self,text):
        self.ver = text

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        i = 0
        self.lable0 =QLabel("LIcenseFile")
        self.edit0 = QLineEdit()
        self.edit0.setText("WRBalance.json")
        
        
        grid.addWidget(self.lable0 ,i+1,0)
        grid.addWidget(self.edit0,i+2,0)
        self.edit0.setFixedWidth(200)
        
        
        self.lableversion =QLabel("version")
        self.editversion = QLineEdit()
        self.editversion.setText(str(self.clientinfo.version))
        
        grid.addWidget( self.lableversion ,i+3,0)
        grid.addWidget(self.editversion,i+4,0)
        self.editversion.setFixedWidth(200)
        
        self.lableedition =QLabel("edition")
        self.editedition = QLineEdit()
        self.editedition.setText(str(self.clientinfo.edition))
        
        grid.addWidget( self.lableedition ,i+5,0)
        grid.addWidget(self.editedition,i+6,0)
        self.editedition.setFixedWidth(200)
        
        # self.dropdown = QComboBox(self)
        # self.dropdown.addItem("Trail")
        # self.dropdown.addItem("1.0")
        # self.dropdown.addItem("Pro")
        # self.dropdown.addItem("Max")
        # # Add the dropdown to the grid
        # grid.addWidget(self.dropdown, i+3, 0)  # Adjust the row and column as per your layout

        # # Connect a function to handle dropdown selection change
        # self.dropdown.activated[str].connect(self.onDropdownSelection)

        self.GenrerateLicLable=QLabel("Genrerate LicenseFile")
        self.GenrerateLicEdit = QLineEdit()
        self.GenrerateLicEdit.setText("WRBalance.dat")
        grid.addWidget( self.GenrerateLicLable ,i+7,0)
        grid.addWidget(self.GenrerateLicEdit,i+8,0)

        self.lableEndtime =QLabel("Days")
        self.EndtimeEdit = QLineEdit()
        self.EndtimeEdit.setText(str(self.clientinfo.get_endTime()))
        grid.addWidget( self.lableEndtime ,i+9,0)
        grid.addWidget(self.EndtimeEdit,i+10,0)
        self.EndtimeEdit.setFixedWidth(200)
        
        
        self.lableBios =QLabel("BIOS")
        self.editBios = QLineEdit()
        self.editBios.setText(str(self.clientinfo.get_bios()))
        grid.addWidget( self.lableBios ,i+11,0)
        grid.addWidget(self.editBios,i+12,0)
        self.editBios.setFixedWidth(400)
        
        
        self.lableMINUTESGAP =QLabel("MINUTESGAP")
        self.editMINUTESGAP = QLineEdit()
        self.editMINUTESGAP.setText(str(self.clientinfo.MINUTESGAP))
        grid.addWidget( self.lableMINUTESGAP ,i+13,0)
        grid.addWidget(self.editMINUTESGAP,i+14,0)
        self.editBios.setFixedWidth(400)
        
        self.lableSTOCKNUM =QLabel("STOCKNUM")
        self.editSTOCKNUM = QLineEdit()
        self.editSTOCKNUM.setText(str(self.clientinfo.STOCKNUM))
        grid.addWidget( self.lableSTOCKNUM ,i+15,0)
        grid.addWidget(self.editSTOCKNUM,i+16,0)
        self.editSTOCKNUM.setFixedWidth(400)
        
        self.lableSTOCKNUM2 =QLabel("STOCKNUM2")
        self.editSTOCKNUM2 = QLineEdit()
        self.editSTOCKNUM2.setText(str(self.clientinfo.STOCKNUM2))
        grid.addWidget( self.lableSTOCKNUM2 ,i+17,0)
        grid.addWidget(self.editSTOCKNUM2,i+18,0)
        self.editSTOCKNUM2.setFixedWidth(400)
        
        
        self.lableApp =QLabel("App")
        self.editApp = QLineEdit()
        self.editApp.setText(str(self.clientinfo.app))
        grid.addWidget( self.lableApp ,i+19,0)
        grid.addWidget(self.editApp,i+20,0)
        self.editApp.setFixedWidth(400)
        
        
        self.lablephoneNum =QLabel("phoneNum")
        self.editphoneNum = QLineEdit()
        self.editphoneNum.setText(str(self.clientinfo.phoneNum))
        grid.addWidget( self.lablephoneNum ,i+21,0)
        grid.addWidget(self.editphoneNum,i+22,0)
        self.editphoneNum.setFixedWidth(400)
        
        saveButton = QPushButton("save License json")
        saveButton.clicked.connect(self.save_settings)
        
        grid.addWidget(saveButton,i+23, 0)
        
        setButton = QPushButton("Ganerate License")
        setButton.clicked.connect(self.SetLicense_sign)
        
        grid.addWidget(setButton,i+24, 0)
        
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')    
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example_Label()
    sys.exit(app.exec_())
    

