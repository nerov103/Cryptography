#codecs 
#ROT13 Algorithm
import string

def rot13():
    lowletter = string.ascii_lowercase
    upletter = string.ascii_uppercase
    shift_Key = 13    
    shift_lower = lowletter[shift_Key:] + lowletter[:shift_Key]
    shift_uper = upletter[shift_Key:] + upletter[:shift_Key]

    translator = str.maketrans(lowletter + upletter, shift_lower + shift_uper)
    return translator


def rot_13(message):
    table = rot13()
    return message.translate(table)


def main():
    user_input = input("Your Mess:")
    encrypted_mess = rot_13(user_input)
    print(f"Encrypted message: {encrypted_mess}")
    decrypted_message = rot_13(encrypted_mess)
    print(f"Decryped message:{decrypted_message}")


main()
