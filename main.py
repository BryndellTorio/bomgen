# Core modules
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# 3rd party modules
from openpyxl import load_workbook, Workbook

# Locally defined modules
import checker
import setup

HOME = os.path.expanduser("~") + "\\Documents"
INITIAL_DIR = HOME + "bomgen\\Data\\bills_of_materials-tmp.xlsx"
ERR_FILE_LOCATION = HOME + "bomgen\\logs\\err.log"
print(HOME)
print(INITIAL_DIR)
print(ERR_FILE_LOCATION)



def validate_bom():
    global t_results
    global ws
    window.path_to_data = filedialog.askopenfilename(
            initialdir=INITIAL_DIR, # Change this to $HOME location.
            title="Select a file",
            filetypes=(("Excel files", "*.xlsx"),
                       ("BOM files", "*.BOM"),
                       ("all files", "*.*")))

    # Loading the selected bom file into the design.
    wb = load_workbook(filename = window.path_to_data)
    ws = wb.active

    workbook_max_row = ws.max_row
    workbook_max_column = ws.max_column

    t_results=[]
    for i in range(workbook_max_row-setup.BOM_INDEX+1):
        reference_List = ws.cell(row=setup.BOM_INDEX+i,column=3).value
        quantity_List = ws.cell(row=setup.BOM_INDEX+i,column=2).value
        comp_QR_result = checker.compare_quantity_to_reference(reference_List,quantity_List)
        if comp_QR_result:
            t_results.append(comp_QR_result)

    for x in range(len(t_results)):
        print(str(t_results[x]).split(':'))

    if t_results:
        error_log()

    # error_results=[]
    # error_results.append(str(ws['A2'].value).split('          '))
    # placeholder = str(error_results).split(',')

def error_log():
    fileName= HOME + ".\\log\\errlog.txt" # Replace filename as err.log
    errorFile = open(fileName, 'w')
    errorFile.write(str(t_results))
    errorFile.close()

    messagebox.showerror(title='Error:',message='Found mismatch in Quantity and Reference.')

    if messagebox.askyesnocancel(title='Debug log',message='Do you like to open debug log?'):
        os.startfile(fileName)

def temporary_function():
    tempo_results = str(t_results).split(',')
    print(tempo_results)

def print_path():
    print(window.path_to_data)

def print_results():
    print(t_results)

# Start of GUI loop.
window = tk.Tk()

window.geometry("500x500")
window.title("Integrater Micro-Electronics Inc. - Design and Development")
icon = tk.PhotoImage(file='.\\Images\\imi-logo.png')
window.iconphoto(True,icon)

label = tk.Label(window,
                 text="BOM Generator",
                 font=('Arial', 20))
label.pack(padx=22, pady=22)

button1 = tk.Button(window,
                    text="Generate BOM",
                    font=('Arial', 11),
                    command=validate_bom)
button1.pack(padx=10, pady=10)

button2 = tk.Button(window,
                    text="Path",
                    font=('Arial', 11),
                    command=print_path)
button2.pack(padx=10, pady=10)

button3 = tk.Button(window,
                    text="Check",
                    font=('Arial', 11),
                    command=print_results)
button3.pack(padx=10, pady=10)

textbox = tk.Text(window,
                  height=3,
                  font=('Arial', 22))
textbox.pack(padx=50,  expand=1)

window.mainloop()
# End of GUI loop.
