import tkinter as tk

def print_values():
    print("Limita 1:", slider1.get())
    print("Limita 2:", slider2.get())

root = tk.Tk()
root.title("Sobel Parameters")

slider1 = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Slider 1")
slider2 = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Slider 2")

print_button = tk.Button(root, text="Print Valori", command=print_values)
slider1.pack()
slider2.pack()
print_button.pack()

# Bucla infinita
root.mainloop()
