import tkinter as tk

def feetToMeeter(n):
    return round(0.3048 * n, 4)

def handleButtonClick():
    try:
        value = et.get()
        feet = int(value)
        meter = feetToMeeter(feet)
        answer.config(text = value + " feet = " + str(meter) + " meter", fg='green', font=("Arial",11, "bold"))
    except ValueError:
        answer.config(text = "Please enter a number!", fg = 'red' , font = 11)

window = tk.Tk()
window.resizable(0,0)
window.geometry("450x300")
window.title("Feet to Meter Converter")

welcome = tk.Label(window, text="Covert feet to meter!", fg="blue", font=("Helvetica", 14, 'bold', 'italic'))
welcome.pack()

et =tk.Entry(window, width=40)
et.insert(0, "Enter feet")
et.bind("<FocusIn>",lambda args: et.delete(0, "end"))
et.pack(side = "top", pady=20)


bt = tk.Button(window, text="Convert", command=handleButtonClick)
bt["fg"] = "white"
bt["font"] = ("roboto", 10, "bold")
bt["bg"] = "#03b6fc"
bt["border"] = "1"
bt.pack(side="top", pady = 10)

answer = tk.Label(window, text='')
answer.pack(pady=12)

window.mainloop()