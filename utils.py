# Print an array or a list into a file
# ARGS:
#   file: the file object returned by the function open()
#   title: a string to print on top of the array
#   array: array or list to print on the file
#   no_punctuation: can be True only when the array contains Strings and is used to eliminate "\n", "\r", "\t"
#                   from the strings to be printed, when no_puntuation is None the array is printed normally
def print_array_file(file, title, array, no_punctuation=None):
    file.write("\n" + title + ":\n")
    for element in array:
        if no_punctuation is None:
            file.write("\t- " + str(element) + "\n")
        else:
            file.write("\t- " + str(element).replace("\n", "").replace("\t", "").replace("\r", "") + "\n")


# Print a dictionary into a file
# ARGS:
#   file: the file object returned by the function open()
#   title: a string to print on top of the dictionary
#   dictionary: dictionary to print on the file
#   no_punctuation: can be True only when the dictionary value are Strings and is used to eliminate "\n", "\r", "\t"
#                   from the strings to be printed, when no_puntuation is None the dictionary is printed normally
def print_dict_file(file, title, dictionary, no_punctuation=None):
    file.write("\n" + title + ":\n")
    for keys, values in dictionary.items():
        if no_punctuation is None:
            file.write("\t- " + str(keys) + ": " + str(values) + "\n")
        else:
            file.write("\t- " + str(keys) + ": " + str(values).replace("\n", "").replace("\t", "").replace("\r", "") + "\n")


# Print a value into a file
# ARGS:
#   file: the file object returned by the function open()
#   title: a string to print before of the variable named value
#   value: variable to print on the file
#   no_punctuation: can be True only when the variable is a Strings and is used to eliminate "\n", "\r", "\t"
#                   from the strings to be printed, when no_puntuation is None the variable is printed normally
def print_var_file(file, title, value, no_punctuation=None):
    if no_punctuation is None:
        file.write("\n" + title + ": " + str(value) + "\n")
    else:
        file.write("\n" + title + ": " + str(value).replace("\n", "").replace("\t", "").replace("\r", "") + "\n")
