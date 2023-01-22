def compare_list(List1, List2):
    comparison_results=[]
    for i in range(len(List1)):
        for j in range(len(List2)):
            if (List1[i] == List2[j]):
                comparison_results.append(List1[i])
    return comparison_results

def compare_quantity_to_reference(Reference_List, quantity_list,item_number):
    QTR_Results=[]
    t_Ref_List = str(Reference_List).split(',')
    length_Ref_List = len(t_Ref_List)

    # Return error list, format: [Item:reference count:quantity count]
    if (length_Ref_List != quantity_list):
        QTR_Results = f'{item_number+1}:{length_Ref_List}:{quantity_list}'
        return QTR_Results
    else:
        return False
