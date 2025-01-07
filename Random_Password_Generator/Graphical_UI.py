import random
import string
import tkinter
import traceback
from tkinter import *
from tkinter import messagebox

from win32ui import MessageBox

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

def check_Min_num(min_val):
    if min_val.isdigit():
        return True
    messagebox.showerror("Minimum Number field error", "Invalid input entered into field. Please enter valid number.")
    return False


def check_Max_num(max_val):
    if max_val.isdigit():
        return True
    messagebox.showerror("Maximum Number field error", "Invalid input entered into field. Please enter valid number.")
    return False


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
                            validatecommand="",
                            width=15,
                            justify="center",
                            relief="sunken",
                            font=("MS Sans Serif", 15))
    max_txt.grid(row=1, column=1, padx=0, pady=1, sticky=W)

    def generatePassword():
        '''
        print("Generate Password")
        mintxt = min_txt.get()
        maxtxt = max_txt.get()
        print(mintxt)
        print(str(maxtxt))
        '''

        min_length = min_txt.get()
        max_length = max_txt.get()

        """ Character types """
        ltr_low = list(string.ascii_lowercase)
        ltr_up = list(string.ascii_uppercase)
        nums = list(string.digits)
        sp_chars = list(string.punctuation)

        """ Password Length Parameters """
        password_len = random.randint(int(min_length), int(max_length))
        ltr_low_len = len(ltr_low)
        ltr_up_len = len(ltr_up)
        nums_len = len(nums)
        sp_chars_len = len(sp_chars)

        text2 = str(max_length + min_length)

        if check_Max_num(min_length) and check_Max_num(max_length):
            # pass_txt.insert(0, text2)

            try:
                passwrd_char_type = random.randint(0, 3)
                password = []

                print("Array Created.....")
                print(password)

                print("Password Length: " + str(password_len))

                pswrd_len = str(password_len)
                addPassLen(pswrd_len)

                x = 0

                while x < password_len:
                    passwrd_char_type = random.randint(0, 3)

                    if passwrd_char_type == 0:
                        password.append(ltr_low[random.randint(0, ltr_low_len - 1)])

                    elif passwrd_char_type == 1:
                        password.append(ltr_up[random.randint(0, ltr_up_len - 1)])

                    elif passwrd_char_type == 2:
                        password.append(nums[random.randint(0, nums_len - 1)])

                    elif passwrd_char_type == 3:
                        password.append(sp_chars[random.randint(0, sp_chars_len - 1)])

                    else:
                        password.append("# ERROR #")
                    x += 1

                print(password)
                passwrd_str = ''.join([str(s) for s in password])

                pass_txt.insert(0, passwrd_str)

                print(passwrd_str)

            except (ValueError, RuntimeError, TypeError, NameError):
                traceback.print_exc()
                print(Exception)

        else:
            messagebox.showerror("Error", "Oops Something went wrong.... \n Please input a valid input and try again.")

        '''

        if check_Max_num(text2):
            pass_txt.insert(0, "Pass: " + text2)
        else:
            pass_txt.insert(0, "Fail: " + text2)

        # pass_txt.insert(0, text2)

        '''

        '''
        if not check_Min_num(min_length) and not int(max_length):
            print("Min Value is: " + min_length + "please enter valid number")
            messagebox.showerror("Minimum Length: Invalid Input",
                                 "Please input a valid number in the minimum length field.")

        elif not check_Max_num(max_length) and not int(max_length):
            print("Min Value is: " + max_length + "please enter a valid number")
            messagebox.showerror("Maximum Length: Invalid Input",
                                 "Please input a valid number in the maximum length field.")

        else:

            """ Character types """
            ltr_low = list(string.ascii_lowercase)
            ltr_up = list(string.ascii_uppercase)
            nums = list(string.digits)
            sp_chars = list(string.punctuation)

            """ Password Length Parameters """
            password_len = random.randint(int(min_length), int(max_length))
            ltr_low_len = len(ltr_low)
            ltr_up_len = len(ltr_up)
            nums_len = len(nums)
            sp_chars_len = len(sp_chars)

            try:
                passwrd_char_type = random.randint(0, 3)
                password = []

                print("Array Created.....")
                print(password)

                print("Password Length: " + str(password_len))

                pswrd_len = str(password_len)
                addPassLen(pswrd_len)

                x = 0

                while x < password_len:
                    passwrd_char_type = random.randint(0, 3)

                    if passwrd_char_type == 0:
                        password.append(ltr_low[random.randint(0, ltr_low_len - 1)])

                    elif passwrd_char_type == 1:
                        password.append(ltr_up[random.randint(0, ltr_up_len - 1)])

                    elif passwrd_char_type == 2:
                        password.append(nums[random.randint(0, nums_len - 1)])

                    elif passwrd_char_type == 3:
                        password.append(sp_chars[random.randint(0, sp_chars_len - 1)])

                    else:
                        password.append("# ERROR #")
                    x += 1

                print(password)
                passwrd_str = ''.join([str(s) for s in password])

                print(passwrd_str)

            except (ValueError, RuntimeError, TypeError, NameError):
                traceback.print_exc()
                print(Exception)
            '''

    generate_btn = tkinter.Button(config_frame,
                                  width=15,
                                  text="Generate",
                                  command=generatePassword,
                                  bg="light green",
                                  borderwidth=5,
                                  justify="center",
                                  relief="raised",
                                  font=("MS Sans Serif", 13))
    generate_btn.grid(row=2, column=0, padx=5, pady=1, sticky=W)

    def clearParameters():
        min_txt.delete(0, END)
        max_txt.delete(0, END)
        print("Min and Max parameters have been cleared")

    clear_btn = tkinter.Button(config_frame,
                               width=15,
                               text="Clear",
                               command=clearParameters,
                               bg="light green",
                               borderwidth=5,
                               justify="center",
                               relief="raised",
                               font=("MS Sans Serif", 13))
    clear_btn.grid(row=2, column=1, padx=5, pady=1, sticky=W)

    bottom_frame = tkinter.Frame(config_frame)
    bottom_frame.grid(row=3, column=0)

    def createLog():
        print("Print Log")

    '''
    log_btn = tkinter.Button(bottom_frame,
                             command=createLog,
                             width=15,
                             text="Check Log",
                             bg="light green",
                             borderwidth=5,
                             justify="center",
                             relief="raised",
                             font=("MS Sans Serif", 13))
    log_btn.grid(row=3, column=0, padx=5, pady=1, sticky=W)
    '''
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

    def addPassLen(array_length):
        if array_length.isdigit():
            pass_len_lbl.config(text=array_length)
            return True
        return False

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

    def inputPassword(passwrd):
        if passwrd.contains(''):
            namess = str(passwrd)
            return True
        else:
            return False

    def resetPasswordSetting():
        print("Clear Password")
        pass_len_lbl.config(text="-" * 30)
        pass_txt.delete(0, END)

    reset_pass_btn = tkinter.Button(inner_generator_frame,
                                    width=30,
                                    command=resetPasswordSetting,
                                    text="Reset Password",
                                    bg="light green",
                                    borderwidth=5,
                                    justify="center",
                                    relief="raised",
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
