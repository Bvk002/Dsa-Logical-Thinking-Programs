s = input()
cd = False
for char in s:
    if char.isdigit():
        cd = True
if cd:
    print("Valid Password")
else:
    print("Invalid Password")