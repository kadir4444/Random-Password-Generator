import tkinter
from tkinter import *

import tk

"""

entry = tkinter.Entry()


def on_entry_click(event):
    #function that gets called whenever entry is clicked
    if entry.get() == 'Enter your user name...':
        entry.delete(0, "end")  # delete all the text in the entry
        entry.insert(0, '')  #Insert blank for user input
        entry.config(fg='black')


def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'Enter your username...')
        entry.config(fg='grey')
"""


# root = tkinter
# root.title("Password Generator: GUI")


# root.config(background="Grey")
# root.resizable(None, None)


def createGUI():
    root = Tk()
    root.title("Password Generator: GUI")
    root.config(background="Black")
    root.geometry("700x300")
    root.resizable(0, 0)

    title_frame = tkinter.Frame(root)
    title_frame.pack()

    title_lbl = tkinter.Label(title_frame,
                              text="Password Generator",
                              bg="light green",
                              borderwidth=5,
                              justify="center",
                              relief="sunken",
                              font=("MS Sans Serif", 20))
    title_lbl.grid(row=0, column=0, padx=0, pady=1, sticky=W)

    """
    header_frame = tkinter.Frame(root)
    header_frame.pack()

    p_config_lbl = tkinter.Label(header_frame,
                                 text="Password Config: ",
                                 bg="light green",
                                 borderwidth=5,
                                 justify="center",
                                 relief="sunken",
                                 font=("MS Sans Serif", 15))
    p_config_lbl.grid(row=0, column=0, padx=0, pady=1, sticky=W)

    header_lbl2 = tkinter.Label(header_frame,
                                text="-" * 30,
                                bg="light green",
                                borderwidth=5,
                                justify="center",
                                relief="sunken",
                                font=("MS Sans Serif", 20))
    header_lbl2.grid(row=0, column=1, padx=0, pady=1, sticky=W)

    """

    content_frame = tkinter.Frame(root)
    content_frame.pack()

    config_frame = tkinter.Frame(content_frame)
    config_frame.grid(row=0, column=0)

    generator_frame = tkinter.Frame(content_frame)
    generator_frame.grid(row=0, column=1)

    min_title_lbl = tkinter.Label(config_frame,
                                  width=15,
                                  text="Minimum Length: ",
                                  bg="light green",
                                  borderwidth=5,
                                  justify="center",
                                  relief="sunken",
                                  font=("MS Sans Serif", 10))
    min_title_lbl.grid(row=0, column=0, padx=0, pady=1, sticky=W)

    header_lbl3 = tkinter.Label(config_frame,
                                width=15,
                                text="Maximum Length: ",
                                bg="light green",
                                borderwidth=5,
                                justify="center",
                                relief="sunken",
                                font=("MS Sans Serif", 10))
    header_lbl3.grid(row=1, column=0, padx=0, pady=1, sticky=W)

    min_txt = tkinter.Entry(config_frame,
                            width=15,
                            justify="center",
                            relief="sunken",
                            font=("MS Sans Serif", 15))
    min_txt.grid(row=0, column=1, padx=0, pady=1, sticky=W)

    max_txt = tkinter.Entry(config_frame,
                            width=15,
                            justify="center",
                            relief="sunken",
                            font=("MS Sans Serif", 15))
    max_txt.grid(row=1, column=1, padx=0, pady=1, sticky=W)

    generate_btn = tkinter.Button(config_frame,
                                  width=15,
                                  text="Generate",
                                  bg="light green",
                                  borderwidth=5,
                                  justify="center",
                                  relief="sunken",
                                  font=("MS Sans Serif", 13))
    generate_btn.grid(row=2, column=0, padx=5, pady=1, sticky=W)

    clear_btn = tkinter.Button(config_frame,
                               width=15,
                               text="Clear",
                               bg="light green",
                               borderwidth=5,
                               justify="center",
                               relief="sunken",
                               font=("MS Sans Serif", 13))
    clear_btn.grid(row=2, column=1, padx=5, pady=1, sticky=W)

    bottom_frame = tkinter.Frame(config_frame)
    bottom_frame.grid(row=3, column=0)

    def createLog():
        print("Print Log")

    log_btn = tkinter.Button(bottom_frame,
                             command=createLog,
                             width=15,
                             text="Check Log",
                             bg="light green",
                             borderwidth=5,
                             justify="center",
                             relief="sunken",
                             font=("MS Sans Serif", 13))
    log_btn.grid(row=3, column=0, padx=5, pady=1, sticky=W)

    pass_len_frame = tkinter.Frame(generator_frame)
    pass_len_frame.grid(row=0, column=0)

    header_lbl3 = tkinter.Label(pass_len_frame,
                                width=15,
                                text="Password Length:",
                                bg="light green",
                                borderwidth=5,
                                justify="center",
                                relief="sunken",
                                font=("MS Sans Serif", 10))
    header_lbl3.grid(row=0, column=0, padx=0, pady=1, sticky=W)

    pass_len_lbl = tkinter.Label(pass_len_frame,
                                 width=18,
                                 text="-" * 30,
                                 bg="light green",
                                 borderwidth=5,
                                 justify="center",
                                 relief="sunken",
                                 font=("MS Sans Serif", 10))
    pass_len_lbl.grid(row=0, column=1, padx=0, pady=1, sticky=W)

    inner_generator_frame = tkinter.Frame(generator_frame)
    inner_generator_frame.grid(row=1, column=0)

    pass_txt = tkinter.Entry(inner_generator_frame,
                             width=30,
                             bg="light green",
                             borderwidth=5,
                             justify="center",
                             relief="sunken",
                             font=("MS Sans Serif", 15))
    pass_txt.grid(row=0, column=0, padx=0, pady=1, sticky=W)

    def clearSetting():
        print("ll")

    reset_pass_btn = tkinter.Button(inner_generator_frame,
                                    width=30,
                                    command=clearSetting,
                                    text="Reset Password",
                                    bg="light green",
                                    borderwidth=5,
                                    justify="center",
                                    relief="sunken",
                                    font=("MS Sans Serif", 14))
    reset_pass_btn.grid(row=1, column=0, padx=0, pady=1, sticky=W)

    author_frame = tkinter.Frame(generator_frame)
    author_frame.grid(row=2, column=0)

    build_deets = tkinter.Label(author_frame,
                                width=15,
                                text="Built by Kadir4444",
                                bg="light grey",
                                justify="right",
                                font=("MS Sans Serif", 5))
    build_deets.grid(row=0, column=0, padx=0, pady=1, sticky=W)

    root.mainloop()





