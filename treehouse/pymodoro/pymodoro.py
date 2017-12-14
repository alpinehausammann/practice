import tkinter


class Pymodoro:
    def __init__(self, master):
        self.master = master
        self.mainframe = tkinter.Frame(self.master, bg='white')
        #Creates the main iframe for application
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)
        #pack()
        self.build_grid()
        self.build_banner()
        self.build_buttons()

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=0)
        #First parameter designates the number column
        #The second parameter controls the proportionality of the row/column,
        #in referance to the frame it is contained within

    def build_banner(self):
        banner = tkinter.Label(
            self.mainframe,
            background='black',
            text='Pymodoro',
            fg='white',
            font=('Helvetica', 24)
        )
        banner.grid(
            row=0,column=0,
            sticky='ew',
            padx=10,

        )
    def build_buttons(self):
        buttons_frame = tkinter.Frame(self.mainframe)
        buttons_frame.grid(row=2,column=0, sticky='nsew', padx=10, pady=10)
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        self.start_button = tkinter.Button(
            buttons_frame,
            text='Start'
        )
        self.stop_button = tkinter.Button(
            buttons_frame,
            text='Stop'
        )
        self.start_button.grid(row=0, column=0, sticky='e', padx=10, pady=10
        )
        self.stop_button.grid(row=0, column=1, sticky='w', padx=10, pady=10
        )
    def button_onclick(self):
        
    def build_timer(self):
        timer_frame = tkinter.Frame(self.mainframe)
        timer_frame.grid()

if __name__ == '__main__':
    root = tkinter.Tk()
    Pymodoro(root)
    root.mainloop()
