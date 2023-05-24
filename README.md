# BOM Generator Tool

### OBJECTIVE:
+ To generate a formatted and validated BOM for OrCAD or Altium files.
+ To be able to recreate the BOM generator of IMI.


### TO DO:
+ Use customtkinter examples to create a modern GUI.


## References:
+ Reference: https://realpython.com/openpyxl-excel-spreadsheets-python/

### BOM settings used for checking MPNs
+ Header
    - Item\tQuantity\tReference\tPCB Footprint\tDescription\tManufacturer1\tMfr_Part_Number1\tROHS\tAssembly Notes

+ Combined property string
    - {Item}\t{Quantity}\t{Reference}\t{PCB Footprint}\t{Description}\t{Manufacturer1}\t{Mfr_Part_Number1}\t{ROHS}\t{Assembly Notes}

### BOM settings used for generating Final BOM
+ Header
    - Item\tQuantity\tReference\tEAZIX_Part_Key\tSAP_Item_Code\tDescription\tManufacturer1\tMfr_Part_Number1\tManufacturer2\tMfr_Part_Number2\tROHS\tAssembly Notes

+ Combined property string
    - {Item}\t{Quantity}\t{Reference}\t{EAZIX_Part_Key}\t{SAP_Item_Code}\t{Description}\t{Manufacturer1}\t{Mfr_Part_Number1}\t{Manufacturer2}\t{Mfr_Part_Number2}\t{ROHS}\t{Assembly Notes}

