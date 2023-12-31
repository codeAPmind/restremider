# from pynput import keyboard, mouse
from threading import Thread
import tkinter as tk
from tkinter import messagebox

import os,time,datetime,dataclasses,webbrowser
# os.environ['REQUESTS_CA_BUNDLE'] =  os.path.join(os.path.dirname(sys.argv[0]), 'cacert.pem')

from Message import showMsgGapFisrt
import simpleaudio as sa
from Settingpanel import SetDialog
from name import datfile,name,path
from keygen import query,permit,trial,key,sample,load,dump1,nt,dc,values
import setting

DEBUG =  False



class RestReminderWin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.keys = ''
        self.reminderTimes = 0
        self.isWork = False
        self.login_window = None
        self.work_id = None
        self.rest_id = None
        self.load_settings('settings.json')
        self.verify()
        self.initUI()
    
    def starttimer(self):
        self.flash()
        self.root.after(1000*5, self.starttimer) 
        
    def flash(self):
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
        self.geometry("420x230")
        self.attributes('-alpha', self.settings.alpha) 
        self.configure(bg=self.settings.bg_color)  

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        context_menu = tk.Menu(self, tearoff=0)
        context_menu.add_command(label="设置", command=self.show_set_window)
        context_menu.add_command(label="购买", command=lambda:webbrowser.open("https://item.taobao.com/item.htm?id=753192371704"))
        self.bind("<Button-3>", lambda event: context_menu.post(event.x_root, event.y_root))

        current_time = datetime.datetime.now()
        current_time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        self.timeUpdate = tk.Text(self, width=20, height=2) 

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
        self.isWork = False


    def enable_button_with_countdown(self, seconds_left):
        if seconds_left > 0:
            # self.update_button.config(state="disabled")
            self.update_button.config(text=f"休息时间 ({int(seconds_left/60)}分{seconds_left%60}秒)")
            self.rest_id = self.after(1000, lambda: self.enable_button_with_countdown(seconds_left - 1))
        else:
            # self.update_button.config(state="normal")
            self.reminderTimes += 1
            if "Trial" in self.edition:
                if self.reminderTimes >= 2:
                    self.update_button.config(text="开始工作")
                    messagebox.showwarning("Version Notes", "试用版连续提醒已超过限制，请手动再次开始或者购买升级")
                    return
            self.contiue_work()
            
    def cancel_work(self):
        if self.isWork:
            if self.work_id:
                self.after_cancel(self.work_id)  # Cancel the after event
                self.work_id = None  # Reset the after_id 
        else:
            if self.rest_id:
                self.after_cancel(self.rest_id)  # Cancel the after event
                self.rest_id = None  # Reset the after_id 

    def work_button(self,seconds_left):
        if seconds_left > 0:
            self.update_button.config(text=f"工作进行中 ({int(seconds_left/60)}分{seconds_left%60}秒)")
            self.work_id = self.after(1000, lambda: self.work_button(seconds_left - 1))
        else:
            self.set_reminder()
            self.arrow()
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
                pass
                # logger.debug("error, no set gap time")
            return False
    
    def arrow(self):
        f=path(self.settings.arrow_up if self.isWork else self.settings.arrow_down)
        self.iconphoto(False,tk.PhotoImage(file=f)) if f else None

    def set_work_msg(self):
        self.update_button.config(text="工作进行中")
        current_time = datetime.datetime.now()
        print("self.settings.workminutes",self.settings.workminutes) if DEBUG else None
        time_after_random_seconds = current_time + datetime.timedelta(seconds=int(self.settings.workminutes)*60)
        formatted_current_time = current_time.strftime("%H:%M:%S")
        formatted_time = time_after_random_seconds.strftime("%H:%M:%S") #%Y-%m-%d %H:%M:%S
        self.timeUpdate.delete('1.0', tk.END)  # Clear the current content
        self.timeUpdate.insert('1.0', f'开始工作时间: {formatted_current_time}  结束工作时间: {formatted_time}\n休息{self.settings.restminutes}分钟')  # Set the new content

    def on_closing(self):
        if any(i!=j for i,j in zip(values(self.settings),self.settings0)):
            if messagebox.askokcancel("Quit", "设置已修改，是否保存？"):
                dump1(dataclasses.asdict(self.settings),self.settingsfile)
        self.destroy()

    def contiue_work(self):
        self.cancel_work()
        self.check_Time()
        self.work_button(int(self.settings.workminutes)*60)
        self.set_work_msg()
        self.isWork = True
        self.arrow()

    def start_work(self):
        self.reminderTimes = 0
        self.contiue_work()
                    
        
if __name__ == '__main__':
    # logger.add('worker.log') 
    app = RestReminderWin()
    app.mainloop()

    