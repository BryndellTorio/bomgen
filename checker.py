def compare_list(List1, List2):
    comparison_results=[]
    for i in range(len(List1)):
        for j in range(len(List2)):
            if (List1[i] == List2[j]):
                comparison_results.append(List1[i])
    return comparison_results

def compare_quantity_to_reference(Reference_List, Quantity_List):
    QTR_Results=[]
    t_Ref_List = str(Reference_List).split(',')
    length_Ref_List = len(t_Ref_List)

    if (length_Ref_List != Quantity_List):
        QTR_Results.append(f'refCnt={length_Ref_List}:qtyCnt={Quantity_List}')
        return QTR_Results
    else:
        return False
