from sys import stdin
from dream_work.file_to_use import *
from dream_work.functions import open_file, decoder, open_new_file

print("Please, press enter to use the decoder.")
for line in stdin:
    if 'exit' == line.strip():
        print("Thank you. Found exit. Terminating the program.")
        exit(0)
    else:
        # assign data to a list
        list1 = open_file(sample1)
        list2 = open_file(sample2)
        list3 = open_file(sample3)
        list4 = open_file(sample4)

        # call the decoder function
        decoded_list1 = decoder(list1)
        decoded_list2 = decoder(list2)
        decoded_list3 = decoder(list3)
        decoded_list4 = decoder(list4)

        # display the result
        print("sample list1: ", list1, "\ndecoded list1: ", decoded_list1, "\n")
        print("sample list2: ", list2, "\ndecoded list2: ", decoded_list2, "\n")
        print("sample list3: ", list3, "\ndecoded list3: ", decoded_list3, "\n")
        print("sample list4: ", list4, "\ndecoded list4: ", decoded_list4, "\n")

        # save decoded list in a new text file.
        open_new_file(new_file1, decoded_list1)
        open_new_file(new_file2, decoded_list2)
        open_new_file(new_file3, decoded_list3)
        open_new_file(new_file4, decoded_list4)
    print("Please, type in 'exit' to terminate the program. Or press enter to continue.")
