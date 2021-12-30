from tkinter import *

# constants
WIDTH = '300'
HEIGHT = '350'
BG_COLOUR = '#85ab54'

# cipher with validation
def performShift():

    # get inputs from the 'text' and 'shift' entries
    text = text_entry.get()
    shift = shift_entry.get()

    ciphertext = ''

    # this flag is set to true if a character with an ASCII value greater than 126
    # or less than 32 is detected
    boundary_flag = False

    if len(text) > 40:
        result_label.config(text='The text must have 40 characters or less, and\ncan only have characters that have an ASCII\nvalue between 32 and 126 can be used.')

    else:
        try: 
            int(shift)

            if int(shift) > 94 or int(shift) < -94:
                result_label.config(text='Please enter a shift between -94 and 94.')
                print('example')
            else:
                for letter in text:
                    ascii_old = ord(letter) # get ASCII value of current letter
                    if ascii_old > 126 or ascii_old < 32:
                        boundary_flag = True
                        break
                    ascii_new = ascii_old + int(shift) # add the shift to the current ASCII value
                    if ascii_new > 126:
                        ascii_new -= 95 # 95 characters between the 'space' (32) and '~' (126)
                    elif ascii_new < 32:
                        ascii_new += 95
                    new_char = chr(ascii_new) # turn the new ASCII value to the corresponding character
                    ciphertext += new_char

                if boundary_flag == False:
                    result_label.config(text=ciphertext)
                else: # i.e. if the program has detected a letter outside of the accepted range
                    result_label.config(text='The text must have 40 characters or less, and\ncan only have characters that have an ASCII\nvalue between 32 and 126 can be used.')
        except:
            result_label.config(text='Please enter a shift between -94 and 94.')

    


# setting up the window
root = Tk()
root.geometry(WIDTH + 'x' + HEIGHT)
root.config(bg=BG_COLOUR)
root.resizable(False, False)

# setting up the display frame
display_frame = Frame(root, bg=BG_COLOUR)
display_frame.pack()


title = Label(display_frame, text='Caesar Cipher', font='Bahnschrift 25 bold', bg=BG_COLOUR, pady=20)
title.pack(fill=X)

text_label = Label(display_frame, text='Please enter some text you want to encrypt', font='Bahnschrift 10', bg=BG_COLOUR, pady=10)
text_label.pack()
text_entry = Entry(display_frame, width=25, bg='#e2f5c9')
text_entry.pack()

shift_label = Label(display_frame, text='Please enter a number to shift the letters', font='Bahnschrift 10', bg=BG_COLOUR, pady=10)
shift_label.pack()
shift_entry = Entry(display_frame, width=5, bg='#e2f5c9')
shift_entry.pack()

encrypt_button = Button(display_frame, text='Encrypt', bg='#44572c', fg='white', command=performShift)
encrypt_button.pack()

# text that displays the result, or informs the user that an input is not accepted
result_label = Label(display_frame, font='Bahnschrift 10', bg=BG_COLOUR, pady=20)
result_label.pack()


root.mainloop()