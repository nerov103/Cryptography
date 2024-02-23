#Transposition Cipher
plintxt = "No good deed will go unpunished"
key = 8
nonelist = [""]*key

for colam in plintxt:
    pointer = colam

    while pointer < len(plintxt):
        nonelist[colam] += nonelist[pointer]
        pointer += key






