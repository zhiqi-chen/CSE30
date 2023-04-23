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

check_equal(word_pairs(" "), [])
check_equal(word_pairs("woohoo"), [])
check_equal(word_pairs("I am"), [("I", "am")])

check_equal(word_pairs("I love bananas"), [("I", "love"), ("love", "bananas")])
check_equal(word_pairs("a b c d e"), [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e")])
