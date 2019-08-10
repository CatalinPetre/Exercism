def is_pangram(sentence):

    if sentence == "":
        return False

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    sen_lowercase = sentence.lower()
    sen_list = list(sen_lowercase)
    alpha_list = list(alphabet)



#test
    #I had to define the flag here because test for empty sentange was failling when flag was defined only in the loop
    # flag = False
    # for i in range(len(alpha_list)):
    #     for j in range(len(sen_list)):
    #         flag = False
    #         if alpha_list[i] == sen_list[j]:
    #             sen_list.remove(sen_list[j])
    #             flag = True
    #             break
    #     if flag == False:
    #         print("Nu e frate")
    #         return False
    # print("Blana")
    # return True

#test

# I should try to set a flag maybe?????
    '''I had to define the flag here because test for 
    empty sentance was failling when flag was defined
    only in the loop'''
    #flag = False
    for i in alpha_list:
        for j in sen_list:
            flag = False
            if i == j:
                sen_list.remove(j)                
                print("They are equal")
                flag = True
                break
        if flag == False:
            print("Nu e frate")
            return False
    print("Blana")
    return True
    
    #     print(alpha_list)
    #     print(sen_list)
    #         #return "False"
    # if flag:
    #     print("it is true")
    #     return True                    
    
    # else:
    #     #print("it is false")
    #     return False    
    #     #return 'True'

#is_pangram("abcdefghijklmnopqrstuvwxyz")
#is_pangram("This is a test")
#is_pangram("")