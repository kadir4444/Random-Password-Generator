import string
import traceback
import random


def randomisePassword_Version1():
    """ Password Length Parameters """
    min_length = 8
    max_length = 15

    """ Character types """
    ltr_low = list(string.ascii_lowercase)
    ltr_up = list(string.ascii_uppercase)
    nums = list(string.digits)
    sp_chars = list(string.punctuation)

    """ Password Length Parameters """
    password_len = random.randint(min_length, max_length)
    ltr_low_len = len(ltr_low)
    ltr_up_len = len(ltr_up)
    nums_len = len(nums)
    sp_chars_len = len(sp_chars)

    try:
        passwrd_char_type = random.randint(0, 3)
        password = []
        print(password)

        print("Length: " + str(password_len))

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
    Next version will have Graphical interface
    Future releases will check generated passwords will contain at least a 1 special character and 1 number and 1 letters
    
    Version 2 - GUI interface will be interoduced allowing users to create passwords and allow them to copy it onto clipboard
    Version 3 - Advanced GUI interface
    Version 4 - Password Storage - Allows user to store passwords based on groups
    Version 4.1 - Users can set or pins favourite passwords
    Version 4.2 - Stored Passwords will be secured as users need to access it via password
    Version 4.3 - Sorting feature on stored passwords
    Version 5 - Reminder to change passwords and not use old passwords
    Version 5.1 - Make sure passwords are different and reminder to notify that same passwords for multiple apps and sites
    '''


