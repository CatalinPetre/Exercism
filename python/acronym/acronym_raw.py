def abbreviate(words):
    words_list = list(words)
    acronym = words_list[0]
    for i in range(len(words_list)):
        if ((words_list[i] == ' ' or words_list[i] == '-' or
                words_list[i] == '_') and words_list[i+1].isalpha()):
            acronym = acronym + words[i+1]
    acronym_up = acronym.upper()
    return acronym_up
