# first string

# first string
firstString = "abc"
secondString = "ghi"
thirdString = "ab"

string = "abcdef"
print("Original string:", string)

tranlsation = string.maketrans(firstString, secondString)
print(tranlsation)
print("Translated string:",string.translate(tranlsation))
