import tkinter as tk 
from tkinter import OptionMenu

class SetDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("设置")
        self.geometry("400x300")
                # Get the size of the parent window
        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()
        
        # Get the screen coordinates of the parent window
        parent_x = parent.winfo_rootx()
        parent_y = parent.winfo_rooty()
        
        # Calculate the coordinates to center the dialog
        center_x = int(parent_x + (parent_width - 400) / 2)
        center_y = int(parent_y + (parent_height - 300) / 2)
        
        # Set the position of the window to the center of the parent
        self.geometry(f"+{center_x}+{center_y}")
        
        self.attributes('-alpha', self.parent.settings.alpha) 
        self.configure(bg=self.parent.settings.bg_color)  
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)  # This will allow edit_alpha to resize

        self.label_work = tk.Label(self, text="工作时间(分钟)",font=(self.parent.settings.text_font, int(self.parent.settings.text_size)))
        self.label_work.grid(row=0, column=0,  sticky='nsew',pady=(10, 0))
       

        self.edit_work = tk.Entry(self)
        self.edit_work.insert(0, str(self.parent.settings.workminutes))
        self.edit_work.grid(row=0, column=1,  sticky='nsew',pady=(10, 0))
        self.edit_work.config(font=(self.parent.settings.text_font, int(self.parent.settings.text_size)))

        self.label_reset = tk.Label(self, text="休息时间(分钟)",font=(self.parent.settings.text_font, int(self.parent.settings.text_size)))
        self.label_reset.grid(row=1, column=0,  sticky='nsew',pady=(10, 0))
       

        self.edit_reset = tk.Entry(self)
        self.edit_reset.insert(0, str(self.parent.settings.restminutes))
        self.edit_reset.grid(row=1, column=1,  sticky='nsew',pady=(10, 0))
        self.edit_reset.config(font=(self.parent.settings.text_font, int(self.parent.settings.text_size)))

        # Set the window background color here
        self.label_alpha = tk.Label(self, text="透明度(0.0~1.0)",font=(self.parent.settings.text_font, int(self.parent.settings.text_size)))
        self.label_alpha.grid(row=2, column=0,  sticky='nsew',pady=(10, 0))
       

        self.edit_alpha = tk.Entry(self)
        self.edit_alpha.insert(0, str(self.parent.settings.alpha))
        self.edit_alpha.grid(row=2, column=1,  sticky='nsew',pady=(10, 0))
        self.edit_alpha.config(font=(self.parent.settings.text_font, int(self.parent.settings.text_size)))
        
        self.label_color = tk.Label(self, text="背景颜色",font=(self.parent.settings.text_font, int(self.parent.settings.text_size)))
        self.label_color.grid(row=3, column=0,  sticky='nsew',pady=(10, 0))


        # Create a StringVar to store the selected color
        self.edit_color = tk.StringVar(self)
        self.edit_color.set(self.parent.settings.bg_color)  # Set the default color

        # Create the OptionMenu with black and white options
        color_names = ('white', 'black', 'red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'purple', 'orange', 'pink', 'gray')
        color_options = OptionMenu(self, self.edit_color,*color_names)
        color_options.grid(row=3, column=1,  sticky='nsew',pady=(10, 0))
        color_options.config(font=(self.parent.settings.text_font, int(self.parent.settings.text_size)))

        self.label_size = tk.Label(self, text="字体大小",font=(self.parent.settings.text_font, int(self.parent.settings.text_size)))
        self.label_size.grid(row=4, column=0,  sticky='nsew',pady=(10, 0))
        

        self.edit_size = tk.StringVar(self)
        self.edit_size.set(str(self.parent.settings.text_size))  # Set the default color

        # Create the OptionMenu with black and white options
        size_options = OptionMenu(self, self.edit_size,*map(str,range(8,33)))
        size_options.grid(row=4, column=1,  sticky='nsew',pady=(10, 0))
        size_options.config(font=(self.parent.settings.text_font, int(self.parent.settings.text_size)))
        # self.edit_size = tk.Entry(self)
        # self.edit_size.insert(0, str(self.parent.settings.text_size))
        # self.edit_size.grid(row=2 ,column=1)
        
        # Add a Checkbutton for the boolean toggle
        self.toggle_var = tk.BooleanVar()  # This variable will hold the on/off state
        self.toggle_var.set(self.parent.settings.sound_on)  # Set default to True (on) or False (off)
        self.bool_toggle = tk.Checkbutton(self, text="设置声音提醒",font=(self.parent.settings.text_font, int(self.parent.settings.text_size)), variable=self.toggle_var)
        self.bool_toggle.grid(row=5, column=0, sticky='nsew', pady=(10, 0))

        ok_button = tk.Button(self, text="OK",font=(self.parent.settings.text_font, int(self.parent.settings.text_size)),command=self.update_settings)
        ok_button.grid(row=6, column=0,  sticky='nsew',pady=(10, 0))
    
        cancel_button = tk.Button(self, text="Cancel" ,font=(self.parent.settings.text_font, int(self.parent.settings.text_size)),command=self.cancel_settings)
        cancel_button.grid(row=6, column=1,  sticky='nsew',pady=(10, 0))

    def update_settings(self):
        isUpdateAlpha = False
        isUpdatebg = False
        isUpdateSize =False

        newSize =  int(self.edit_size.get())
        newAlpha =  str(self.edit_alpha.get())
        newBg = str(self.edit_color.get())
        toggle_state = self.toggle_var.get()

        newrestminutes =  str(self.edit_reset.get())
        newworkminutes =  str(self.edit_work.get())
        if self.parent.settings.sound_on  is not toggle_state:
            self.parent.settings.sound_on = toggle_state
        if self.parent.settings.text_size != newSize:
            # print("=======")
            self.parent.settings.text_size = newSize
            isUpdateSize = True
        if self.parent.settings.alpha not  in  newAlpha:
            # print("=======sssssssss")
            self.parent.settings.alpha = newAlpha
            isUpdateAlpha = True
        if self.parent.settings.bg_color not in newBg:
            # print("=======ssssssdddddd")
            self.parent.settings.bg_color  = newBg 
            isUpdatebg =True
            
        if str(self.parent.settings.restminutes) not in newrestminutes:
            self.parent.settings.restminutes  = int(newrestminutes )

        if str(self.parent.settings.workminutes) not in newworkminutes:
            self.parent.settings.workminutes  = int(newworkminutes )

        


        self.parent.updateUI(isUpdateAlpha,isUpdatebg,isUpdateSize)
        # self.parent.updateDataHand()
        self.destroy()
    
    def  cancel_settings(self):
         self.destroy()