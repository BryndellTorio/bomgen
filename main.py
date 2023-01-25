# Core modules
import os
import time
import tkinter as tk
from tkinter import BOTTOM, SUNKEN, Label, filedialog, messagebox
from datetime import date

# 3rd party modules
from openpyxl import load_workbook

# Locally defined modules
import checker

# [DEFINITION]
# Path definition
HOME = os.path.expanduser("~") + "\\Documents"
INITIAL_DIR = HOME + "\\bomgen\\Data"
LOG_FILE_LOCATION = HOME + "\\bomgen\\log\\err.log"
LOGO_LOCATION = HOME + "\\bomgen\\Images\\IMI-Logo.png"
FORMAT_LOCATION = HOME + "\\bomgen\\Format\\Default_Format.xlsx"

# BOM column number definitions
QUANTITY_INDEX = 2
REFERENCE_INDEX = 3
EAZIX_INDEX = 4
SAP_INDEX = 5
MANUFACTURER1_INDEX = 7
MPN1_INDEX = 8
MANUFACTURER2_INDEX = 9
MPN2_INDEX = 10
NOTES_INDEX = 12

# Index of BOM file.
BOM_INDEX = 15

# [IMPORTANT] Save the *.BOM files as Excel Workbook. Stict Open XML Spreadsheet format will cause errors.
def validate_bom():
    set_statusbar_message("Generating BOM...")
    window.path_to_data = filedialog.askopenfilename(
            initialdir=INITIAL_DIR, # Change this to $HOME location.
            title="Select a file",
            filetypes=(("Excel files", "*.xlsx"), # ("BOM files", "*.BOM"), Check if .BOM can be processed.
                       ("all files", "*.*")))

    # Loading the selected bom file into the design.
    wb = load_workbook(filename=window.path_to_data, read_only=True)
    ws = wb.active

    # Validating item count for Reference and Quantity column.
    t_results=[]

    BOM_MAX_ROW = ws.max_row-BOM_INDEX+1

    for i in range(BOM_MAX_ROW):
        comp_QR_result = checker.compare_quantity_to_reference(ws.cell(row=BOM_INDEX+i,column=REFERENCE_INDEX).value,
                                                               ws.cell(row=BOM_INDEX+i,column=QUANTITY_INDEX).value,
                                                               i)
        if comp_QR_result:
            t_results.append(comp_QR_result)

    if t_results:
        log("WRITE_ITEM_COUNT_ERROR",list=t_results)

def test_function():
    window.path_to_data = filedialog.askopenfilename(
            initialdir=INITIAL_DIR, # Change this to $HOME location.
            title="Select a file",
            filetypes=(("Excel files", "*.xlsx"), # ("BOM files", "*.BOM"), Check if .BOM can be processed.
                       ("all files", "*.*")))

    # Loading the selected bom file into the design.
    wb = load_workbook(filename=window.path_to_data, read_only=True)
    ws = wb.active

    BOM_MAX_ROW = ws.max_row-BOM_INDEX+1

    # Validating MPN1
    mpn1_list=[] 
    place_holder=[]
    for i in range(BOM_MAX_ROW):
       mpn1_list.append(ws.cell(row=BOM_INDEX+i,column=MPN1_INDEX).value)
    mpn1_list = checker.check_column(mpn1_list,length=BOM_MAX_ROW)

    mpn1_results=[]
    for i in range(len(mpn1_list)):
        place_holder = mpn1_list[i].split(':')

        # Checks if the item is already listed in mpn1_results list if no append to the list.
        ELEMENT1 = place_holder[0]
        ELEMENT2 = place_holder[1]
        mark1 = checker.check_list_content(mpn1_results,ELEMENT1)
        if mark1 == 0:
            mpn1_results.append(ELEMENT1)
        mark2 = checker.check_list_content(mpn1_results,ELEMENT2)
        if mark2 == 0:
            mpn1_results.append(ELEMENT2)
    print(mpn1_results)

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
    elif select == "WRITE_ITEM_COUNT_ERROR":
        set_statusbar_message("ERROR found check log file.")
        DATE = date.today()
        curr_time = time.strftime("%H:%M:%S", time.localtime())
        log("WRITE",message=f"###\tSTART\t###\t[{curr_time} {DATE}]\n")

        # Split the received list using ':' then store it in an array.
        arr = []
        for i in range(len(list)):
            arr.append(str(list[i]).split(":"))

        for index in range(len(arr)):
            item_number = arr[index][0]
            ref_count = arr[index][1]
            qty_count = arr[index][2]
            message_log = f"ERROR: Reference and Quantity item count mismatch.===> Row:{int(item_number)+BOM_INDEX-1}\t\tReference count:{ref_count}\tQuantity count:{qty_count}\n"
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

button4 = tk.Button(window,
                    text="Test",
                    font=('Arial', 11),
                    command=test_function)
button4.pack(padx=10, pady=10)

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
