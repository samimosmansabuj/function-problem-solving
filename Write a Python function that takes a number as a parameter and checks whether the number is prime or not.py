# Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

enter_num = int(input("Enter a prime number: "))

#-----------------------------------step 01 using for loop----------------------------------------------
def check_prime_01(input_num):
    ''' Check the number is prime or not using for loop'''
    if input_num == 0 or input_num == 1:
        return "This is not a prime number!"
    else:
        verify_number = 0
        for i in range(2, input_num):
            if input_num%i==0:
                verify_number+=1
        return verify_number==0
print(check_prime_01(enter_num))

#-----------------------------------step 02 using while loop----------------------------------------------
def check_prime_02(input_num):
    ''' Check the number is prime or not using while loop'''
    if input_num == 0 or input_num == 1:
        return "This is not a prime number!"
    else:
        verify_number = 0
        start_range = 2
        while start_range<input_num:
            if input_num%start_range==0:
                verify_number+=1
            start_range+=1
        return verify_number==0
print(check_prime_02(enter_num))

#-----------------------------------Check Function details(comment)----------------------------------------------
print()
print("check_prime_01 function using for ", check_prime_01.__doc__)
print("check_prime_02 function using for ", check_prime_02.__doc__)

