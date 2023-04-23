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

def compose(f, g):
    d={k:g[v] for (k,v) in f.items() if v in g}
    return d

f = {'cat': 4, 'dog': 4, 'bird': 2, "centipede": 100}
g = {4: "quadruped", 2: "biped"}

check_equal(compose(f, g), {"cat": "quadruped", "dog": "quadruped", "bird": "biped"})

f = {0: 1, 1: 2}
g = {10: 11, 11: 12}
check_equal(compose(f, g), {})
