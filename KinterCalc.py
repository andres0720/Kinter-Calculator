import tkinter as tk

root = tk.Tk()
root.title("kinterCalc")

#Define the Entry box 
e = tk.Entry(root, width = 35,borderwidth=5)
e.grid(row=0,column=0, columnspan=3,  padx=10,pady=10)

#Definning the results text box
result_text = tk.Text(root, height = 1, width=20, borderwidth=5)
result_text.grid(row=1, column=0, columnspan=3)
result_text.insert(tk.END, "")
result_text.config(state=tk.DISABLED)

#Main Functions definition
def button_click(number):
    curent = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(curent) + str(number))
    
def button_clear():
    e.delete(0, tk.END)
    
def button_addit():
    firstdig = e.get()
    global f_num
    f_num = int(firstdig)
    e.delete(0, tk.END)

def button_equals():
    seconddig= e.get()
    result = f_num + int(seconddig)
    
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Result: {result}")
    result_text.config(state=tk.DISABLED)

# Define Buttons
button1= tk.Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button2= tk.Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button3= tk.Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button4= tk.Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button5= tk.Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button6= tk.Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button7= tk.Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button8= tk.Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button9= tk.Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button0= tk.Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))

button_add= tk.Button(root, text='+', padx=39, pady=20, command=button_addit)
button_equal= tk.Button(root, text='=', padx=86.9, pady=20, command=button_equals)
button_clear= tk.Button(root, text='Clear', padx=77, pady=20, command=button_clear)


#put buttons on screen 
button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

button0.grid(row=5, column=0)
button_clear.grid(row=5, column=1, columnspan=2)
button_add.grid(row=6, column=0)
button_equal.grid(row=6, column=1, columnspan=2)

root.mainloop()