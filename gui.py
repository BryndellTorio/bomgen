import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Integrater Micro-Electronics Inc. - Design and Development")


label = tk.Label(root, text="BOM Generator", font=('Arial', 20))
label.pack(padx=22, pady=22)

button = tk.Button(root, text="Generate BOM", font=('Arial', 11))
button.pack(padx=10, pady=10)

button = tk.Button(root, text="Compare Netlist", font=('Arial', 11))
button.pack(padx=10, pady=10)

textbox = tk.Text(root, height=3, font=('Arial', 22))
textbox.pack(padx=50,  expand=1)

root.mainloop()

# Ref: https://www.youtube.com/watch?v=ibf5cx221hk
