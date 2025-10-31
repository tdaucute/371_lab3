file1 = "penguin.jpg"
file2 = "penguin_decrypted.jpg"

with open(file1, "rb") as f1, open(file2, "rb") as f2:
    data1 = f1.read()
    data2 = f2.read()

if data1 == data2:
    print("Files are exactly the same!")
else:
    print("Files are different.")


