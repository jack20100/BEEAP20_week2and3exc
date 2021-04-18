import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.font as tkFont

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

class App:
    def __init__(self, root):
        # changed title
        root.title("Alphateam")
        # changed window size
        width = 700
        height = 600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
         # Add a new name for open file "buttton" 
        self.__GButton_450 = tk.Button(root)
        self.__GButton_450["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.__GButton_450["font"] = ft
        self.__GButton_450["fg"] = "#000000"
        self.__GButton_450["justify"] = "center"
<<<<<<< HEAD
        self.__GButton_450["text"] = "load_files"#label changed 
=======
        self.__GButton_450["text"] = "load_file"
>>>>>>> 30081284d370ae2f2f7770d299e7d619ad98a6b8
        self.__GButton_450.place(x=70, y=50, width=70, height=25)
        self.__GButton_450["command"] = self.__GButton_450_command
         #Add a lable for "load_file" button
        self.__GListBox_563 = ttk.Combobox(root)
        self.__GListBox_563.place(x=350, y=50, width=80, height=25)
        self.__GListBox_563.bind("<<ComboboxSelected>>", self.__comboBoxCb)
        self.__GLabel_544 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.__GLabel_544["font"] = ft
        self.__GLabel_544["fg"] = "#333333"
        self.__GLabel_544["justify"] = "center"
<<<<<<< HEAD
        self.__GLabel_544["text"] = "Data_files"#label changed
=======
        self.__GLabel_544["text"] = "Data_files"
>>>>>>> 30081284d370ae2f2f7770d299e7d619ad98a6b8
        self.__GLabel_544.place(x=150, y=50, width=70, height=25)
        
        
    
        self.__SelectTown = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.__SelectTown["font"] = ft
        self.__SelectTown["fg"] = "#333333"
        self.__SelectTown["justify"] = "center"
        self.__SelectTown["text"] = "Select town"#Changed Label 
        self.__SelectTown.place(x=450, y=50, width=70, height=25)

        # these canvases are broken, fix them
        self.__GLineEdit_517 = tk.Canvas(root)
        self.__GLineEdit_517.place(x=50, y=130, width=234, height=140)

        self.__GLineEdit_985 = tk.Canvas(root)
        self.__GLineEdit_985.place(x=310, y=130, width=239, height=139)

        self.__GLineEdit_392 = tk.Canvas(root)
        self.__GLineEdit_392.place(x=50, y=290, width=233, height=157)

        self.__GLineEdit_700 = tk.Canvas(root)
        self.__GLineEdit_700.place(x=310, y=290, width=234, height=158)

    def __GButton_450_command(self):
        filePath = fd.askopenfilename(initialdir='.')
        try:
            self.__df = pd.read_csv(filePath)
            self.__df = self.__df.dropna()
            self.__GListBox_563['values'] = list(self.__df['COMMUNITY AREA NAME'].unique())
        except:
            # quick and dirty, desired behavior would be to show a notification pop up that says
            # "nope!"
            print('nope')

    # desired behavior: select one area, show 4 plots drawn on 4 canvases of that area: 
    # top left: bar chart, average KWH by month
    # top right: bar chart, average THERM by month
    # bottom left and bottom right up to you
    def __comboBoxCb(self, event=None):
        self.__subdf = self.__df.loc[self.__df['COMMUNITY AREA NAME'] == self.__GListBox_563.get()]
        print(self.__subdf.head())
        fig1 = Figure(figsize=(self.__GLineEdit_392.winfo_width, self.__GLineEdit_392.winfo_height), dpi=100)
        ax1 = fig1.add_subplot(111)
        self.__subdf.iloc[:, range(self.__subdf.columns.get_loc['KWH JANUARY 2010'], 12)].mean().plot.bar(ax=ax1)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
