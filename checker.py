def compare_list(List1,List2):
    comparison_results = []
    for i in range(len(List1)):
        for j in range(len(List2)):
            if (List1[i] == List2[j]):
                comparison_results.append(List1[i])
    return comparison_results

# sample_list = ['C1','C2','C3']
# sample_quantity = 2

def compare_quantity_to_reference(Reference_List,Quantity_List):
    compare_QTR_results = []
    t_Ref_List = Reference_List.split(',')

    if (len(t_Ref_List) != Quantity_List):
        return True
    else:
        return False
