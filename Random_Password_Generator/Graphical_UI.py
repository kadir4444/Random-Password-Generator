import random
import string
import tkinter
import traceback
from tkinter import *
from tkinter import messagebox

global logFiles


# Method used to check that min value is a number and will return an error message if anything else is inputted.
def check_Min_num(min_val):
    if min_val.isdigit():
        return True
    messagebox.showerror("Minimum Number field error", "Invalid input entered into field. Please enter valid number.")
    return False


# Method used to check that max value is a number and will return an error message if anything else is inputted.
def check_Max_num(max_val):
    if max_val.isdigit():
        return True
    messagebox.showerror("Maximum Number field error", "Invalid input entered into field. Please enter valid number.")
    return False


def createGUI():
    # Initialise GUI window with tkinter.
    root = Tk()
    root.title("Password Generator: GUI")
    root.config(background="Black")
    root.geometry("700x300")
    root.resizable(0, 0)

    # As the name suggests this is the frame that will hold the title.
    title_frame = tkinter.Frame(root)
    title_frame.pack()

    # This is the label that contains the title.
    title_lbl = tkinter.Label(title_frame,
                              text="Password Generator",
                              bg="light green",
                              borderwidth=5,
                              justify="center",
                              relief="sunken",
                              font=("MS Sans Serif", 20))
    title_lbl.grid(row=0, column=0, padx=0, pady=1, sticky=W)

    '''
    This is the content frame that will contain other frames like the config and generators frames to 
    keep the UI looking snazzy.
    '''
    content_frame = tkinter.Frame(root)
    content_frame.pack()

    '''
    This frame will  contain elements like the min and max value as well as buttons responsible for generating 
    passwords and clearing configuration passwords and in the future getting logs.
    '''
    config_frame = tkinter.Frame(content_frame)
    config_frame.grid(row=0, column=0)

    '''
    This frame contains elements that will display the password length, and the newly generated passwords and a 
    button to clear new passwords.
    '''
    generator_frame = tkinter.Frame(content_frame)
    generator_frame.grid(row=0, column=1)

    # Minimum Length title label
    min_title_lbl = tkinter.Label(config_frame,
                                  width=15,
                                  text="Minimum Length: ",
                                  bg="light green",
                                  borderwidth=5,
                                  justify="center",
                                  relief="sunken",
                                  font=("MS Sans Serif", 10))
    min_title_lbl.grid(row=0, column=0, padx=0, pady=1, sticky=W)

    # Minimum Length title label
    max_title_lbl = tkinter.Label(config_frame,
                                  width=15,
                                  text="Maximum Length: ",
                                  bg="light green",
                                  borderwidth=5,
                                  justify="center",
                                  relief="sunken",
                                  font=("MS Sans Serif", 10))
    max_title_lbl.grid(row=1, column=0, padx=0, pady=1, sticky=W)

    # Minimum Length value entry element
    min_txt = tkinter.Entry(config_frame,
                            width=15,
                            justify="center",
                            relief="sunken",
                            font=("MS Sans Serif", 15))
    min_txt.grid(row=0, column=1, padx=0, pady=1, sticky=W)

    # Maximum Length value entry element
    max_txt = tkinter.Entry(config_frame,
                            validatecommand="",
                            width=15,
                            justify="center",
                            relief="sunken",
                            font=("MS Sans Serif", 15))
    max_txt.grid(row=1, column=1, padx=0, pady=1, sticky=W)

    # method used to generate new password
    def generatePassword():
        # variable used to the value from min and max entry elements.
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

        # This if statement is used to check a number has been inputted into the min and max entry boxes.
        if check_Max_num(min_length) and check_Max_num(max_length):

            '''
            This try and except block is used to generate the new password and will throw error messages into a console 
            (In the future I will be ensuring that errors are entered onto a log file).
            '''
            try:
                passwrd_char_type = random.randint(0, 3)
                password = []

                print("Array Created.....")
                print(password)

                print("Password Length: " + str(password_len))

                pswrd_len = str(password_len)
                addPassLen(pswrd_len)

                x = 0

                '''
                This while loop is used to randomly select a character type for each character and will stop when the 
                password's max length is met.
                '''
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

    # This is the main button in this application without it, we are lost and will not be able to generate a password
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

    # Method to clear the configurations entry box parameters
    def clearParameters():
        min_txt.delete(0, END)
        max_txt.delete(0, END)
        print("Min and Max parameters have been cleared")

    # This is the button used to clear the min and max entry box values
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

    ''' Log frame 
    log_frame = tkinter.Frame(config_frame)
    log_frame.grid(row=3, column=0)

    
    # Open log method 
    def createLog():
        print("Print Log")
        logFiles = open("LogFile.txt")
        print("---" * 10)
        print("Log says: " + logFiles.read())

    # Open Log button constructor
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

    ''' Password Length Frame '''
    pass_len_frame = tkinter.Frame(generator_frame)
    pass_len_frame.grid(row=0, column=0)

    ''' Password Length Label Tile '''
    header_lbl3 = tkinter.Label(pass_len_frame,
                                width=15,
                                text="Password Length:",
                                bg="light green",
                                borderwidth=5,
                                justify="center",
                                relief="sunken",
                                font=("MS Sans Serif", 10))
    header_lbl3.grid(row=0, column=0, padx=0, pady=1, sticky=W)

    ''' View Password Length Label '''
    pass_len_lbl = tkinter.Label(pass_len_frame,
                                 width=18,
                                 text="-" * 30,
                                 bg="light green",
                                 borderwidth=5,
                                 justify="center",
                                 relief="sunken",
                                 font=("MS Sans Serif", 10))
    pass_len_lbl.grid(row=0, column=1, padx=0, pady=1, sticky=W)

    ''' Add password length label '''

    def addPassLen(array_length):
        if array_length.isdigit():
            pass_len_lbl.config(text=array_length)
            return True
        return False

    ''' Generator Frame which contains the elements that  '''
    inner_generator_frame = tkinter.Frame(generator_frame)
    inner_generator_frame.grid(row=1, column=0)

    # Entry box used to display the newly generated password
    pass_txt = tkinter.Entry(inner_generator_frame,
                             width=30,
                             bg="light green",
                             borderwidth=5,
                             justify="center",
                             relief="sunken",
                             font=("MS Sans Serif", 15))
    pass_txt.grid(row=0, column=0, padx=0, pady=1, sticky=W)

    # Method to clear and reset the array length label and the password entry box
    def resetPasswordSetting():
        print("Clear Password")
        pass_len_lbl.config(text="-" * 30)
        pass_txt.delete(0, END)

    # Button used to clear and reset the array length label and the password entry box
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

    # Author frame. So I can mark my handiwork
    author_frame = tkinter.Frame(generator_frame)
    author_frame.grid(row=2, column=0)

    # Label used for display my GitHub id
    build_deets = tkinter.Label(author_frame,
                                width=15,
                                text="Built by Kadir4444",
                                bg="light grey",
                                justify="right",
                                font=("MS Sans Serif", 5))
    build_deets.grid(row=0, column=0, padx=0, pady=1, sticky=W)

    root.mainloop()
