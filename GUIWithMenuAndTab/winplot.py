from tkinter import *
import tkinter.ttk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib import animation
import numpy as np
import random
import time

def makeMenu():
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Graph1", command=donothing)
    filemenu.add_command(label="Graph2", command=donothing1)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    window.config(menu=menubar)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

def makeGraph1(tab):

    data2 = {'Year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2021, 2022],
             'Rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3, 8.7, 9.5, 7.8]
             }
    df2 = DataFrame(data2, columns=['Year', 'Rate'])

    figure2 = plt.Figure(figsize=(5, 4), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, tab)
    line2.get_tk_widget().pack(side=LEFT, fill=BOTH)
    df2 = df2[['Year', 'Rate']].groupby('Year').sum()
    df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
    ax2.set_title('Year Vs. Rate')

    label = Label(tab, text='제목')
    label.pack()
    entry = Entry(tab)
    entry.pack()
    label2 = Label(tab, text='값 추가')
    label2.pack()
    entry2 = Entry(tab)
    entry2.pack()
    btn1 = Button(tab, text='저장', width=20, height=15)
    btn1.pack()
    btn2 = Button(tab, text='삭제', width=20, height=15)
    btn2.pack()

def makeGraph2(tab):
    fig = Figure(figsize=(5, 5), dpi=100)
    y = [i ** 2 for i in range(101)]
    plot1 = fig.add_subplot(111)
    plot1.plot(y)

    canvas = FigureCanvasTkAgg(fig, master=tab)
    canvas.draw()

    canvas.get_tk_widget().pack(side='left')

    toolbar = NavigationToolbar2Tk(canvas, tab)
    toolbar.update()

    canvas.get_tk_widget().pack()

def makeTreeView(tab):
    frame = tkinter.Frame(tab, width=300, height = 300, bg='yellow')
    frame.grid(row=0, column=0,sticky='ew')

    tree = tkinter.ttk.Treeview(frame, columns=(1, 2, 3), height=5, show="headings")
    tree.pack(side='left')

    tree.heading(1, text="A")
    tree.heading(2, text="B")
    tree.heading(3, text="C")

    tree.column(1, width=100)
    tree.column(2, width=100)
    tree.column(3, width=100)

    scroll = tkinter.ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scroll.pack(side='right', fill='y')
    tree.configure(yscrollcommand=scroll.set)

    data = [["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["10", "11", "12"],
            ["13", "14", "15"],
            ["16", "17", "18"]]

    for val in data:
        tree.insert('', 'end', values=(val[0], val[1], val[2]))

    label = Label(tab, text="default text")
    label.grid(row=1, column=0,sticky='ew')

    def click_item(event):
        selectedItem = tree.focus()
        getValue = tree.item(selectedItem).get('values')
        label.configure(text=getValue)

    tree.bind('<ButtonRelease-1>', click_item)


def makeTab():
    notebook = tkinter.ttk.Notebook(window, width=700, height=500)
    notebook.pack()

    tab1 = tkinter.Frame(window)
    notebook.add(tab1, text=" Graph1 ")
    tab2 = tkinter.Frame(window)
    notebook.add(tab2, text=" Graph2 ")
    tab3 = tkinter.Frame(window)
    notebook.add(tab3, text=" Data ")
    tab4 = tkinter.Frame(window)
    notebook.add(tab4, text=" Graph3 ")

    return tab1, tab2, tab3, tab4

# def makeGraph():
#     pass
def donothing():
   makeGraph1(tab4)

def donothing1():
   pass

window = Tk()
window.title("Graph")
window.geometry("700x500+200+200")
makeMenu()
tab1, tab2, tab3, tab4 = makeTab()
makeGraph1(tab1)
makeGraph2(tab2)
makeTreeView(tab3)


window.mainloop()