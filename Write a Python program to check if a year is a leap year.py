#Write a Python program to check if a year is a leap year.

enter_year = int(input("Enter a year: "))

def check_leap_y(input_year):
    # print(input_year)
    # result = ''
    if input_year%4==0:
        result = "This is leap year!"
        if input_year%100==0:
            result = "This is not a leap year!"
            if input_year%400==0:
                result = "This is leap year!"
            else:
                result = "This is not a leap year!"
        else:
            result = "This is a leap year!"
    else:
        result = "This is not a leap year!"
    return result
    
print(check_leap_y(enter_year))
