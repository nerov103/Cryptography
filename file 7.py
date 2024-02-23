# first string

table = str.maketrans("abc", "xyz")
text = "hello world"
translated_text = text.translate(table)
print(translated_text)  # আউটপুট: "xzyyx ooyzld"
