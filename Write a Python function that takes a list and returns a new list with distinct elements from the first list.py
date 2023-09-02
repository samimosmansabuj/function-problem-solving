# Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

my_list = [1,2,3,3,3,3,4,5]
def unique_con_normallist(input_list):
    unique_list = []
    for i in input_list:
        if i not in unique_list:
            unique_list.append(i)
        else:
            pass
    return unique_list
print(unique_con_normallist(my_list))








