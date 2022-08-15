file = input().split("\\")
name = ""
extension = ""
for f in file:
    if "." in f:
        f = f.split(".")
        name = f[0]
        extension = f[1]
print(f"File name: {name}")
print(f"File extension: {extension}")
