from tkinter import Label, Entry, Button, Tk

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
FONT = ("Avenir Next", 10, "bold")

equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

result_label = Label(text=0)
result_label.grid(column=1, row=1)

mile_label = Label(text="Miles", font=FONT)
mile_label.grid(column=2, row=0)

num_input = Entry(width=10)
num_input.grid(column=1, row=0)
num_input.insert(0, string=0)


def calculate_km():
    miles = float(num_input.get())
    kms = miles * 1.609
    return result_label.config(text=f"{kms}")


button = Button(text="Calculate", font=FONT, command=calculate_km)
button.grid(column=1, row=2)


window.mainloop()
