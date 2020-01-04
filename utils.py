# Print an array or a list into a file
# ARGS:
#   file: the file object returned by the function open()
#   title: a string to print on top of the array
#   array: array or list to print on the file
def print_array_file(file, title, array):
    file.write("\n" + title + ":\n")
    for i in array:
        file.write("\t- " + str(i) + "\n")


# Print a dictionary into a file
# ARGS:
#   file: the file object returned by the function open()
#   title: a string to print on top of the dictionary
#   dictionary: dictionary to print on the file
def print_dict_file(file, title, dictionary):
    file.write("\n" + title + ":\n")
    for keys, values in dictionary.items():
        file.write("\t- " + str(keys) + ": " + str(values) + "\n")


# Print a value into a file
# ARGS:
#   file: the file object returned by the function open()
#   title: a string to print before of the variable named value
#   value: variable to print on the file
def print_var_file(file, title, value):
    file.write("\n" + title + ": " + str(value) + "\n")
