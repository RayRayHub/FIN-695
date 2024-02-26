email= "John.Smith@uky.edu"
names=email.split("@")
print(names)
firstlast=names[0].split(".")
print("last name is", firstlast[1])