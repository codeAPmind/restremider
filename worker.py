import sys
import time
import datetime
from pynput import keyboard, mouse
from threading import Thread
from loguru import logger

from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, 
    QMessageBox, QGridLayout, QDialog,QApplication)

import os
# os.environ['REQUESTS_CA_BUNDLE'] =  os.path.join(os.path.dirname(sys.argv[0]), 'cacert.pem')


# import tkinter as tk
# from tkinter import messagebox
import schedule

from Message import showMsgInvolid, showMsg,showMsgIoginFisrt,showMsgGapFisrt, testnew
from login import LoginWindow
from license import getLicense
from PhoneNumber import encryption      
from common import load_json

global mouse_start_time
mouse_start_time = time.time()

global key_start_time
key_start_time = time.time()

global mouse_elapsed_time 
mouse_elapsed_time = 0

global key_elapsed_time 
key_elapsed_time = 0

global firstshow
firstshow = False

global HasLog
HasLog = False

def getGaptime():
    data =  load_json("setting.json")
    i = 0
    for key, value in data.items():
        if "GapTime" in key:
            print("Gaptime vluae", value)
            return value
    return ""

global timeGap
timeGap = 0

# root = tk.Tk()
def on_press(key):
    global key_elapsed_time,mouse_elapsed_time,key_start_time
    key_elapsed_time += time.time() - key_start_time
    # print("press")
    print("time. time()", time.time())
    print("key start time", key_start_time)
    
    logger.debug(f'{key} :pushed') 
    print(" click",key_elapsed_time)
    # Rest of your code...
    global timeGap
    if key_elapsed_time > timeGap :
        mouse_elapsed_time = 0
        key_elapsed_time = 0
        logger.debug("mouse_elapsed_time,")
        key_start_time = time.time()
        try:
            t1 = Thread(target=testnew)
            t1.start()
        except:
            logger.debug("error, unable to start  showMsg")


def on_click(x, y, button, pressed):
    if pressed is  False:
        return
    global key_elapsed_time,mouse_elapsed_time,key_start_time
    elaped_time =  time.time() - key_start_time
    key_elapsed_time += elaped_time
    # print("press")
    print("time. time()", time.time())
    print("key start time", key_start_time)
    print(" click",key_elapsed_time)
    print("pressed",pressed)
    # Rest of your code...
    global timeGap
    if key_elapsed_time > timeGap :
        mouse_elapsed_time = 0
        key_elapsed_time = 0
        logger.debug("mouse_elapsed_time,")
        key_start_time = time.time()
        try:
            t1 = Thread(target=testnew)
            t1.setDaemon(True)
            t1.start()
        except:
            logger.debug("error, unable to start  showMsg")

def  check():
        while True:
            print("no working check")
            noworking()
            time.sleep(2)
                 
def noworking():
    global key_elapsed_time,mouse_elapsed_time,key_start_time
    global timeGap
    if key_elapsed_time > timeGap :
        # print("No mouse or key operation in the last 1 minute.")
        mouse_elapsed_time = 0
        key_elapsed_time = 0
        # print("new value" , key_elapsed_time)
        logger.debug("mouse_elapsed_time,")
        key_start_time = time.time()
        # root.withdraw()
        testnew()
        # try:
        #     t1 = Thread(target=showMsg)
        #     t1.start()
        # except:
        #     logger.debug("error, unable to start  showMsg")
                         
 
def showMsgES():
    app = QApplication(sys.argv)
    msgBox = QMessageBox()
    msgBox.setText("Time to rest." )
    msgBox.exec_()
    sys.exit(app.exec_())
    
