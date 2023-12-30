import json

import tkinter as tk
from tkinter import messagebox

import os
# os.environ['REQUESTS_CA_BUNDLE'] =  os.path.join(os.path.dirname(sys.argv[0]), 'cacert.pem')

# from common import Hardware
# from .. import wmihelp
from wmihelp import get_bios

class LoginDialog(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Info")
        self.geometry("500x100")
        self.configure(bg='white')  # Set the window background color here
        self.attributes('-alpha', 1.0)  # Set the window transparency here

        self.label0 = tk.Label(self, text="localinfo")
        self.label0.grid(row=0, column=0)

        self.edit0 = tk.Entry(self,width=80)
        self.edit0.grid(row=0, column=1)
        self.generate_license()

        # login_button = tk.Button(self, text="Enter", command=self.check_license)
        # login_button.grid(row=1, column=0)
    def  generate_license(self):
        key = ""
        # key += Hardware.get_cpu_sn()
        # key += Hardware.get_baseboard_sn()
        # key += Hardware.get_bios_sn()
        key = get_bios()
        
        # print("CPU序列号：{}".format(Hardware.get_cpu_sn()))
        # print("主板序列号：{}".format(Hardware.get_baseboard_sn()))
        # print("Bios序列号：{}".format(Hardware.get_bios_sn()))
        self.edit0.delete(0, tk.END)  # Clear the current content
        self.edit0.insert(0, key)  # Set the new content

if __name__ == "__main__":
    app = LoginDialog()
    app.mainloop()   