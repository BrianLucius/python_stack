def values_greater_than_second(number_list):
    if len(number_list) <= 2:
        return False
    
    filtered_list = []
    for x in range(len(number_list)):
        if number_list[x] > number_list[1]:
            filtered_list.append(number_list[x])
    print(len(filtered_list))
    return filtered_list

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))