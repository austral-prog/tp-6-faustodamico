# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    result = []
    for i in range(len(list_to_remove_elements)):
        if i != 0 and i != 4 and i != 5:
            result.append(list_to_remove_elements[i])
    return result

def add_elements(list_to_add_elements):
    result = []
    result.append('Pink') 
    for item in list_to_add_elements:
        result.append(item)
    result.append('Yellow')  
    return result

def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    else:
        return False
        
def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) > 2 and len(list_to_compare2) > 2:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
    return False

def list_of_lists(list_of_lists_to_modify):
    result = []
    primera = list_of_lists_to_modify[0][:2]
    result.append(primera)
    segunda = list_of_lists_to_modify[1][1:4]
    result.append(segunda)
    tercera = list_of_lists_to_modify[2][-2:]
    result.append(tercera)
    return result
