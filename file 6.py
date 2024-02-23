import string



# dict = {"a" : "123", "b" : "456", "c" : "789"}
# stre = "abc"
# print(stre.maketrans(dict))

# dice = {97: '123', 98: '456', 99: '789'}
# stre = "abc"
# print(stre.maketrans(dice))


# firststrint  = "abc"
# seconstring = "def"

# print(str.maketrans(firststrint, seconstring))

one_str = "abcy"
tow_str = "defg"
thirdstr = "abcg"
print(str.maketrans(one_str, tow_str, thirdstr))

