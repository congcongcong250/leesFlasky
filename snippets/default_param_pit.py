class Thing:
    def __init__(self, p):
        self.p = [p]

    def add(self, e):
        self.p.append(e)

    def __str__(self):
        return str(self.p)


def hole(s, l=[]):
    l.append(s)
    print(l)


def dict_hole(k, v, d={}):
    d[k] = v
    print(d)
    return d


def obj_hole(e, t=Thing('a')):
    t.add(e)
    print(t)
    return t


def decorate(a):
    def res(b):
        return a+b
    return res
