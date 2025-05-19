def pig_latin(sentence):
    result = []

    for word in sentence.split():
        if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            result.append(word)
        else:
            new_word = word[1:] + word[0] + 'ay'
            result.append(new_word)

    return ' '.join(result)


# Test cases
assert pig_latin("something") == "omethingsay"
assert pig_latin("awesome") == "awesome"
assert pig_latin("latin is a hard language") == "atinlay is a ardhay anguagelay"
assert pig_latin("y") == "yay"
assert pig_latin("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")