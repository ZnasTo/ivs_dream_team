from tkinter import *

root = Tk()
root.title("Calculator")

def show_screen(event=None):
    screen = entry.get()
    print(screen)




entry = Entry(root, width = 25, borderwidth= 0, font = ("Arial", 20))
entry.grid(row = 0, column = 0, columnspan = 4, rowspan= 2, padx= 10, pady= 10)
entry.bind('<Return>', show_screen)
button_size = {"padx": 0, "pady": 0, "width": 5}

button_0 = Button(root, text = "0",**button_size)
button_1 = Button(root, text = "1",**button_size)
button_2 = Button(root, text = "2",**button_size)
button_3 = Button(root, text = "3",**button_size)
button_4 = Button(root, text = "4",**button_size)
button_5 = Button(root, text = "5",**button_size)
button_6 = Button(root, text = "6",**button_size)
button_7 = Button(root, text = "7",**button_size)
button_8 = Button(root, text = "8",**button_size)
button_9 = Button(root, text = "9",**button_size)



button_mode = Button(root, text = "mode",**button_size)
button_float = Button(root, text = ".",**button_size)
button_help = Button(root, text = "?",**button_size)
button_equal = Button(root, text = "=",**button_size)
button_plus = Button(root, text = "+",**button_size)
button_minus = Button(root, text = "-",**button_size)
button_lc = Button(root, text = "LC",**button_size)
button_sqrt = Button(root, text = "\u221A",**button_size)
button_abs = Button(root, text = "abs",**button_size)
button_multiply = Button(root, text = "*",**button_size)
button_ac = Button(root, text = "AC",**button_size)
button_fact = Button(root, text = "!",**button_size)
button_exp = Button(root, text = "exp",**button_size)
button_div = Button(root, text = "/",**button_size)



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