def convert(value:int)->str:
    res = ''
    while value != 0:
        res = str(value%2)+res
        value //= 2
    return res

if __name__ == "__main__":
    value:int = 42
    res:str = convert(value)
    print('picoCTF{'+res+'}')
