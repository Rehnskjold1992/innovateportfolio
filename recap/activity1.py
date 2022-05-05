phrase = input("Enter the phrase: ")
correctphrase = "Welcome to Code Nation"
length = len(phrase)


def phrase_checker(string, len):
    if phrase == correctphrase and len(phrase)%2==0:
        print(correctphrase)
        print("The string as an even length")
        print("And the correct phrase!")
        print(f"The length of the string is {len(string)}!")
    # elif phrase != correctphrase and len(phrase)%2!=0:
    #     print("Now you're justbeing silly")
    #     print(len(string))
    else:
        print("The string is an odd length")
        print("That's not the phrase!")
        print(f"The length of the string is {len(string)}!")

phrase_checker(phrase, len)