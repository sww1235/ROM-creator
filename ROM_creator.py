__author__ = 'Stephen'

import os.path
def switchNumber(least='0', middle='0', most='0'):
    arguments = [most, middle, least]
    #  print(arguments)
    list_returned = ['40'] * 3
    for i, j in enumerate(arguments):
        # print('' + str(i) + '+' + j)
        j = int(j)
        if j == 0:
            list_returned[i] = '40'  # 0 case
        elif j == 1:
            list_returned[i] = '79'  # 1 case
        elif j == 2:
            list_returned[i] = '24'  # 2 case
        elif j == 3:
            list_returned[i] = '30'  # 3 case
        elif j == 4:
            list_returned[i] = '19'  # 4 case
        elif j == 5:
            list_returned[i] = '12'  # 5 case
        elif j == 6:
            list_returned[i] = '03'  # 6 case
        elif j == 7:
            list_returned[i] = '78'  # 7 case
        elif j == 8:
            list_returned[i] = '00'  # 8 case
        elif j == 9:
            list_returned[i] = '18'  # 9 case
        # print(list_returned[i])
    temp = ''
    for j in range(len(list_returned)):
        temp += list_returned[j]
    # print(list_returned)
    return list_returned


begining = ["-- Copyright (C) 1991-2010 Altera Corporation\n",
            "-- Your use of Altera Corporation's design tools, logic functions\n",
            "-- and other software and tools, and its AMPP partner logic\n",
            "-- functions, and any output files from any of the foregoing\n",
            "-- (including device programming or simulation files), and any\n",
            "-- associated documentation or information are expressly subject\n",
            "-- to the terms and conditions of the Altera Program License\n",
            "-- Subscription Agreement, Altera MegaCore Function License\n",
            "-- Agreement, or other applicable license agreement, including,\n",
            "-- without limitation, that your use is for the sole purpose of\n",
            "-- programming logic devices manufactured by Altera and sold by\n",
            "-- Altera or its authorized distributors.  Please refer to the\n",
            "-- applicable agreement for further details.\n",
            "\n",
            "-- Quartus II generated Memory Initialization File (.mif)\n",
            "\n",
            "WIDTH=24;\n",
            "DEPTH=256;\n",
            "\n",
            "ADDRESS_RADIX=HEX;\n",
            "DATA_RADIX=HEX;\n",
            "\n",
            "CONTENT\n",
            "BEGIN\n"]
stringBuilder = {}
for i in range(256):
    word = str(i)
    if len(word) > 2:
        #  print(word[0] + ':' + word[1] + ':' + word[2])
        stringBuilder[i] = switchNumber(word[2], word[1], word[0])
    elif len(word) == 2:
        #  print(word[0] + ':' + word[1])
        stringBuilder[i] = switchNumber(word[1], word[0])
    elif len(word) == 1:
        #  print(word[0])
        stringBuilder[i] = switchNumber(word[0])
# print(stringBuilder)

mif = 0
newLines = []
if mif == 1:
    with open('test.txt', 'w') as f:
        f.writelines(begining)
        for k, v in stringBuilder.items():
            f.write('0' + hex(k)[2:].zfill(2).upper() + '  :  ' + ''.join(v) + ';\n')
        f.write("END;")
    print(f.closed)
elif mif == 0:
    with open(os.path.expanduser('~/Copy/School_Work/School_Work_2015-2016/ECE102/Labs/Lab_7/ROM_Contents.csv'), 'w') as f:
        f.write(',0,+1,+2,+3,+4,+5,+6,+7\n')
        for k, v in stringBuilder.items():
            if (k + 1) % 8 == 0:
                f.write(' '.join(v) + '\n')
            elif k % 8 == 0:
                f.write(str(k//8)+','+ ' '.join(v) + ',')
            else:
                f.write(' '.join(v) + ',')

    print(f.closed)
