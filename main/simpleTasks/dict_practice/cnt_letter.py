# import pprint
# message = "xkwpoakokropakcposaijijkeirasjodjosjackoawikeiskakcjosdjgakovkpckpoiajvrijfkijkeskocjkisdkkpfkakpkpokspolzkpockszpokwaokeoskapokopxkzopfkeoqkfrpoklpdckxzlkpofloe[pal';flxlkloqell[lwellslpkapodkspkaoiwjriowj"
# count = {}
#
# for character in message:
#
#     # It's doesn't matter that value is set to 0 on every loop session, because if character exist's it will not be replaced.
#     count.setdefault(character, 0)
#
#     count[character] += 1
#
#
# pprint.pprint(count)

# Program created to count words in text

# i will use for loop for string, dictionary and setdefault function for create unique value in dict



import pprint

mess = 'you are amazing amazing you are you you are amazing are you ?'
dict = {}

splitted = mess.split(' ')
print(splitted)

for word in splitted:
    dict.setdefault(word, 0)
    dict[word] = dict[word] + 1

print(dict)


