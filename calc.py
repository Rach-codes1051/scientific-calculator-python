import tkinter as tk
import math

# Create the main window
window = tk.Tk()
window.configure(bg="Pink")
window.title("Scientific Calculator")

window.geometry("350x450")


# Entry box to display input and output
display = tk.Entry(window, width=25, font=("Arial", 18), borderwidth=5,bg="Black",fg="White")
display.pack(pady=10)


# Function to add text to the display
def button_click(value):
    display.insert(tk.END, value)


# Function to clear the display
def clear_display():
    display.delete(0, tk.END)


# Function to calculate the result
def calculate():
    try:
        result = eval(display.get())
        clear_display()
        display.insert(0, result)
    except:
        clear_display()
        display.insert(0, "Error")


# Scientific functions
def sin():
    value = float(display.get())
    clear_display()
    display.insert(0, math.sin(math.radians(value)))

def cos():
    value = float(display.get())
    clear_display()
    display.insert(0, math.cos(math.radians(value)))

def tan():
    value = float(display.get())
    clear_display()
    display.insert(0, math.tan(math.radians(value)))

def sqrt():
    value = float(display.get())
    clear_display()
    display.insert(0, math.sqrt(value))


# Frame to hold buttons
buttons_frame = tk.Frame(window,bg="Sky blue")
buttons_frame.pack()


# Button layout
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+'
]


row = 0
col = 0

for button in buttons:
    if button == "=":
        tk.Button(buttons_frame, text=button, width=7, height=2,bg="Yellow",fg="Red",
                  command=calculate).grid(row=row, column=col)
    else:
        tk.Button(buttons_frame, text=button, width=7, height=2,bg="Yellow",fg="Red",
                  command=lambda b=button: button_click(b)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1


# Scientific buttons
tk.Button(window, text="sin", width=10,bg="Yellow",fg="Red", command=sin).pack(pady=2)
tk.Button(window, text="cos", width=10,bg="Yellow",fg="Red", command=cos).pack(pady=2)
tk.Button(window, text="tan", width=10,bg="Yellow",fg="Red", command=tan).pack(pady=2)
tk.Button(window, text="√", width=10,bg="Yellow",fg="Red", command=sqrt).pack(pady=2)
tk.Button(window, text="Clear", width=10,bg="Yellow",fg="Red", command=clear_display).pack(pady=5)


# Run the application
window.mainloop()




