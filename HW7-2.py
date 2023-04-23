def check_equal(x, y, msg=None):
    if x != y:
        if msg is None:
            print("Error:")
        else:
            print("Error in", msg, ":")
        print("    Your answer was:", x)
        print("    Correct answer: ", y)
    assert x == y, "%r and %r are different" % (x, y)
    print("Success")

def derivate(e,x):
    if type(e)!=tuple:
        if e==x:
            return 1
        else:
            return 0
    else:
        op,e1,e2=e
        d1=derivate(e1,x)
        d2=derivate(e2,x)
        if op=='+' or op=='-':
            return (op,d1,d2)
        if op=='*' or op=='/':
            if op=='*':
                f1=(op,e2,d1)
                f2=(op,e1,d2) 
                return ('+',f1,f2)
            elif op=='/':
                s1=('*',e2,d1)
                s2=('*',e1,d2)
                f1=('-',s1,s2)
                f2=('*',e2,e2)
                return (op,f1,f2)

check_equal(derivate(3, 'x'), 0)
check_equal(derivate('y', 'x'), 0)
check_equal(derivate('x', 'x'), 1)

check_equal(derivate(('+', 'x', 'x'), 'x'), ('+', 1, 1))
check_equal(derivate(('-', 4, 'x'), 'x'), ('-', 0, 1))
check_equal(derivate(('*', 2, 'x'), 'x'),
             ('+', ('*', 'x', 0), ('*', 2, 1)))
check_equal(derivate(('/', 2, 'x'), 'x'),
             ('/', ('-', ('*', 'x', 0), ('*', 2, 1)), ('*', 'x', 'x')))

e1 = ('*', 'x', 'x')
e2 = ('*', 3, 'x')
num = ('-', e1, e2)
e3 = ('*', 'a', 'x')
den = ('+', e1, e3)
e = ('/', num, den)

f = ('/',
 ('-',
  ('*',
   ('+', ('*', 'x', 'x'), ('*', 'a', 'x')),
   ('-',
    ('+', ('*', 'x', 1), ('*', 'x', 1)),
    ('+', ('*', 'x', 0), ('*', 3, 1)))),
  ('*',
   ('-', ('*', 'x', 'x'), ('*', 3, 'x')),
   ('+',
    ('+', ('*', 'x', 1), ('*', 'x', 1)),
    ('+', ('*', 'x', 0), ('*', 'a', 1))))),
 ('*',
  ('+', ('*', 'x', 'x'), ('*', 'a', 'x')),
  ('+', ('*', 'x', 'x'), ('*', 'a', 'x'))))

check_equal(derivate(e, 'x'), f)
