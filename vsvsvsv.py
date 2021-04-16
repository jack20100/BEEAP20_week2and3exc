


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.font as tkFont
import os
 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

class App:
    def __init__(self, root):
        # Changed title
        root.title("ALPHATEAM")# title changed ,Mohsen Fadaee and Jack hocock
        # Changed window size# size changed from W 700, h 500 to W900 ,h 700
        width = 700
        height = 600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.__LoadFile = tk.Button(root)
        self.__LoadFile["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.__LoadFile["font"] = ft
        self.__LoadFile["fg"] = "#000000"
        self.__LoadFile["justify"] = "center"
        self.__LoadFile["text"] = "load file"# changed Button
        self.__LoadFile.place(x=70, y=50, width=70, height=25)
        self.__LoadFile["command"] = self.__LoadFile_command

        self.__Combobox1 = ttk.Combobox(root)
        self.__Combobox1.place(x=550, y=50, width=80, height=25)
        self.__Combobox1.bind("<<ComboboxSelected>>", self.__comboBoxCb)

        self.__File_Label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.__File_Label["font"] = ft
        self.__File_Label["fg"] = "#333333"
        self.__File_Label["justify"] = "left"
        self.__File_Label["text"] = "Data file"
        self.__File_Label.place(x=130, y=50, width=200, height=25)
    
        self.__SelectTown = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.__SelectTown["font"] = ft
        self.__SelectTown["fg"] = "#333333"
        self.__SelectTown["justify"] = "center"
        self.__SelectTown["text"] = "Select town"#Changed Label 
        self.__SelectTown.place(x=450, y=50, width=70, height=25)

        # these canvases are broken, fix them
        
        self.__plot1 = tk.Canvas(root, width=234, height=140)
        self.__plot1.place(x=50, y=130 )

        self.__plot2 = tk.Canvas(root)
        self.__plot2.place(x=310, y=130, width=239, height=139)

        self.__plot3 = tk.Canvas(root)
        self.__plot3.place(x=50, y=290, width=233, height=157)

        self.__plot4 = tk.Canvas(root)
        self.__plot4.place(x=310, y=290, width=233, height=157)

    def __LoadFile_command(self):
        filePath = fd.askopenfilename(initialdir='.')
        
        self.__File_Label.config(text = os.path.basename(filePath))                    
        try:
            self.__df = pd.read_csv(filePath)
            self.__df = self.__df.dropna()
            self.__Combobox1['values'] = list(self.__df['COMMUNITY AREA NAME'].unique())
            
        except:
            
            #print('nope'), fixed
            tk.messagebox.showinfo("Nope","NOPE ")

    # desired behavior: select one area, show 4 plots drawn on 4 canvases of that area: 
    # top left: bar chart, average KWH by month
    # top right: bar chart, average THERM by month
    # bottom left and bottom right up to you
    def __comboBoxCb(self, event=None):
        self.__subdf = self.__df.loc[self.__df['COMMUNITY AREA NAME'] == self.__Combobox1.get()]
        print(self.__subdf.head())
        fig1 = Figure(figsize=(self.__plot3.winfo_width, self.__plot3.winfo_height), dpi=100)
        ax1 = fig1.add_subplot(111)
        self.__subdf.iloc[:, range(self.__subdf.columns.get_loc['KWH JANUARY 2010'], 12)].mean().plot.bar(ax=ax1)
       
        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
