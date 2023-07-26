import tkinter as tk
from tkinter import messagebox as msg


class MyGUI:

    def __init__(self):
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=exit)

        self.msgmenu = tk.Menu(self.menubar, tearoff=0)
        self.msgmenu.add_command(label="Show message", command=self.show_msg)
        self.msgmenu.add_command(label="Clear textbox", command=self.clear_textbox)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.msgmenu, label="Message")

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="Hello there")
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=3)
        self.textbox.bind("<Key>", self.pressed_key)
        self.textbox.pack(padx=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show message with MessageBox", variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show message", command=self.show_msg)
        self.button.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
        self.root.mainloop()

    def show_msg(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            msg.showinfo(title="My Message", message=self.textbox.get('1.0', tk.END))

    def pressed_key(self, event):
        if event.keysym.lower() == 'return' and event.state == 4:
            msg.showinfo(title="You pressed ctrl+return", message=self.textbox.get('1.0', tk.END))

    def close_window(self):
        if msg.askyesno(title="???", message="Are you sure you want to close the app?"):
            self.root.destroy()

    def clear_textbox(self):
        self.textbox.delete('1.0', tk.END)


MyGUI()