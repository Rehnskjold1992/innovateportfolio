alphabet = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"

for letter in alphabet:
    print(letter)

def letter_num():
    user_num=input("Please enter a number between 1-26: ")
    user_num=int(user_num)
    user_num -=1
    if user_num >= 0 and user_num <=26:
        print(alphabet[user_num]) #### needs square brackets because indexing
    else:
        print("Please enter a valid number, dumdum!")
        letter_num()
letter_num()



# mylist = [21, 5, 8, 52, 21, 87]
# item = 8

# #search for the item
# index = mylist.index(item)

# print('The index of', item, 'in the list is:', index)