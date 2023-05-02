# BOM Generator Tool

### OBJECTIVE:
+ To generate a formatted and validated BOM for OrCAD or Altium files.
+ To be able to recreate the BOM generator of IMI.


### TO DO:
+ Home path directory error
    - Move the program directory in desktop[$Home/Desktop/]


## References:
+ Reference: https://realpython.com/openpyxl-excel-spreadsheets-python/

# Format:
+ Header
    Item\tQuantity\tReference\tEAZIX_Part_Key\tSAP_Item_Code\tDescription\tManufacturer1\tMfr_Part_Number1\tManufacturer2\tMfr_Part_Number2\tROHS\tAssembly Notes
+ Combined Property String 
    {Item}\t{Quantity}\t{Reference}\t{EAZIX_Part_Key}\t{SAP_Item_Code}\t{Description}\t{Manufacturer1}\t{Mfr_Part_Number1}\t{Manufacturer2}\t{Mfr_Part_Number2}\t{ROHS}\t{Assembly Notes}
