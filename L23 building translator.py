# here we are trying to build a translator which converts all the vowels to letter 's' in a word that user types in

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation +"G"
            else:
                translation = translation + "g"

        else:
            translation = translation + letter
    return translation

print(translate(input("enter a phrase: ")))