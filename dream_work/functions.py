from pathlib import Path


# these are a functions for the decoder.
def open_file(file_name):
    # assign data to "text"
    dataFolder = Path(file_name)
    text = dataFolder.read_text()
    # split string to a list
    list_opened = text.rsplit(" ")
    return list_opened


# this is the decoder function
def decoder(work):
    number = 0  # int variable to store converted numbers - temporary
    new_list = []  # This is a new list to hold the decoded numbers
    for num in work:
        number += int(num)
        new_list.append(number)
    return new_list


# this function opens a new file and save the decoded list.
def open_new_file(new_file, decoded_list):
    f = open(new_file, "a+")  # create/open a new txt file for the final result
    # write the decoded_list_1 in the text file.
    for i in decoded_list:
        f.write("%s " % i)
    f.close()
