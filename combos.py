combos = set()

i = ""
while i != "exit":
    i = input("(L/B): ")
    try:
        combos.add((int(i[0]), int(i[2])))
    except:
        print("invalid")

print(combos)
