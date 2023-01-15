# Locally defined modules
import checker
import setup
import tkinter as tk

# Python modules
from openpyxl import load_workbook, Workbook

# Path to BOM Data.
path_to_data_1 = "C:\\Users\\bryndell.torio\\OneDrive - Integrated Micro-Electronics Inc\\Design\\Training\\bomgen\\Data\\bills_of_materials.xlsx"
path_to_data_2 = "C:\\Users\\bryndell.torio\\OneDrive - Integrated Micro-Electronics Inc\\Design\\Training\\bomgen\\Data\\test_data.xlsx"
path_to_data_3 = "C:\\Users\\bryndell.torio\\OneDrive - Integrated Micro-Electronics Inc\\Design\\Training\\bomgen\\Data\\bills_of_materials-tmp.xlsx"

wb = load_workbook(filename = path_to_data_3)
ws = wb.active

workbook_max_row = ws.max_row
workbook_max_column = ws.max_column

check_results = []

for i in range(workbook_max_row-setup.BOM_INDEX + 1):
    reference_List = ws.cell(row=setup.BOM_INDEX+i,column=3).value
    quantity_List = ws.cell(row=setup.BOM_INDEX+i,column=2).value
    comp_QR_result = checker.compare_quantity_to_reference(reference_List,quantity_List)

    if (comp_QR_result != False):
        check_results.append(str(comp_QR_result))

class myGUI():

    def __init__(self) -> None:

        self.root = tk.Tk()

        self.root.geometry("500x500")
        self.root.title("Integrater Micro-Electronics Inc. - Design and Development")


        self.label = tk.Label(self.root, text="BOM Generator", font=('Arial', 20))
        self.label.pack(padx=22, pady=22)


        self.button1 = tk.Button(self.root, text="Generate BOM", font=('Arial', 11), command=self.print_Check)
        self.button1.pack(padx=10, pady=10)

        self.button2 = tk.Button(self.root, text="Compare Netlist", font=('Arial', 11))
        self.button2.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=3, font=('Arial', 22))
        self.textbox.pack(padx=50,  expand=1)

        self.root.mainloop()

    def print_Check(self):
        print(check_results)

myGUI()


