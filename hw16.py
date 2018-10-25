a=((),(),('a','b'),('a','b','c'),('d'))
b=set(a)
b.remove(())
print tuple(b)