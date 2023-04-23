def check_equal(x, y, msg=None):
    if x != y:
        if msg is None:
            print("Error:")
        else:
            print("Error in", msg, ":")
        print("    Your answer was:", x)
        print("    Correct answer: ", y)
    assert x == y, "%r and %r are different" % (x, y)

def combinations(k, elements):
    assert isinstance(elements, list)
    if k==len(elements):
        yield set(elements)
    elif k>len(elements):
        return
    else:
        if k==0:
            yield set()
        else:
            for i in range(len(elements)):
                for p in combinations(k-1,elements[i+1:]):
                    p.add(elements[i])
                    yield p
          
### Basic tests for Combination Generation
# Let us start from some base cases.
L = [1, 2, 3, 4, 5]

# There are no combinations of 5 elements in groups of 6.
n = 0
for c in combinations(6, L):
    n += 1
check_equal(n, 0)


# There is only one combination of 5 elements in groups of 5: the set itself.
n = 0
for c in combinations(5, L):
    check_equal(c, set(L))
    n += 1
check_equal(n, 1)

### Basic tests 2 for Combination Generation
L = [1, 2, 3, 4, 5]

# There is only one combination of 5 elements in groups of 0: the empty set.
n = 0
for c in combinations(0, L):
    check_equal(c, set())
    n += 1
check_equal(n, 1)

### Basic tests 3 for Combination Generation
L = [1, 2, 3, 4, 5]

# There is only one combination of 5 elements in groups of 5: the set itself.
n = 0
for c in combinations(5, L):
    check_equal(c, set(L))
    n += 1
check_equal(n, 1)

### Normal tests for Combination Generator

L = [1, 3, 4, 2, 5]
c2 = combinations(2, L)
c3 = combinations(3, L)
n = 0
ok = False
for c in c2:
    n += 1
    check_equal(len(c), 2)
    if c == {3, 2}:
        ok = True
check_equal(n, 10, msg="n")
check_equal(ok, True, msg="ok")

n = 0
ok = False
for c in c3:
    check_equal(len(c), 3)
    n += 1
    if c == {2, 3, 5}:
        ok = True
check_equal(n, 10)
check_equal(ok, True)
