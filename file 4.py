import string

def rot13():
    lowletter = string.ascii_lowercase
    upletter = string.ascii_uppercase
    shift_Key = 13
     
    shift_letter = lowletter[shift_Key:] + lowletter[:shift_Key]
    print(shift_letter)

    

rot13()