class Example_Label(QWidget):
    def __init__(self):
        super().__init__()
        self.keys = ''
        self.values = ''
        self.mouse_listener = None
        self.keyboard_listener = None
        self.login_window = None
        self.initUI()
    
        # messagebox.showinfo("Time for Rest", "No mouse or key operation in the last 1 minute.")
        #  QMessageBox.information(None, "No Operation", "No mouse or key operation in the last 1 minute.")
    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        self.timeLable =QLabel("工作时间(分钟)")
        self.timeSet = QLineEdit()
        
        grid.addWidget( self.timeLable ,1,0)
        grid.addWidget(self.timeSet,2,0)
        self.timeSet.setFixedWidth(200)
        
        current_time = datetime.datetime.now()
        current_time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        self.editTime = QLineEdit()
        self.editTime.setText("update time"+current_time_string)

        grid.addWidget(self.editTime, 3 , 0)

        
        updateButton = QPushButton("Start")
        updateButton.clicked.connect(self.start)
        
        grid.addWidget(updateButton,4 , 0)
        
        login_button = QPushButton("Login", self)
        login_button.clicked.connect(self.show_login_window)
        grid.addWidget(login_button,5 , 0)
        
       # print(self.snow_data_stock('01810'))
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Review')    
        self.show()
        # showMsg()
    
    def set_test(self,x, y, button, pressed):
        if pressed is  False:
            return
        global key_elapsed_time,mouse_elapsed_time,key_start_time
        elaped_time =  time.time() - key_start_time
        key_elapsed_time += elaped_time
        # print("press")
        print("time. time()", time.time())
        print("key start time", key_start_time)
        print(" click",key_elapsed_time)
        print("pressed",pressed)
        # Rest of your code...
        global timeGap
        if key_elapsed_time > timeGap :
            mouse_elapsed_time = 0
            key_elapsed_time = 0
            logger.debug("mouse_elapsed_time,")
            key_start_time = time.time()
            current_time = datetime.datetime.now()
            current_time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
            # self.editTime = QLineEdit()
            newText = "set update time"+ current_time_string
            self.editTime.setText(f'<font color="red">{newText}</font>')

            try:
                t1 = Thread(target=testnew)
                t1.setDaemon(True)
                t1.start()
            except:
                logger.debug("error, unable to start  showMsg")



                          
    def getGapTime(self):
        set = self.timeSet.text()
        if len(set) <= 0:
            try:
                    t1 = Thread(target=showMsgGapFisrt)
                    t1.start()
            except:
                logger.debug("error, no set gap time")
                
            return False
        gap_time = float(set)
        global timeGap
        timeGap = gap_time * 6000
        logger.debug(f'{timeGap} :timegap') 
        # return True
    
            
            
    def start(self):
        # QMessageBox.warning(self, "License Error", "Invalid license")
        self.getGapTime()
        global timeGap
        if(timeGap < 0):
            return 
        # global HasLog
        # if HasLog == False:
        #     try:
        #         t1 = Thread(target=showMsgIoginFisrt)
        #         t1.start()
        #     except:
        #         logger.debug("error, unable to start  showMsg")
        #     return
        
        # if self.login_window.loginSecessed == False:
        #     try:
        #         t1 = Thread(target=showMsgInvolid)
        #         t1.start()
        #     except:
        #         logger.debug("error, unable to start  showMsg")
        #     return
        
        self.keyboard_listener = keyboard.Listener(on_press=on_press)
        self.mouse_listener = mouse.Listener(on_click=self.set_test)
        self.keyboard_listener.start()
        self.mouse_listener.start()
        logger.debug("start listen")

                
    def show_login_window(self):
        global HasLog
        HasLog = True
        self.login_window = LoginWindow()
        self.login_window.exec_()
        


    def closeEvent(self, event):
        print("closing stop ")
        if self.mouse_listener:
            print("closing stop ")
            self.mouse_listener.stop()
        if self.keyboard_listener:
            self.keyboard_listener.stop()
        event.accept()
        
import os, win32com.client
def runScreensaver():
    strComputer = "."
    objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
    colItems = objSWbemServices.ExecQuery("Select * from Win32_Desktop")
    for objItem in colItems:
        if objItem.ScreenSaverExecutable:
            os.system(objItem.ScreenSaverExecutable + " /start")
            break
        
if __name__ == '__main__':
    logger.add('worker.log') 
    # runScreensaver()
    app = QApplication(sys.argv)
    ex = Example_Label()
    sys.exit(app.exec_())

    