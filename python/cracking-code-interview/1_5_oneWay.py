# 1_5
def oneEditAway():

    word1 = input("first word: ")
    word2 = input("second word: ")

    lenWord1 = len(word1)
    lenWord2 = len(word2)

    if abs(lenWord1 - lenWord2) > 1:
        return False

    numDiffChar = 0

    # Check which word is the smallest
    if lenWord1 < lenWord2:
        smallWord = 1
    elif lenWord1 > lenWord2:
        smallWord = 2
    # words have the same size
    else:
        smallWord = 0

    # Get the size of the smallest word
    y = lenWord1 if lenWord1 <= lenWord2 else lenWord2

    index1 = 0
    index2 = 0

    for i in range(y):

        if word1[index1] != word2[index2]:

            numDiffChar += 1

            # if word1 is smaller than word2
            if smallWord == 1:
                index1 += 1
                if index1+1 <= lenWord1:
                    if word1[index1] != word2[index2]:
                        return False
                else:
                    break

            # if word1 is larger than word2
            elif smallWord == 2:
                index2 += 1
                if index2 <= lenWord2:
                    if word1[index1] != word2[index2]:
                        return False
                else:
                    break

        index1 += 1
        index2 += 1

        if numDiffChar > 1:
            return False

    if lenWord1 == lenWord2 and numDiffChar == 0:
        return False
    else:
        return True


print(oneEditAway())