# Given an input string, reverse the string word by word.

# For example,
#  Given s = "the sky is blue",
#  return "blue is sky the".


def spliter(sentence):
    word = []
    word = sentence.split(' ')
    return word


def trim_space(words):
    temp = []
    for word in words:
        if word == '':
            continue
        else:
            temp.append(word)
    return temp


def reverse_words(words):
    words.reverse()
    return words


def printer(words):
    space = ' '
    words = space.join(words)
    print(words)
    return


if __name__ == '__main__':
    sentence = input('Please input a sentence:\n')
    words = spliter(sentence)
    words = trim_space(words)
    words = reverse_words(words)
    printer(words)
