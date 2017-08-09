def unique_o_square():
    for i in range(len(string)):
        for j in range(len(string)):
            if i != j and string[i] == string[j]:
                return False
    return True

string = input("Insert string to test: ")
result_o_square = unique_o_square()

if result_o_square:
    print("String contains unique characters")
else:
    print("String contains repeated characters")