def encript(value:str)->list:
    lst_val = [*value]

    a_val = ord("a")
    z_val = ord("z")
    A_val = ord("A")
    Z_val = ord("Z")

    for i in range(len(lst_val)):
        temp_val = lst_val[i]
        if (ord(temp_val)>=a_val and ord(temp_val)<=z_val):
            new_l = ord(temp_val)-a_val
            new_l += 13
            new_l %= 26
            temp_val = chr(new_l+a_val)
        elif (ord(temp_val)>=A_val and ord(lst_val[i])<=Z_val):
            new_l = ord(temp_val)-A_val
            new_l += 13
            new_l %= 26
            temp_val = chr(new_l+A_val)
        lst_val[i] = temp_val
    return "".join(lst_val)


if __name__ == "__main__":
    value = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}"
    encripted_value = encript(value)
    print(encripted_value)
