def print_message(word, invert):
    if word == invert:
        print('la plaabra ${word} es palindroma ')
    else:
        print('la plaabra ${word} no es palindroma')


word = input("Escriba una palabra palidroma : ")
invert_word = word[::-1]
if word.isspace():
    word = word.replace(" ", "")
    invert_word = invert_word.replace(" ", "")
    print_message(word, invert_word)
else:
    print_message(word, invert_word)
