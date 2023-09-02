# Write a Python function to check whether a number is "Perfect" or not.
# Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.

enter_num = int(input("Enter a Number: "))
def check_perfect_num(input_num):
    sum_num = 0
    for i in range(1, input_num):
        if input_num%i==0:
            sum_num+=i
    if sum_num==input_num:
        return "This is perfect Number!"
    else:
        return "This is not a perfect Number!"

print(check_perfect_num(enter_num))
