#first example
# string = "abcdef"
# dict1 = {"a":"1", "b":"2", "c":"3"}
# data = string.maketrans(dict1)
# print(data)

#scend example

# sometxt = "Hello World! ima love python"
# dicx = {"a":"1", "b":"2", "c":"3", "d":"4"}
# tabel = sometxt.maketrans(dicx)
# print(tabel)

#three example
# main_txt = "Hacking not a crime!" 
# str_one = "abcde"
# str_tow = "12345"
# b = main_txt.maketrans(str_one, str_tow)
# print(b)

#fore explem 
main_str = "i love my contry(@^"
str1 = "abcde"
str2 = "12345"
str3 = "(@^"
ex = main_str.maketrans(str1,str2,str3)
b = main_str.translate(ex)
print(b)


