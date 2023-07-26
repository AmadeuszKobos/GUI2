import tkinter as tk
from tkinter import messagebox as msg

class MyGUI:

    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Hello there")
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=3)
        self.textbox.bind("<Key>", self.PressedKey)
        self.textbox.pack(padx=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show message with MessageBox", variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show message", command=self.ShowMSG)
        self.button.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.CloseWindow)
        self.root.mainloop()

    def ShowMSG(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            msg.showinfo(title="My Message", message=self.textbox.get('1.0', tk.END))

    def PressedKey(self, event):
        if event.keysym.lower() == 'return' and event.state == 4:
            msg.showinfo(title="You pressed ctrk+return", message=self.textbox.get('1.0', tk.END))

    def CloseWindow(self):
        if msg.askyesno(title="???", message="Are you sure you want to close the app?"):
            self.root.destroy()

MyGUI()