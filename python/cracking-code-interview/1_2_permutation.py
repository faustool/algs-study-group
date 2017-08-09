def permutation_o_n_square():
    equals = 0
    for ci in string_1:
        for cj in string_2:
            if ci == cj:
                equals += 1
    return equals == len(string_1)


string_1 = input("Inform the first String: ")
string_2 = input("Inform the second String: ")

if len(string_1) != len(string_2):
    print("Both Strings should have the same length, doh!")
    exit(1)

if permutation_o_n_square():
    print("The second String IS a permutation of the first")
else:
    print("The second String is NOT a permutation of the first")