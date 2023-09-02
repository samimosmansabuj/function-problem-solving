# Write a Python program to print the even numbers from a given list.

enter_range = int(input("Enter Range: "))

def even_num_list(input_range):
    '''this function using for list even number
    and this function accept 1 parameter'''
    even_num_list = []
    for i in range(1,input_range+1):
        if i%2==0:
            even_num_list.append(i)
    return (even_num_list)

def sum_even_num(input_range):
    '''this function using for sum even number
    and this function accept 1 parameter'''
    sum_even_num = 0
    for i in range(1,input_range+1):
        if i%2==0:
            sum_even_num+=i
    return (sum_even_num)

even_num_list(enter_range)
sum_even_num(enter_range)

print(f"All even numbers from (1 - {enter_range}): ", even_num_list(enter_range))
print(f"sum of all even numbers from (1 - {enter_range}): ", sum_even_num(enter_range))




