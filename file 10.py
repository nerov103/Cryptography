from cryptography.fernet import Fernet

user_txt = input("Your Mess: ")

key = Fernet.generate_key()
f = Fernet(key)

token = f.encrypt(user_txt.encode())
print(token)

decode = f.decrypt(token)
print(decode.decode())


