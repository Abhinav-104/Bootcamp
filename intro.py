def ndigits(n):
 return len(str(abs(n)))

def nwords(s):
 l = s.split()
 return len(l)
 
def nsentence(s):
 l = s.count(".") + s.count("!")+s.count("?")
 return l
