from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"

# Entry
input = Entry(width=10)
input.pack()


# Button

def button_clicked():
    my_label["text"] = "Submitted"
    print(input.get())
    new_label["text"] = "Entered value is : " + input.get()


button = Button(text="Click Me", command=button_clicked)
button.pack()

new_label = Label(text="I am a new Label", font=("Arial", 12, "bold"))
new_label.pack()

window.mainloop()
