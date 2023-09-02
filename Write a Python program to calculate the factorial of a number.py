# 5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

f_num = int(input("Enter a factorial range: "))
def factorial_num(input_num):
    if input_num == 0:
        return 1
    else:
        return input_num*factorial_num(input_num-1)
print(factorial_num(f_num))
