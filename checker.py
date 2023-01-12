def compare_list(List1,List2):
    comparison_results = []
    for i in range(len(List1)):
        for j in range(len(List2)):
            if (List1[i] == List2[j]):
                comparison_results.append(List1[i])
    return comparison_results

# sample_Data = ['C1','C2','C3']
# sample_quantity = 2

def compare_quantity_to_reference(Reference_List,Quantity_List):
    compare_QTR_results = []
    t_Ref_List = str(Reference_List).split(',')
    length_Ref_List = len(t_Ref_List)

    if (length_Ref_List != Quantity_List):
        compare_QTR_results.append(f'refLength={length_Ref_List}:quantity={Quantity_List}')
        return compare_QTR_results
    else:
        return False
