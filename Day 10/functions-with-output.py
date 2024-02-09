def my_function():
    result = 3 * 2
    return result

def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs."
    else:
        fullname = (first_name + ' ' + last_name).title()
        return fullname
    

f_name = 'rune'
l_name = 'faaberg'

print(format_name(input("What is your first name? "), input("What is your last name? ")))


output = my_function()

print(output)
print(my_function())