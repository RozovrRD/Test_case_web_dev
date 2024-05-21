from itertools import product


operands = ['', '+', '-']

for oper_pos in list(product(*[operands for _ in range(9)])):
    current_string = f'9{oper_pos[0]}8{oper_pos[1]}7{oper_pos[2]}6{oper_pos[3]}5{oper_pos[4]}4{oper_pos[5]}3{oper_pos[6]}2{oper_pos[7]}1{oper_pos[8]}0'
    result = eval(current_string)
    if result == 200:
        print(current_string, '=', result)
