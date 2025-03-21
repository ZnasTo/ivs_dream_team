##
# @author xkovacj00, Jakub Kováčik
#
#   This file contains Graphical User Interface for the calculator
from tkinter import *

root = Tk()

root.title("Calculator")
root.configure(bg = 'Black')
def show_screen(event=None):
    screen = entry.get()
    print(screen)

position = 0       # 0 chosen for better work with 10,100, etc
numbers = []

def getchar_from_button(character):
    global position

    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(character))
    
    if isinstance(character, int):
        save_number(character, position)
        position += 1
    
    elif character == '.':  #NOT WORKING
        if '.' not in current:
            print()
    
    if not (isinstance(character, int)):
        position = 0


def save_number(number, position):  #saves digits as one number
    digits = []     
    floatdigits = []    # this is not used in this version, just set up for future
    
    if position >= 0:
        tmp = save_to_list(digits, position)
        numbers.append(tmp)
        digits.clear()
        digits.append(number)
    
    if position < 0:    #not working, TODO NEXT VERSION
        digits.append(number + pow(10, position))
    
    numbers.append(sum(digits))

def save_to_list(digits, position):
    tmp = 0
    for digit in digits:
        tmp = digit + 10*position
        position -= 1
    return tmp

print(numbers)

entry = Entry(root, width = 25, borderwidth= 0, font = ("Arial", 20))
entry.grid(row = 0, column = 0, columnspan = 4, rowspan= 2, padx= 10, pady= 10)
entry.bind('<Return>', show_screen)
button_size = {"padx": 0, "pady": 0, "width": 5}

button_0 = Button(root, text = "0",**button_size, command= lambda: getchar_from_button(0))
button_1 = Button(root, text = "1",**button_size, command= lambda: getchar_from_button(1))
button_2 = Button(root, text = "2",**button_size, command= lambda: getchar_from_button(2))
button_3 = Button(root, text = "3",**button_size, command= lambda: getchar_from_button(3))
button_4 = Button(root, text = "4",**button_size, command= lambda: getchar_from_button(4))
button_5 = Button(root, text = "5",**button_size, command= lambda: getchar_from_button(5))
button_6 = Button(root, text = "6",**button_size, command= lambda: getchar_from_button(6))
button_7 = Button(root, text = "7",**button_size, command= lambda: getchar_from_button(7))
button_8 = Button(root, text = "8",**button_size, command= lambda: getchar_from_button(8))
button_9 = Button(root, text = "9",**button_size, command= lambda: getchar_from_button(9))



button_mode = Button(root, text = "mode",**button_size, bg="#4C4E4E")
button_help = Button(root, text = "?",**button_size, bg="#4C4E4E")
button_equal = Button(root, text = "=",**button_size, bg="#4C4E4E", command= lambda: getchar_from_button("="))
button_ac = Button(root, text = "AC",**button_size, bg="#4C4E4E", command= lambda: getchar_from_button("AC"))
button_lc = Button(root, text = "LC",**button_size, bg="#4C4E4E", command= lambda: getchar_from_button("LC"))


button_float = Button(root, text = ".",**button_size, command= lambda: getchar_from_button("."))
button_plus = Button(root, text = "+",**button_size, command= lambda: getchar_from_button("+"))
button_minus = Button(root, text = "-",**button_size, command= lambda: getchar_from_button("-"))
button_sqrt = Button(root, text = "\u221A",**button_size, command= lambda: getchar_from_button("\u221A"))
button_abs = Button(root, text = "abs",**button_size, command= lambda: getchar_from_button("abs: "))
button_multiply = Button(root, text = "*",**button_size, command= lambda: getchar_from_button("*"))
button_fact = Button(root, text = "!",**button_size, command= lambda: getchar_from_button("!"))
button_exp = Button(root, text = "exp",**button_size, command= lambda: getchar_from_button("exp: "))
button_div = Button(root, text = "/",**button_size, command= lambda: getchar_from_button("/"))



button_0.grid(row = 7, column = 1)
button_1.grid(row = 6, column = 0)
button_2.grid(row = 6, column = 1)
button_3.grid(row = 6, column = 2)


button_4.grid(row = 5, column = 0)
button_5.grid(row = 5, column = 1)
button_6.grid(row = 5, column = 2)

button_7.grid(row = 4, column = 0)
button_8.grid(row = 4, column = 1)
button_9.grid(row = 4, column = 2)


button_mode.grid(row = 7, column = 0)
button_float.grid(row = 7, column = 2)
button_help.grid(row = 7, column = 3)

button_equal.grid(row = 6, column = 3)

button_plus.grid(row = 5, column = 3)

button_minus.grid(row = 4, column = 3)
button_lc.grid(row = 3, column = 0)
button_sqrt.grid(row = 3, column = 1)
button_abs.grid(row = 3, column = 2)
button_multiply.grid(row = 3, column = 3)

button_ac.grid(row = 2, column = 0)
button_fact.grid(row = 2, column = 1)
button_exp.grid(row = 2, column = 2)
button_div.grid(row = 2, column = 3)


root.mainloop()