"""
Get a phrase from the user
Split the phrase into a list
Use the first letter of each word to create the acronym
Change the acronym to all caps
Display the acronym on screen


"""







def main():
    phrase = input("Please enter a phrase to convert to an acronym")
    phrase_list = phrase.split()
    acronym = ""
    for word in phrase_list:
        letter = word[0]
        acronym += letter
    print(acronym)


main()
