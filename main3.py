from tkinter import *

root = Tk()
root.geometry("300x200")
root.title("Calculator")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

def buttonClick():
  if firstNum.get() != "" and secondNum.get() != "":
    first = int(firstNum.get())
    second = int(secondNum.get())
    ans = str(first + second)
    Label1.config(text=ans)
  else:
    Label1.config(text="Please enter nums")

root_x = screen_width // 2 -100
root_y = screen_height // 2 - 100
root.geometry(f"400x50+{root_x}+{root_y}")

label = Label(root, text="Addition:", font=("Arial", 14))
label.grid(column=1, row=0)
firstNum = Entry(root, width=5, font=("Arial", 12))
firstNum.grid(column=2, row=0)
secondNum = Entry(root, width=5, font=("Arial", 12))
labelPlus = Label(root, text="+", font=("Arial", 14))
labelPlus.grid(column=3, row=0)
secondNum.grid(column=4, row=0)
button  = Button(root, text="=", font=("Arial", 14), command=buttonClick)
button.grid(column = 5, row = 0)
Label1 = Label(root, text="", font=("Arial", 14))
Label1.grid(column=6, row=0)
root.mainloop()