def position(word):
    if len(word)>1:
        pos = 0
        for idx, letter in enumerate(word[::-1]):
            pos += (position(letter)+(1 if idx!=0 else 0))*26**(idx)
        return pos
    return ord(word.lower()) - 97


print(position("A")) --> 0
print(position("AA")) --> 26
print(position("AZ")) --> 51