from pynput import keyboard, mouse
from threading import Thread
from loguru import logger
import tkinter as tk
from tkinter import messagebox

import sys,os,time,math,datetime,random,dataclasses
# os.environ['REQUESTS_CA_BUNDLE'] =  os.path.join(os.path.dirname(sys.argv[0]), 'cacert.pem')


from Message import showMsgGapFisrt
import simpleaudio as sa
from Settingpanel import SetDialog
from name import datfile,name,path
from keygen import query,permit,trial,key,sample,load,dump1,nt,dc,values
import setting

DEBUG =  True



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
            self.configure(bg=self.settings.bg_color)  
        
        if isUpdateSize:
            self.timeUpdate.config(font=(self.settings.text_font, int(self.settings.text_size)))
            self.update_button.config(font=(self.settings.text_font, int(self.settings.text_size)))
        
        
    def initUI(self):
        self.geometry("500x400")
        self.attributes('-alpha', self.settings.alpha) 
        self.configure(bg=self.settings.bg_color)  

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        context_menu = tk.Menu(self, tearoff=0)
        context_menu.add_command(label="设置", command=self.show_set_window)
        self.bind("<Button-3>", lambda event: context_menu.post(event.x_root, event.y_root))

        current_time = datetime.datetime.now()
        current_time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        self.timeUpdate = tk.Entry(self, width=17)

        self.timeUpdate.grid(row=1, column=0,sticky='nsew',pady=(10, 0)) 
        self.timeUpdate.config(font=(self.settings.text_font, int(self.settings.text_size)))

        self.update_button = tk.Button(self, text="开始工作", command=self.start_work)
        self.update_button.grid(row=0, column=0,sticky='nsew',pady=(10, 0)) 
        self.update_button.config(font=(self.settings.text_font, int(self.settings.text_size)))
        if isinstance(self.result,tuple) and not all(self.result):
            self.update_button.config(state="disabled")
            messagebox.showwarning("License Error", f"{', '.join(j for i,j in zip(self.result,('软件过期','硬件错误','程序错误','授权错误')) if not i)}, 联系微信号w809500586购买")


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
        self.flash()


    def enable_button_with_countdown(self, seconds_left):
        if seconds_left > 0:
            self.update_button.config(state="disabled")
            self.update_button.config(text=f"休息时间 ({int(seconds_left/60)}分{seconds_left%60}秒)")
            self.after(1000, lambda: self.enable_button_with_countdown(seconds_left - 1))
        else:
            self.update_button.config(state="normal")
            self.start_work()

    def work_button(self,seconds_left):
        if seconds_left > 0:
            self.update_button.config(text=f"工作进行中 ({int(seconds_left/60)}分{seconds_left%60}秒)")
            self.after(1000, lambda: self.work_button(seconds_left - 1))
        else:
            self.set_reminder()
            self.enable_button_with_countdown(int(self.settings.restminutes) * 60)

    def play_sound(self):
        if self.settings.sound_on:
            f=path(self.settings.sound_file)
            if f:
                wave_obj = sa.WaveObject.from_wave_file(f)
                play_obj = wave_obj.play()
                play_obj.wait_done()
                          
    def check_Time(self):
        set = self.settings.workminutes
        if set <= 0:
            try:
                t1 = Thread(target=showMsgGapFisrt)
                t1.start()
            except:
                logger.debug("error, no set gap time")
            return False
    

    def set_work_msg(self):
        self.update_button.config(text="工作进行中")
        current_time = datetime.datetime.now()
        print("self.settings.workminutes",self.settings.workminutes) if DEBUG else None
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
        self.check_Time()
        self.work_button(int(self.settings.workminutes)*60)
        self.set_work_msg()
                    
        
if __name__ == '__main__':
    logger.add('worker.log') 
    app = RestReminderWin()
    app.mainloop()

    