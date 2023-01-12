# Locally defined modules
import checker
import setup

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

print(check_results)
