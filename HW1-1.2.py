def check_equal(x, y, msg=None):
    if x == y:
        if msg is None:
            print("Success")
        else:
            print(msg, ": Success")
    else:
        if msg is None:
            print("Error:")
        else:
            print("Error in", msg, ":")
        print("    Your answer was:", x)
        print("    Correct answer: ", y)
    assert x == y, "%r and %r are different" % (x, y)

def word_pairs(sentence):
    words=sentence.split()
    result=[]
    number=int(len(words))
    i=0
    k=1
    if number>2 or number==2:
        for n in range(number-1):
            wordlist=(words[i],words[k])
            result.append(wordlist)          
            i+=1
            k+=1
        return result
    return result # My Error: No return
    print(result)

def common_word_pairs(sentence1, sentence2):
    list1=word_pairs(sentence1)
    list2=word_pairs(sentence2)
    result=set(list1)&set(list2)
    return result

s1 = "I love bananas"
s2 = "I love to eat bananas"
s3 = "Nobody truly dislikes to eat bananas"
s4 = "I love to eat anything but bananas"
s5 = "I like mangos more than bananas"

check_equal(common_word_pairs(s1, s2), {("I", "love")})
check_equal(common_word_pairs(s2, s3), {("to", "eat"), ("eat", "bananas")})
check_equal(common_word_pairs(s3, s4), {("to", "eat")})
check_equal(common_word_pairs(s1, s5), set())
