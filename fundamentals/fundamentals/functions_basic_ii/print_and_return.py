def print_and_return(values_list):
    print("Printing: " + str(values_list[0]))
    return(values_list[1])
    
print("Returned: " + str(print_and_return([1,2])))