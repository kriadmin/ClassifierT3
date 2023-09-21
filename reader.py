s = ""

with open("classes.txt","r") as f:
    s = f.read()

classes = [set(x.split(",")) for x in s.replace("\n","").split("t")][0:-1]

print(len(classes))