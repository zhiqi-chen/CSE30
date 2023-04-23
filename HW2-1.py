def check_equal(x, y, msg=None):
    if x != y:
        if msg is None:
            print("Error:")
        else:
            print("Error in", msg, ":")
        print("    Your answer was:", x)
        print("    Correct answer: ", y)
    assert x == y, "%r and %r are different" % (x, y)

def fibonacci_generator():

    number=[]
    i=0
    while (True):
        if i==0:
            n=0
            number.append(n)
            yield n
        elif i==1:
            n=1
            number.append(n)
            yield n
        else:
            n=number[i-1]+number[i-2]
            number.append(n)
            yield n
        i+=1
    
r = []
for n in fibonacci_generator():
    r.append(n)
    if n > 100:
        break
check_equal(r, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])

        
