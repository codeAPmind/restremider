import time
import datetime
from pynput import keyboard, mouse
from threading import Thread
from loguru import logger
import tkinter as tk
from tkinter import messagebox

import sys,os,time,math,datetime,random,dataclasses
# os.environ['REQUESTS_CA_BUNDLE'] =  os.path.join(os.path.dirname(sys.argv[0]), 'cacert.pem')


from Message import showMsgGapFisrt

from LicenseCheck import check_license

from license import getLicense
      
from common import load_json

import ctypes
import simpleaudio as sa
from Settingpanel import SetDialog
from name import datfile,name,path
from keygen import query,permit,trial,key,sample,load,dump1,nt,dc,values
import setting

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


def getLicenseEX():
    data =  load_json("License.json")
    i = 0
    for key, value in data.items():
            return value
    return ""

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


                         


class RestReminderWin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.keys = ''
        self.values = ''
        self.mouse_listener = None
        self.keyboard_listener = None
        self.login_window = None
        self.load_settings('settings.json')
        self.verify()
        self.initUI()
    
    def starttimer(self):
        self.flash()
        self.root.after(1000*5, self.starttimer) 
        
    def flash(self):
        # hwnd = self.root.winfo_id() 
        # print("flashing ",hwnd)
        self.state('zoomed') 
        # ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), True )#ctypes.windll.kernel32.GetConsoleWindow()
        
    def verify(self):
        self.license=path(datfile())
        self.IsFreetrial = not self.license
        self.query=query(self.license) if self.license else query(permit()) if os.path.exists(permit()) else trial(permit(),key(sample()))
        self.key=self.query[0][0]
        self.result=self.query[0][-1]
        self.endTimeStr = self.query[0][1]
        for k,v in zip(self.key._fields,self.key):setattr(self,k,v)
        self.ver=f'{self.version}'
        self.endTimeStr2=datetime.datetime.strptime(self.endTimeStr,'%a %b %d %H:%M:%S %Y').strftime("%Y-%m-%d %H:%M:%S")
        self.title(f"{name()} {self.version} {self.edition} {int((self.time-time.time())/86400)} days. © {time.strftime('%Y')} 图正的小店")
        print("tile seting ")

    def load_settings(self,f):
        self.settingsfile=path(f)
        d=load(self.settingsfile) if self.settingsfile else dump1(setting.s(),f)
        self.settingsfile=self.settingsfile or f
        self.settings=dc(d)
        self.settings0=nt(d)
    

    def show_set_window(self):
        self.login_window = SetDialog(self)
        self.login_window.grab_set()
    
    def updateUI(self,isUpdateAlpha,isUpdatebg,isUpdateSize):
        if isUpdateAlpha:
            self.attributes('-alpha', self.settings.alpha)  
        
        if isUpdatebg:
            self.config(bg=self.settings.bg_color)
        
        if isUpdateSize:
            # self.label1.config(font=(self.settings.text_font, int(self.settings.text_size)))
        #     self.edit1.tag_configure("red_text", foreground="red")
        #     # self.edit1.config(font=(self.settings.text_font, int(self.settings.text_size)))
            # self.timeSet.config(font=(self.settings.text_font, int(self.settings.text_size)))
            self.timeUpdate.config(font=(self.settings.text_font, int(self.settings.text_size)))
            self.update_button.config(font=(self.settings.text_font, int(self.settings.text_size)))
        
        

        # messagebox.showinfo("Time for Rest", "No mouse or key operation in the last 1 minute.")
        #  QMessageBox.information(None, "No Operation", "No mouse or key operation in the last 1 minute.")
    def initUI(self):
        # self.title("Main")
        
        # self.title("Work-Rest Balance")
        self.geometry("500x400")
        # self.bg_color = "white"
        self.config(bg=self.settings.bg_color)
        self.attributes('-alpha', self.settings.alpha)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.grid_columnconfigure(0, weight=1)

        context_menu = tk.Menu(self, tearoff=0)
        context_menu.add_command(label="设置", command=self.show_set_window)
        self.bind("<Button-3>", lambda event: context_menu.post(event.x_root, event.y_root))



        # if check_license() is False:
        #     return

        # self.configure(bg='black')  # Set the window background color here
        # self.attributes('-alpha', 0.3)  # Set the window transparency here
        current_time = datetime.datetime.now()
        current_time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")

        # self.label1 = tk.Label(self, text="工作时间(分钟)")
        # self.label1.grid(row=0, column=0, sticky='nsew',pady=(5, 0))


        # self.timeSet = tk.Entry(self, width=17)

        # # self.edit1.grid(row=0, column=0,pady=(10, 0))  # Adjust the layout using grid
        # self.timeSet.grid(row=1, column=0,sticky='nsew',pady=(10, 0)) 
        # self.edit1.delete(0, tk.END)  # Clear the current content
        # self.edit1.insert(0, self.values[:-2])  # Set the new content
        
        self.timeUpdate = tk.Entry(self, width=17)

        # self.edit1.grid(row=0, column=0,pady=(10, 0))  # Adjust the layout using grid
        self.timeUpdate.grid(row=1, column=0,sticky='nsew',pady=(10, 0)) 

        self.update_button = tk.Button(self, text="start work", command=self.start_work)
        self.update_button.grid(row=0, column=0,sticky='nsew',pady=(10, 0)) 
        
        # login_button = tk.Button(self, text=" Login ", command=self.show_login_window)
        # login_button.grid(row=3, column=0,pady=(10, 0)) 

    def vibrate_window(self, magnitude, duration, steps):
        x, y = self.winfo_x(), self.winfo_y()
        for _ in range(steps):
            self.geometry(f"+{x + magnitude}+{y}")
            self.update_idletasks()
            self.geometry(f"+{x - magnitude}+{y}")
            self.update_idletasks()
        self.geometry(f"+{x}+{y}")

    def set_reminder(self):
        self.vibrate_window(5,300,100)
        try:
            t1 = Thread(target=self.play_sound)
            t1.start()
        except:
            pass
        self.set_work_rest_msg()
        self.flash()

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
            timeGap += int(self.settings.restminutes) * 6000
            print("time gap", timeGap)
            mouse_elapsed_time = 0
            key_elapsed_time = 0
            logger.debug("mouse_elapsed_time,")
            key_start_time = time.time()
            current_time = datetime.datetime.now()
            current_time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
            # self.editTime = QLineEdit()
            newText = "set update time"+ current_time_string
            self.timeUpdate.delete(0, tk.END)  # Clear the current content
            self.timeUpdate.insert(0, current_time_string)  
            self.set_reminder()

            
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
            timeGap += int(self.settings.restminutes)  * 6000
            print("time gap", timeGap)
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
            # self.flash()
            self.self.set_reminder()
            # try:
                # t1 = Thread(target=testnew)
                # t1 = Thread(target=self.flash)
                # t1.setDaemon(True)
                # t1.start()
            # except:
                # logger.debug("error, unable to start  showMsg")


    def play_sound(self):
        if self.settings.sound_on:
            f=path(self.settings.sound_file)
            if f:
                wave_obj = sa.WaveObject.from_wave_file(f)
                play_obj = wave_obj.play()
                play_obj.wait_done()
                          
    def getGapTime(self):
        set = self.settings.workminutes
        # set = self.timeSet.text()/
        if set <= 0:
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
    

    def set_work_rest_msg(self):
        current_time = datetime.datetime.now()
        print("self.settings.workminutes",self.settings.workminutes)
        time_after_random_seconds = current_time + datetime.timedelta(seconds=int(self.settings.workminutes)*60)
        formatted_current_time = current_time.strftime("%H:%M:%S")
        formatted_time = time_after_random_seconds.strftime("%H:%M:%S") #%Y-%m-%d %H:%M:%S
        self.timeUpdate.delete(0, tk.END)  # Clear the current content
        self.timeUpdate.insert(0, f'开始工作时间: {formatted_current_time}   结束工作时间: {formatted_time}   休息{self.settings.restminutes}分钟')  # Set the new content

    def on_closing(self):
        if any(i!=j for i,j in zip(values(self.settings),self.settings0)):
            if messagebox.askokcancel("Quit", "设置已修改，是否保存？"):
                dump1(dataclasses.asdict(self.settings),self.settingsfile)
        self.destroy()

    def start_work(self):
        # QMessageBox.warning(self, "License Error", "Invalid license")
        self.getGapTime()
        global timeGap
        if(timeGap < 0):
            return 

        self.keyboard_listener = keyboard.Listener(on_press=self.press_test)
        self.mouse_listener = mouse.Listener(on_click=self.click_test)
        self.keyboard_listener.start()
        self.mouse_listener.start()
        logger.debug("start listen")

        self.set_work_rest_msg()
        # current_time = datetime.datetime.now()
        # time_after_random_seconds = current_time + datetime.timedelta(seconds=int(self.settings.workminutes)*60)
        # formatted_current_time = current_time.strftime("%H:%M:%S")
        # formatted_time = time_after_random_seconds.strftime("%H:%M:%S") #%Y-%m-%d %H:%M:%S
        # self.timeUpdate.delete(0, tk.END)  # Clear the current content
        # self.timeUpdate.insert(0, f'开始工作时间: {formatted_current_time}   结束工作时间: {formatted_time}   休息{self.settings.restminutes}分钟')  # Set the new content
        
        # self.timeUpdate.insert('1.0',f'开始工作时间: {formatted_current_time}        下次休息时间: {formatted_time}')
                
    def show_login_window(self):
        pass
        global HasLog
        HasLog = True
        # self.login_window = LoginDialog(self)
        # self.login_window.grab_set()

        


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

    