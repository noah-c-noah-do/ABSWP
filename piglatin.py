message = input('Enter the English message to translate into Pig Latin: ')

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y')
pig_latin = []
word_list = message.rstrip('.').split()
for word in word_list:
    if word.startswith(VOWELS):
        if word.islower() and len(word) > 1:
            pig_latin.append(word + "yay")
        elif len(word) == 1:
            pig_latin.append(word + "yay")
        else:
            pig_latin.append(word + "YAY")
    elif word.isalpha():
        if word.islower():
            pig_latin.append(word.lstrip(word[0]) + word[0] + "ay")
        else:
            pig_latin.append(word.lstrip(word[0]) + word[0] + "AY")
    else:
        pig_latin.append(word)
pig_latin[0] = pig_latin[0].capitalize()
print(*pig_latin, sep=" ", end=".")
