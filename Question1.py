#demonstrate the use case of exception handling

try:
    f = open("testfile.txt")
except FileNotFoundError as et:
    print(et)
except Exception as et:
    print(et)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally..")
