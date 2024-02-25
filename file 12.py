from cryptography.fernet import Fernet

  


key = Fernet(Fernet.generate_key())

with open("simple.txt", "rb") as plintxt:
    cipertxt = plintxt.read()

with open("simple.txt", "wb") as file:
    k = key.encrypt(file)
    print(k)

    




