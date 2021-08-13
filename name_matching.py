def animal_crackers(text):
    wordlist = text.lower().split()
    print(wordlist)
    return wordlist[0][0] == wordlist[1][0]