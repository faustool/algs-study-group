class Pair:
    key = ""
    value = 1


def hash_code(char, length):
    return ord(char) % length


def create_hash_table(length):
    hash_table = []
    for i in range(length):
        hash_table.append([])
    return hash_table


def find_pair(hash_table, char):
    pos = hash_code(char, len(hash_table))
    lst = hash_table[pos]
    for pair in lst:
        if pair.key == char:
            return pair
    return None


def save_pair(hash_table, char):
    pos = hash_code(char, len(hash_table))
    lst = hash_table[pos]
    pair = Pair()
    pair.key = char
    lst.append(pair)


def is_permutation_of_palindrome(string):
    string = string.upper()
    length = 5
    hash_table = create_hash_table(length)

    actual_size = 0

    for c in string:
        if c != ' ':
            actual_size += 1
            pair = find_pair(hash_table, c)
            if pair is None:
                save_pair(hash_table, c)
            else:
                pair.value += 1

    is_size_even = actual_size % 2 == 0
    odd_count = 0

    for list in hash_table:
        for pair in list:
            if pair.value % 2 != 0:
                odd_count += 1

    if is_size_even:
        return odd_count == 0
    else:
        return odd_count <= 1


assert is_permutation_of_palindrome("Tact Coa") is True
assert is_permutation_of_palindrome("aa") is True
assert is_permutation_of_palindrome("baa") is True
assert is_permutation_of_palindrome("cba") is False

