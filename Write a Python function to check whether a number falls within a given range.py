#  Write a Python function to check whether a number falls within a given range.

enter_num = int(input("Enter a Number: "))
def check_number(input_num):
    if input_num in range(1,10):
        print("%s is in the range!" %(input_num))
    else:
        print("%s is outside the given range!" %(input_num))
check_number(enter_num)
