from cryptography.fernet import Fernet

ky = Fernet.generate_key()
with open("Key.txt", 'wb') as k:
    k.write(ky)


with open("file.txt", 'rb') as fl:
    contents = fl.read()
contents_encrypted = Fernet(ky).encrypt(contents)


with open("file.txt", 'w') as en:
    en.write(contents_encrypted.decode())


decodeplintxt = Fernet(ky).decrypt(contents)


