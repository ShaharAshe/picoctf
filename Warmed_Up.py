convert_map:dict[int] = {
        1:1,
        2:2,
        3:3,
        4:4,
        5:5,
        6:6,
        7:7,
        8:8,
        9:9,
        'A':10,
        'B':11,
        'C':12,
        'D':13,
        'E':14,
        'F':15,
        'a':10,
        'b':11,
        'c':12,
        'd':13,
        'e':14,
        'f':15
    }


def convert(value:int)->int:
    if len(value) == 0:
        return 0
    if value[0] == 'O' or value[0] == 'o':
        if 1<len(value) and (value[1] == 'x' or value[1] == 'X'):
            value = value[2:]
        else:
            value = value[1:]
    power_of_16:int = 1
    res:int = 0
    for i in (range(len(value)-1, -1, -1)):
        val = int(value[i]) if value[i].isdigit() else value[i]
        res += convert_map[val]*power_of_16
        power_of_16 *= 16
    return res


if __name__ == "__main__":
    value:str = 'Ox3D'
    try:
        res:int = convert(value)
    except:
        print("Error in input")
        exit()
    print('picoCTF{'+str(res)+'}')
