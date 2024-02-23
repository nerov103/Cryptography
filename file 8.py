firststr = "Hello"
scendstr = "Javps"

stn = "Hello Wolrd"
trans = stn.maketrans(firststr, scendstr)
print(trans)

convet = stn.translate(trans)
print(convet)
