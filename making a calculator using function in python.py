_1st_number = float(input("Enter a First Number: "))
select_operator = input("Enter Operator(+, -, *, / or %): ")
_2nd_number = float(input("Enter a Second Number: "))
def calculator(_1st_number, select_operator, _2nd_number):
    if select_operator=="+":
        equalation = _1st_number + _2nd_number
    elif select_operator=="-":
        equalation = _1st_number - _2nd_number
    elif select_operator=="*":
        equalation = _1st_number * _2nd_number
    elif select_operator=="/":
        equalation = _1st_number / _2nd_number
    elif select_operator=="%":
        equalation = _1st_number % _2nd_number
    else:
        equalation = "Wrong Input"
    return equalation
#comment
print(calculator(_1st_number, select_operator, _2nd_number))
