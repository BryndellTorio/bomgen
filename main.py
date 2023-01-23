# Core modules
import os
import tkinter as tk
from tkinter import BOTTOM, LEFT, RIGHT, SUNKEN, Label, filedialog, messagebox
from datetime import date
import time

# 3rd party modules
from openpyxl import load_workbook, Workbook

# Locally defined modules
import checker
import setup

# Path definition
HOME = os.path.expanduser("~") + "\\Documents"
INITIAL_DIR = HOME + "\\bomgen\\Data"
LOG_FILE_LOCATION = HOME + "\\bomgen\\log\\err.log"
LOGO_LOCATION = HOME + "\\bomgen\\Images\\IMI-Logo.png"

def validate_bom():
    set_statusbar_message("Generating BOM...")
    window.path_to_data = filedialog.askopenfilename(
            initialdir=INITIAL_DIR, # Change this to $HOME location.
            title="Select a file",
            filetypes=(("Excel files", "*.xlsx"), # ("BOM files", "*.BOM"), Check if .BOM can be processed.
                       ("all files", "*.*")))

    # Loading the selected bom file into the design.
    wb = load_workbook(filename = window.path_to_data)
    ws = wb.active

    workbook_max_row = ws.max_row
    workbook_max_column = ws.max_column

    t_results=[]
    for i in range(workbook_max_row-setup.BOM_INDEX+1):
        reference_list = ws.cell(row=setup.BOM_INDEX+i,column=3).value
        quantity_list = ws.cell(row=setup.BOM_INDEX+i,column=2).value
        comp_QR_result = checker.compare_quantity_to_reference(reference_list,quantity_list,i)
        if comp_QR_result:
            t_results.append(comp_QR_result)

    if t_results:
        log("WRITE_ERROR",list=t_results)

    # Might be useful in extracting the schematic filename.
    # error_results=[]
    # error_results.append(str(ws['A2'].value).split('          '))
    # placeholder = str(error_results).split(',')

def show_err_message():
    messagebox.showerror(title='Error:',message='Found mismatch in Quantity and Reference.')
    if messagebox.askyesnocancel(title='log',message='Do you like to open log file?'):
        os.startfile(LOG_FILE_LOCATION)

def set_statusbar_message(select_status):
    status['text'] = select_status

def log(select,message="",list=[]):
    fileName=LOG_FILE_LOCATION
    if select == "WRITE":
        logFile = open(fileName, 'a')
        logFile.write(message)
        logFile.close()
    elif select == "WRITE_ERROR":
        set_statusbar_message("ERROR found check log file.")
        DATE = date.today()
        log("WRITE",message=f"###\tSTART [{DATE}]\t###\n")
        arr = []
        for i in range(len(list)):
            arr.append(str(list[i]).split(":"))

        for j in range(len(arr)):
            item_number = arr[j][0]
            ref_count = arr[j][1]
            qty_count = arr[j][2]
            curr_time = time.strftime("%H:%M:%S", time.localtime())
            message_log = f"ERROR: Reference and Quantity item count mismatch. [{curr_time}]=>\titem:{item_number}\t\tReference count:{ref_count}\tQuantity count:{qty_count}\n"
            log("WRITE", message=message_log)
        log("WRITE",message="###\tEND\t###\n")
        show_err_message()

def open_log_file():
    set_statusbar_message("Opening log file...")
    os.startfile(LOG_FILE_LOCATION)
    set_statusbar_message("Done.")

def clear_log():
    set_statusbar_message("Clearing log file")
    fileName=LOG_FILE_LOCATION
    logFile = open(fileName, 'w')
    logFile.close()
    set_statusbar_message("Done.")

# Start of GUI loop.
window = tk.Tk()

window.geometry("350x350")
window.title("Integrater Micro-Electronics Inc. - Design and Development")
icon = tk.PhotoImage(file=LOGO_LOCATION)
window.iconphoto(True,icon)

label = tk.Label(window,
                 text="BOM Generator",
                 font=('Arial', 20))
label.pack(padx=15, pady=15)

button1 = tk.Button(window,
                    text="Generate BOM",
                    font=('Arial', 11),
                    command=validate_bom)
button1.pack(padx=10, pady=10)

button2 = tk.Button(window,
                    text="Open Log",
                    font=('Arial', 11),
                    command=open_log_file)
button2.pack(padx=10, pady=10)

button3 = tk.Button(window,
                    text="Clear Log",
                    font=('Arial', 11),
                    command=clear_log)
button3.pack(padx=10, pady=10)

status_message = ""
status = Label(window,
               text=status_message,
               bd=1,
               relief=SUNKEN,
               anchor="w",
               font=('Arial', 9))
status.pack(side=BOTTOM, fill="x")

window.mainloop()
# End of GUI loop.
