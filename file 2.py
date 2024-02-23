#new ima createa  the same program use python for loop

message = 'This is program to explain reverse cipher.'
translated = ''


for i in range(len(message)-1, -1, -1):
    translated +=message[i]

print(translated)




