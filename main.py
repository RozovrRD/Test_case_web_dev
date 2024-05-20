operand_map = {
    0: '',
    1: '-',
    2: '+'
}

base_string = list('9_8_7_6_5_4_3_2_1_0')

for index1 in range(3):
    for index2 in range(3):
        for index3 in range(3):
            for index4 in range(3):
                for index5 in range(3):
                    for index6 in range(3):
                        for index7 in range(3):
                            for index8 in range(3):
                                for index9 in range(3):
                                    base_string[1] = operand_map[index1]
                                    base_string[3] = operand_map[index2]
                                    base_string[5] = operand_map[index3]
                                    base_string[7] = operand_map[index4]
                                    base_string[9] = operand_map[index5]
                                    base_string[11] = operand_map[index6]
                                    base_string[13] = operand_map[index7]
                                    base_string[15] = operand_map[index8]
                                    base_string[17] = operand_map[index9]

                                    result = eval("".join(base_string))
                                    if result == 200:
                                        print("".join(base_string), '=', result)
