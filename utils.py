# Print an array or a list into a file
# ARGS:
#   file: the file object returned by the function open()
#   title: a string to print on top of the array
#   array: array or list to print on the file
#   no_punctuation: can be True only when the array contains Strings and
#                   is used to eliminate "\n", "\r", "\t" from the strings that you're printing
def print_array_file(file, title, array, no_punctuation=None):
    file.write("\n" + title + ":\n")
    for i in array:
        if no_punctuation is None:
            file.write("\t- " + str(i) + "\n")
        else:
            file.write("\t- " + str(i).replace("\n", "").replace("\t", "").replace("\r", "") + "\n")


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
#   no_punctuation: can be different from None only when the variable is a string and
#                   is used to eliminate "\n", "\r", "\t" from the string that you're printing
def print_var_file(file, title, value, no_punctuation=None):
    if no_punctuation is None:
        file.write("\n" + title + ": " + str(value) + "\n")
    else:
        file.write("\n" + title + ": " + str(value).replace("\n", "").replace("\t", "").replace("\r", "") + "\n")
