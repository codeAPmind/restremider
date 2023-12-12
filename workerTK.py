import sys
import time
import datetime
from pynput import keyboard, mouse
from threading import Thread
from loguru import logger

import tkinter as tk
from tkinter import messagebox

# from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, 
#     QMessageBox, QGridLayout, QDialog,QApplication)

import os
os.environ['REQUESTS_CA_BUNDLE'] =  os.path.join(os.path.dirname(sys.argv[0]), 'cacert.pem')

import json
from common import readBinfile, getBios,writeBinfile
# import tkinter as tk
# from tkinter import messagebox
import schedule

from Message import showMsgInvolid, showMsg,showMsgIoginFisrt,showMsgGapFisrt, testnew
from login import LoginWindow
from license import getLicense
from PhoneNumber import encryption      
from common import load_json

import ctypes

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
                         

class LoginDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Login")
        self.geometry("100x100")
        self.configure(bg='black')  # Set the window background color here
        self.attributes('-alpha', 0.3)  # Set the window transparency here
        self.loginSecessed = False

        self.label0 = tk.Label(self, text="Name")
        self.label0.grid(row=0, column=0)

        self.edit0 = tk.Entry(self)
        self.edit0.grid(row=0, column=1)

        login_button = tk.Button(self, text="Enter", command=self.check_license)
        login_button.grid(row=1, column=0)

    def check_bios(self):
        bios_current = getBios()
        if os.path.exists("main.bin"):
            bios = readBinfile("main.bin")
            if bios_current in bios:
                 return True
            else:
                return False
        else:
            writeBinfile(bios_current, "main.bin")
            return True
        
    def check_license(self):
        saveLicense = getLicense()
        license = encryption(self.edit0.get())
        print("license", license)
        if  saveLicense  not in license:
            print ("license error===")
            # count_right = 
            messagebox.showwarning("License Error", "Invalid license")
            return
        else:
            if self.check_bios():
                global count_right
                count_right = True
                self.loginSecessed = True
                self.destroy()
            else:
                messagebox.showwarning("License Error", "Invalid Computer")
                return
            # self.accept()

class RestReminderWin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.keys = ''
        self.values = ''
        self.mouse_listener = None
        self.keyboard_listener = None
        self.login_window = None
        self.load_settings()
        self.initUI()
    
    def starttimer(self):
        self.flash()
        self.root.after(1000*5, self.starttimer) 
        
    def flash(self):
        # hwnd = self.root.winfo_id() 
        # print("flashing ",hwnd)
        self.state('zoomed') 
        ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), True )#ctypes.windll.kernel32.GetConsoleWindow()
        
    def load_settings(self):
        try:
            with open('settings.json', 'r') as f:
                settings = json.load(f)
                self.bg_color = settings['bg_color']
                self.alpha = settings['alpha']
                print("bg_color, alpha",self.bg_color,self.alpha)
        except FileNotFoundError:
            self.bg_color = 'black'
            self.alpha = 0.3

    def save_settings(self):
        with open('settings.json', 'w') as f:
            settings = {'bg_color': self.bg_color, 'alpha': self.alpha}
            json.dump(settings, f)

    def set_bg_color(self, color):
        self.bg_color = color
        self.config(bg=color)
        self.save_settings()

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.attributes('-alpha', alpha)
        self.save_settings()
        
        # messagebox.showinfo("Time for Rest", "No mouse or key operation in the last 1 minute.")
        #  QMessageBox.information(None, "No Operation", "No mouse or key operation in the last 1 minute.")
    def initUI(self):
        self.title("Main")
        # self.bg_color = "white"
        self.config(bg=self.bg_color)
        self.attributes('-alpha', self.alpha)

        # self.configure(bg='black')  # Set the window background color here
        # self.attributes('-alpha', 0.3)  # Set the window transparency here
        current_time = datetime.datetime.now()
        current_time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")

        self.label1 = tk.Label(self, text="工作时间(分钟)")
        self.label1.grid(row=0, column=0, pady=(5, 0))


        self.timeSet = tk.Entry(self, width=17)

        # self.edit1.grid(row=0, column=0,pady=(10, 0))  # Adjust the layout using grid
        self.timeSet.grid(row=1, column=0,pady=(10, 0)) 
        # self.edit1.delete(0, tk.END)  # Clear the current content
        # self.edit1.insert(0, self.values[:-2])  # Set the new content
        
        self.timeUpdate = tk.Entry(self, width=17)

        # self.edit1.grid(row=0, column=0,pady=(10, 0))  # Adjust the layout using grid
        self.timeUpdate.grid(row=4, column=0,pady=(10, 0)) 

        update_button = tk.Button(self, text="start work", command=self.start_work)
        update_button.grid(row=2, column=0,pady=(10, 0)) 
        
        login_button = tk.Button(self, text=" Login ", command=self.show_login_window)
        login_button.grid(row=3, column=0,pady=(10, 0)) 
        
    
    def press_test(self,key):
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
            self.flash()
            
    def click_test(self,x, y, button, pressed):
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
            self.timeUpdate.delete(0, tk.END)  # Clear the current content
            self.timeUpdate.insert(0, current_time_string)  # Set the new content
            self.flash()
            # try:
                # t1 = Thread(target=testnew)
                # t1 = Thread(target=self.flash)
                # t1.setDaemon(True)
                # t1.start()
            # except:
                # logger.debug("error, unable to start  showMsg")



                          
    def getGapTime(self):
        set = self.timeSet.get()
        # set = self.timeSet.text()/
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
    
            
            
    def start_work(self):
        # QMessageBox.warning(self, "License Error", "Invalid license")
        self.getGapTime()
        global timeGap
        if(timeGap < 0):
            return 
        global HasLog
        if HasLog == False:
            messagebox.showwarning("License Error", "Login first")
            return
        
            # try:
            #     t1 = Thread(target=showMsgIoginFisrt)
            #     t1.start()
            # except:
            #     logger.debug("error, unable to start  showMsg")
        
        if self.login_window.loginSecessed == False:
            messagebox.showwarning("License Error", "Login first")
            return
        
        self.keyboard_listener = keyboard.Listener(on_press=self.press_test)
        self.mouse_listener = mouse.Listener(on_click=self.click_test)
        self.keyboard_listener.start()
        self.mouse_listener.start()
        logger.debug("start listen")

                
    def show_login_window(self):
        global HasLog
        HasLog = True
        self.login_window = LoginDialog(self)
        self.login_window.grab_set()

        


    def closeEvent(self, event):
        print("closing stop ")
        if self.mouse_listener:
            print("closing stop ")
            self.mouse_listener.stop()
        if self.keyboard_listener:
            self.keyboard_listener.stop()
        event.accept()
        
        
if __name__ == '__main__':
    logger.add('worker.log') 
    # runScreensaver()
    app = RestReminderWin()
    app.mainloop()

    