def remove_dots1(string):
    return string.replace(".", "")

def add_dots1(input_string):
    dots = "." * (len(input_string)-1) + " "
    zip_arr = [first + second for first, second in zip(input_string, dots)]
    result_string = "".join(zip_arr)
    return result_string.strip()

def remove_dots(string):
    return remove_dots1(string)

def add_dots(string):
    return add_dots1(string)


