import pyinputplus as co


def encoding():
    final_list = []
    message = co.inputStr("Enter your message here for encoding: ")
    encoding_no = co.inputInt("Enter the no by which you'll like to encode: ", min=1, max=25)

    raw_Data = list(message)

    for item in raw_Data:

        if ord(item) == 32:
            final_list.append(chr(32))

        elif ord(item) in range(97, 123):
            no = ord(item) + encoding_no

            if no >= 123:
                char = ord(item)
                new_no = 97 + (encoding_no - (122 - char))
                final_list.append(chr(new_no))
            else:
                final_list.append(chr(no))

        elif ord(item) in range(65, 91):
            no = ord(item) + encoding_no

            if no >= 91:
                char = ord(item)
                new_no = 65 + (encoding_no - (90 - char))
                final_list.append(chr(new_no))
            else:
                final_list.append(chr(no))

        else:
            final_list.append(item)

    print("".join(final_list))


def decoding():
    final_list = []

    message = co.inputStr("Enter your message here for decoding: ")
    encoding_no = co.inputInt("Enter the number by which it was encoded: ", min=1, max=25)

    raw_Data = list(message)

    for item in raw_Data:

        if ord(item) == 32:
            final_list.append(chr(32))

        elif ord(item) in range(97, 123):
            no = ord(item) - encoding_no

            if no < 97:
                char = ord(item)
                new_no = 122 - (encoding_no - (char - 97))
                final_list.append(chr(new_no))
            else:
                final_list.append(chr(no))

        elif ord(item) in range(65, 91):
            no = ord(item) - encoding_no

            if no < 65:
                char = ord(item)
                new_no = 90 - (encoding_no - (char - 65))
                final_list.append(chr(new_no))
            else:
                final_list.append(chr(no))

        else:
            final_list.append(item)

    print("".join(final_list))


choice = co.inputMenu(["encoding", "decoding"])

if choice == "encoding":
    encoding()
elif choice == "decoding":
    decoding()

print("Thanks for using me!")