# Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

enter_string = "Python is The Best Problem Language!"
def check_uplow_case(input_string):
    result_dict = {"upper_case":0, "lower_case":0}
    for i in input_string:
        if i.isupper():
            result_dict["upper_case"]+=1
        elif i.islower():
            result_dict["lower_case"]+=1
        else:
            pass
    return result_dict
print(f"""No. of Upper case characters : {check_uplow_case(enter_string)["upper_case"]}
No. of Lower case Characters : {check_uplow_case(enter_string)["lower_case"]}
""")











