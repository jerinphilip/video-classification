

def scanl(f, base, l):
   for x in l:
        base = f(base, x)
        yield base


