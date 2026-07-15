common_ports = {
    21:  "FTP",
    22:  "SSH",
    23:  "Telnet",
    25:  "SMTP",
    53:  "DNS",
    80:  "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306:"MySQL",
    3389:"RDP",
    8080:"HTTP-Alt"
}
if 520 in common_ports:
    print("yes")
else:
    print("no")



























# for item in raw_Data:
#         if ord(item) != 32:
#             no = ord(item) + encoding_no
#             if no>=123:
#                 char = ord(item)
#                 new+no = 90 + (encoding_no-(122-char))
#             final_list.append(chr(no))
#         else:
#             final_list.append(chr(32))
#     print("".join(final_list))