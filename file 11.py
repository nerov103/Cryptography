from cryptography.fernet import MultiFernet, Fernet

plintxt = input("Plintxt: ")

key1 = Fernet(Fernet.generate_key())
key2 = Fernet(Fernet.generate_key())
multiKEY = MultiFernet([key1, key2])

massge = plintxt.encode()

token = multiKEY.encrypt(massge)

print(token)

print(multiKEY.decrypt(token).decode())



