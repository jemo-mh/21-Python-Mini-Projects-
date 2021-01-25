text= str(input("entera string\n"))
text = text.split()
acronym =""
for i in text:
    # print(str(i[0]))
    acronym = acronym + str(i[0]).upper()
print(acronym)