def proteins(strand):
    my_dict = dict(AUG='Methionine', UUU='Phenylalanine',
                   UUC='Phenylalanine', UUA='Leucine', UUG='Leucine',
                   UCU='Serine', UCC='Serine', UCA='Serine',
                   UCG='Serine', UAU='Tyrosine', UAC='Tyrosine',
                   UGU='Cysteine', UGC='Cysteine', UGG='Tryptophan',
                   UAA='STOP', UAG='STOP', UGA='STOP')
    list = []
    i = 0
    while i < len(strand):
        if strand[i:i+3] != 'UAA' and strand[i:i+3] != 'UAG' \
           and strand[i:i+3] != 'UGA':
            list.append(my_dict.get(strand[i:i+3]))
        else:
            break
        i = i+3
    return list
