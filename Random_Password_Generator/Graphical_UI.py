import tkinter
from tkinter import *


def createGUI():

    root = Tk()
    root.title("Password Generator: GUI")

    left_frame = Frame(root, width=400, height=500, bg="blue")
    left_frame.grid(row=0, column=0, padx=5, pady=5)

    left_top_frame = Frame(left_frame)
    left_top_frame.grid(row=0, column=0, padx=5, pady=5)

    Label(left_top_frame, text="Minimum").grid(row=0, column=0, padx=5, pady=0)
    Entry(left_top_frame).grid(row=0, column=1, padx=5, pady=0)
    Label(left_top_frame, text="Maximum").grid(row=1, column=0, padx=5, pady=0)
    Entry(left_top_frame).grid(row=1, column=1, padx=5, pady=0)

    left_middle_frame = Frame(left_frame)
    left_middle_frame.grid(row=1, column=0, padx=5, pady=5)

    Button(left_middle_frame, text="Generate").grid(row=0, column=0, padx=5, pady=5)
    Button(left_middle_frame, text="Clear Settings").grid(row=1, column=0, padx=5, pady=5)

    left_bottom_frame = Frame(left_frame)
    left_bottom_frame.grid(row=2, column=0, padx=5, pady=5)

    Button(left_bottom_frame, text="Open Log\n File").grid(row=0, column=0, padx=5, pady=5)

    #######################################################

    right_frame = Frame(root, width=400, height=500, bg="red")
    right_frame.grid(row=0, column=1, padx=5, pady=5)

    right_top_frame = Frame(right_frame)
    right_top_frame.grid(row=0, column=0, padx=5, pady=5)

    Label(right_top_frame, text="Password\nLength").grid(row=0, column=0, padx=0, pady=0)
    Label(right_top_frame, text="<<<<<<<(O)>>>>>>>").grid(row=0, column=1, padx=0, pady=0)

    right_middle_frame = Frame(right_frame)
    right_middle_frame.grid(row=1, column=0, padx=5, pady=5)

    Label(right_middle_frame, text="Generated Password").grid(row=0, column=0, padx=0, pady=0)
    Entry(right_middle_frame).grid(row=1, column=0, padx=0, pady=0)

    right_bottom_frame = Frame(right_frame)
    right_bottom_frame.grid(row=2, column=0, padx=5, pady=5)

    Button(right_bottom_frame, text="Clear Password").grid(row=0, column=0, padx=0, pady=0)

    root.mainloop()
