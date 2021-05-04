from sys import stdin
from pathlib import Path

sample1 = r'C:\Users\ncssa\PycharmProjects\dreamWork\sample-1.txt'
sample2 = r'C:\Users\ncssa\PycharmProjects\dreamWork\sample-2.txt'
sample3 = r'C:\Users\ncssa\PycharmProjects\dreamWork\sample-3.txt'
sample4 = r'C:\Users\ncssa\PycharmProjects\dreamWork\sample-4.txt'

print("press enter to use 'sys.stdin'")
for line in stdin:
    if 'exit' == line.strip():
        print("Thank you. Found exit. Terminating the program.")
        exit(0)
    else:

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


        list1 = open_file(sample1)
        list2 = open_file(sample2)
        list3 = open_file(sample3)
        list4 = open_file(sample4)

        # call the decoder function
        decoded_list1 = decoder(list1)
        decoded_list2 = decoder(list2)
        decoded_list3 = decoder(list3)
        decoded_list4 = decoder(list4)

        print("sample list1: ", list1)
        print("decoded list1: ", decoded_list1, "\n")
        print("sample list2: ", list2)
        print("decoded list2: ", decoded_list2, "\n")

        print("sample list3: ", list3)
        print("decoded list3: ", decoded_list3, "\n")
        print("sample list4: ", list4)
        print("decoded list4: ", decoded_list4, "\n")

        # this function opens a new file and save the decoded list.
        def open_new_file(new_file, decoded_list):
            f = open(new_file, "a+")  # create/open a new txt file for the final result
            # write the decoded_list_1 in the text file.
            for i in decoded_list:
                f.write("%s " % i)
            f.close()

        # new file to save the decoded list
        new_file1 = "final-1.txt"
        new_file2 = "final-2.txt"
        new_file3 = "final-3.txt"
        new_file4 = "final-4.txt"

        # save decoded list in a new text file.
        open_new_file(new_file1, decoded_list1)
        open_new_file(new_file2, decoded_list2)
        open_new_file(new_file3, decoded_list3)
        open_new_file(new_file4, decoded_list4)
