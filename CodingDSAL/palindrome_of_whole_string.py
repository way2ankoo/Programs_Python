def reverse_sentence(sentence):
    words = sentence.split()

    rev_words = words[::-1]
    rev_sentence = ' '.join(rev_words)
    return rev_sentence


def reverse_word(word):
    word_lis = list(word)
    l = 0
    r = len(word_lis) - 1
    while l < r:
        temp = word_lis[l]
        word_lis[l] = word_lis[r]
        word_lis[r] = temp
        l += 1
        r -= 1
    word = "".join(word_lis)
    return word

def rev_sent(sent):
    words = sent.split()
    rev_word_lis = []
    for word in words:
        rev_word = reverse_word(word)
        rev_word_lis.append(rev_word)
    rev_letters_sent = " ".join(rev_word_lis)
    print(rev_letters_sent)
    result = reverse_word(rev_letters_sent)
    print(result)


sent = "hello how are you"
# print(reverse_sentence(sent))

rev_sent(sent)
