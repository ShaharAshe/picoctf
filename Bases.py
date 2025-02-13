import base64

def convert(value:str)->str:
    return base64.b64decode(value).decode('utf-8')


if __name__ == "__main__":
    value:str = 'bDNhcm5fdGgzX3IwcDM1'
    res:str = convert(value)
    print('picoCTF{'+res+'}')
