def unique_o_n_square():
    for i in range(len(string)):
        for j in range(len(string)):
            if i != j and string[i] == string[j]:
                return False
    return True


def unique_o_n():
    hash_table = []
    for i in range(20):
        hash_table.append([])

    for c in string:
        hash_code = ord(c) % len(hash_table)
        hash_list = hash_table[hash_code]
        for list_item in hash_list:
            if c == list_item:
                return False
        hash_list.append(c)

    return True


string = input("Insert string to test: ")
result_o_n_square = unique_o_n_square()
result_o_n = unique_o_n()

if result_o_n != result_o_n_square:
    print("This bad program could not make its mind about the answer, sorry :[")
    exit(1)

if result_o_n_square:
    print("String contains unique characters")
else:
    print("String contains repeated characters")
