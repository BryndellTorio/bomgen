BOM_INDEX = 15

def compare_list(LIST1, LIST2):
    comparison_results=[]
    for i in range(len(LIST1)):
        for j in range(len(LIST2)):
            if (LIST1[i] == LIST2[j]):
                comparison_results.append(LIST1[i])
    return comparison_results

def compare_quantity_to_reference(Reference_List, quantity_list,item_number):
    QTR_Results=[]
    ref_list = str(Reference_List).split(',')
    ref_list_length = len(ref_list)

    # Return error list, format: [Item:reference count:quantity count]
    if (ref_list_length != quantity_list):
        QTR_Results = f"{item_number+1}:{ref_list_length}:{quantity_list}"
        return QTR_Results
    else:
        return False

# Checks each element inside a list then returns 0 if no match is found.
def check_list_content(LIST,ELEMENT):
    mark=0
    for i in range(len(LIST)):
        if LIST[i] == ELEMENT:
            mark=+1
    return mark

def check_column(LIST, length=0):
    results=[]
    LIST_COPY=[]

    # Create a copy of LIST with 1 element greater. To workaround the out of range list error.
    for x in range(length):
        LIST_COPY.append(LIST[x])
    LIST_COPY.append(0)

    for i in range(length):
        if i != length:
            for j in range(1, length-i):
                if LIST[i] == LIST_COPY[i+j]:
                    ELEMENT1 = f'{LIST[i]}:{i+BOM_INDEX}'
                    ELEMENT2 = f'{LIST[i+j]}:{i+j+BOM_INDEX}'
                    mark1 = check_list_content(results,ELEMENT1)
                    if mark1 == 0:
                        results.append(ELEMENT1)
                    mark2 = check_list_content(results,ELEMENT2)
                    if mark2 == 0:
                        # results.append(f'{i+j+BOM_INDEX}:{LIST[i+j]}')
                        results.append(ELEMENT2)
    return results
