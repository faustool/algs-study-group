string = input("Insert string to test: ")

for i in range(len(string)):
    for j in range(len(string)):
        if i != j and string[i] == string[j]:
            print("string contains repeated characters")
            exit(1)

print("string contains unique characters")
