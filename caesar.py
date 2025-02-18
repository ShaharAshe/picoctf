def most_common(strI: str):
    str_list = [s for s in strI if s != ' ']
    return (str_list, max(str_list, key=str_list.count))


def cipher(strI: str):
    str_list, mC = most_common(strI)
    print("\n===========================================================")
    print("_________________________________")
    print(f"Now we will analyze the message encripted")
    print("_________________________________")
    print(f"The most common letter in the cipher is: {mC}", end="\n\n")
    re_list = []
    letter_frequency = ["e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p", "b", "v", "k", "j", "x", "q", "z"]

    for aBi in range(len(letter_frequency)):
        print(f"More {len(letter_frequency)-(aBi+1)} possible messages left\n")
        distunce = ((ord(mC.lower()) - ord(letter_frequency[aBi])) % 26)
        if distunce >= 0:
            re_list = " ".join([str(chr(((ord(s) - ord("a") - distunce) % 26) + ord('a'))) for s in str_list])
            print(f"Possible messages for {letter_frequency[aBi]}:\n {re_list}\n")
            ans = input("Is this the correct message? (y/n): ")
            while ans not in ['y', 'n']:
                print("---------------------------------\n*** Invalid answer, please try again ***\n---------------------------------")
                ans = input("Please enter a valid answer (y/n): ")
            if ans == 'n':
                continue
            else:
                print(f"The most common letter in the cipher is: {mC}", end="\n\n")
                print("=================================")
                print(f"The message is encripted with the Shift code:")
                print(f"e(x) = x+{distunce} mod26")
                print("---------------------------------")
                print(f"And copying the decoding is:")
                print(f"d(y) = y-{distunce} = y+{26 - distunce} mod26")
                print("=================================", end="\n\n")
                print()
                print("The key: picoCTF{",end='')
                for c in re_list:
                    print(c.strip(),end='')
                print("}")
                return True
    return False


if __name__ == "__main__":
    M1 = "dspttjohuifsvcjdpoabrkttds"
    
    cipher(M1)
    
    print("\n=================================")
    print("           Goodbye!")
    print("=================================")
