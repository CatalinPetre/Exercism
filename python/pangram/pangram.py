def is_pangram(sentence):
    if sentence == "":
        return False
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sen_lowercase = sentence.lower()
    sen_list = list(sen_lowercase)
    alpha_list = list(alphabet)
    flag = False
    for i in alpha_list:
        for j in sen_list:
            flag = False
            if i == j:
                sen_list.remove(j)
                flag = True
                break
        if not flag:
            return False
    return True
