"""
Check to see whether a string is the reverse of another.
If it is, print YES, otherwise, print NO.
"""

word1 = input()
word2 = input()


# We could just reverse one of the words and check if they're both equal, but that is worse when the words are large.
# Loop backwards to see whether all characters match their mirror.
def reverseEqual(word1, word2):

    length = len(word1)
    
    # If words aren't the same length, there's no chance the two are mirrors.
    if length != len(word2):
        return False

    # They could be mirrors, so individually check each character.
    for i in range(0, len(word1)):
        if word1[i] != word2[length - i - 1]:
            return False
    return True


print('YES' if reverseEqual(word1, word2) else 'NO')
