from tkinter import *
root = Tk()
calcule_list = []
main_list = []

root.title("Simple calculator")
box = Entry(root, width = 32, borderwidth = 5)
box.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def clear_func():
    global calcule_list 
    global main_list
    global variable
    box.delete(0, END)
    
    main_list = []
    calcule_list = []
    variable = 0 
    

def click_button(number):
    global variable
    variable = 0

    current = box.get()
    box.delete(0, END)

    box.insert(0, str(current) + str(number))
    variable = str(current) + str(number)
    variable = int(variable)

def add_func():
    main_list.append(variable)
    calcule_list.append("sum")
    box.delete(0, END)
    
def mult_func():
    main_list.append(variable)
    calcule_list.append("mult")
    box.delete(0, END)

def div_func():
    main_list.append(variable)
    calcule_list.append("div")
    box.delete(0, END)

def subs_func():
    main_list.append(variable)
    calcule_list.append("subs")
    box.delete(0, END)

def equ_func():
    global variable
    global main_list
    global calcule_list

    main_list.append(variable)
    variable = 0

    final = 0
    box.delete(0, END)

    for idx, i in enumerate(calcule_list):
        if i == "sum":
            if idx == 0:
                final += main_list[0] + main_list[1]
            else:
                try:
                    final += main_list[idx + 1]
                except IndexError:
                    continue

        elif i == "mult":
            if idx == 0:
                final += main_list[0] * main_list[1]
            else:
                try:
                    final *= main_list[idx + 1]
                except IndexError:
                    continue
        
        elif i == "div":
            if idx == 0:
                final += main_list[0] / main_list[1]
            else:
                try:
                    final /= main_list[idx + 1]
                except IndexError:
                    continue

        elif i == "subs":
            if idx == 0:
                final += main_list[0] - main_list[1]
            else:
                try:
                    final -= main_list[idx + 1]
                except IndexError:
                    continue
     
    variable = final
    main_list = []
    calcule_list = []
    
    box.insert(0, final)



#DEFINIR BOTONES
button_1 = Button(root, text = "1", padx = 25, pady = 15, command = lambda: click_button(1))
button_2 = Button(root, text = "2", padx = 25, pady = 15, command = lambda: click_button(2))
button_3 = Button(root, text = "3", padx = 25, pady = 15, command = lambda: click_button(3))
button_4 = Button(root, text = "4", padx = 25, pady = 15, command = lambda: click_button(4))
button_5 = Button(root, text = "5", padx = 25, pady = 15, command = lambda: click_button(5))
button_6 = Button(root, text = "6", padx = 25, pady = 15, command = lambda: click_button(6))
button_7 = Button(root, text = "7", padx = 25, pady = 15, command = lambda: click_button(7))
button_8 = Button(root, text = "8", padx = 25, pady = 15, command = lambda: click_button(8))
button_9 = Button(root, text = "9", padx = 25, pady = 15, command = lambda: click_button(9))
button_0 = Button(root, text = "0", padx = 100, pady = 15, command = lambda: click_button(0))

button_add = Button(root, text = "+", padx = 28, pady = 15, command = add_func)
button_multiply = Button(root, text = "*", padx = 28, pady = 15, command = mult_func)
button_divide = Button(root, text = "/", padx = 30, pady = 15, command = div_func)
button_substract = Button(root, text = "-", padx = 28, pady = 15, command = subs_func)
button_equal = Button(root, text = "=", padx = 98, pady = 15, command = equ_func)
button_clear = Button(root, text = "Clear", padx = 88, pady = 15, command = clear_func)
#POSICIONAR BOTONES
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)
button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)
button_0.grid(row = 4, column = 0, columnspan = 3)

button_add.grid(row = 5, column = 0, columnspan = 2)
button_multiply.grid(row = 5, column = 1, columnspan = 2)
button_divide.grid(row = 6, column = 0, columnspan = 2)
button_substract.grid(row = 6, column = 1, columnspan = 2)
button_equal.grid(row = 7, column = 0, columnspan = 3 )
button_clear.grid(row = 8, column = 0, columnspan = 3)

root.mainloop()
