from tkinter import *
import  parser

root = Tk()
root.title('calculadora')

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

# estoes para que los numeros solo se agreguen
i= 0
def get_numbers(n):
    global i
    display.insert(i, n)
    i += 1

    # para los operadores funcionen
def get_operation(operator):
        global i
        operator_lenght = len(operator)
        display.insert(i, operator)
        i += operator_lenght

        # limpiar numeros completos
def clear_display():
    display.delete(0, END)

        # limpiar numero uno por uno
def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
            clear_display()
            display.insert(0, 'error')

            # igual
def Calculate():
    display_state = display.get()
    try:
        math_expresion = parser.expr(display_state).compile()
        result = eval(math_expresion)
        clear_display()
        display.insert(0, result)
    except  expression as identifier:
        clear_display()
        display.insert(0, 'error')

#BUTTONS NUMERICS
Button(root, text='1', command=lambda:get_numbers(1)).grid(row=2, column=0, sticky=W+E)
Button(root, text='2', command=lambda:get_numbers(2)).grid(row=2, column=1, sticky=W+E)
Button(root, text='3', command=lambda:get_numbers(3)).grid(row=2, column=2, sticky=W+E)

Button(root, text='4', command=lambda:get_numbers(4)).grid(row=3, column=0, sticky=W+E)
Button(root, text='5', command=lambda:get_numbers(5)).grid(row=3, column=1, sticky=W+E)
Button(root, text='6', command=lambda:get_numbers(6)).grid(row=3, column=2, sticky=W+E)

Button(root, text='7', command=lambda:get_numbers(7)).grid(row=4, column=0, sticky=W+E)
Button(root, text='8', command=lambda:get_numbers(8)).grid(row=4, column=1, sticky=W+E)
Button(root, text='9', command=lambda:get_numbers(9)).grid(row=4, column=2, sticky=W+E)

# BUTTON PT:2
Button(root, text='C', command=lambda:clear_display()).grid(row=5, column=0, sticky=W+E)
Button(root, text='0', command=lambda:get_numbers(0)).grid(row=5, column=1, sticky=W+E)
Button(root, text='%', command=lambda:get_operation('%')).grid(row=5, column=2, sticky=W+E)

Button(root, text='+', command=lambda:get_operation('+')).grid(row=2, column=3, sticky=W+E)
Button(root, text='-', command=lambda:get_operation('-')).grid(row=3, column=3, sticky=W+E)
Button(root, text='*', command=lambda:get_operation('*')).grid(row=4, column=3, sticky=W+E)
Button(root, text='/', command=lambda:get_operation('/')).grid(row=5, column=3, sticky=W+E)

Button(root, text='☚', command=lambda:undo()).grid(row=2, column=4, sticky=W+E, columnspan=2)
Button(root, text='exp', command=lambda:get_operation('**')).grid(row=3, column=4, sticky=W+E)
Button(root, text='^2', command=lambda:get_operation('**2')).grid(row=3, column=5, sticky=W+E)
Button(root, text='(', command=lambda:get_operation('(')).grid(row=4, column=4, sticky=W+E)
Button(root, text=')', command=lambda:get_operation(')')).grid(row=4, column=5, sticky=W+E)
Button(root, text='=', command=lambda:Calculate()).grid(row=5, column=4, sticky=W+E, columnspan=2)


root.mainloop()