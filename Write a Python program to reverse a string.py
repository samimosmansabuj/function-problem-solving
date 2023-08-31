# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def reverse_string_01(string01):
    # reverse_string_01 = string01[::-1]
    return string01[::-1]
    
print(reverse_string_01("1234abcd"))

def reverse_string_02(string02):
    reverse_string02 = ""
    string02_len = len(string02)
    while string02_len>0:
        reverse_string02+= string02[string02_len-1]
        string02_len-=1
    return reverse_string02
print(reverse_string_02("dcba4321"))
