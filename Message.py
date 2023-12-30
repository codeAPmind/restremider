
import tkinter as tk
from tkinter import messagebox

import ctypes
global firstshow
firstshow = False


def testnew():
    ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), True )
    root = tk.Tk()
    root.geometry("130x100") 
    # root.state('zoomed') 
    root.grab_set() #test
    
    var = tk.StringVar()
    var.set("小小妞妞,\n很少烦恼,\n无忧无虑乐陶陶.\n")
    message = tk.Message(root, bg="lightyellow", textvariable=var, font="times 12 italic",width=500)
    message.pack(padx=10, pady=10)
    root.lift()
    root.mainloop()

def showMsg():
        root = tk.Tk()
        root.withdraw()  # Hide the Tkinter root window
        print("show msg in")
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to close the message box?"):
                root.destroy()
        root.protocol("WM_DELETE_WINDOW", on_closing)
        global firstshow
        print("show msg in"+str(firstshow))
        # if(firstshow != False):
        messagebox.showinfo("Message", "Time to rest.")
        # firstshow = True
        print("show msg out")
        root.mainloop()
        

def showMsgInvolid():
        root = tk.Tk()
        root.withdraw()  # Hide the Tkinter root window
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to close the message box?"):
                root.destroy()
        root.protocol("WM_DELETE_WINDOW", on_closing)
        global firstshow
        if(firstshow != False):
            messagebox.showinfo("Message", "Involid Count.")
        firstshow = True
        root.mainloop()
    
def showMsgIoginFisrt():
        root = tk.Tk()
        root.withdraw()  # Hide the Tkinter root window
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to close the message box?"):
                root.destroy()
        root.protocol("WM_DELETE_WINDOW", on_closing)
        global firstshow
        if(firstshow != False):
            messagebox.showinfo("Message", "Login First.")
        firstshow = True
        root.mainloop()
        

def showMsgGapFisrt():
        root = tk.Tk()
        root.withdraw()  # Hide the Tkinter root window
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to close the message box?"):
                root.destroy()
        root.protocol("WM_DELETE_WINDOW", on_closing)
        global firstshow
        if(firstshow != False):
            messagebox.showinfo("Message", "时间设置错误, 请填入正确时间 .")
        firstshow = True
        root.mainloop()
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

        
def showMsg(msg):
    app = QApplication(sys.argv)
    msgBox = QMessageBox()
    msgBox.setText("Time to rest." + msg)
    msgBox.exec_()
    sys.exit(app.exec_())
'''
if __name__ == '__main__':
    testnew()
