def ndigits(n):
 return len(str(abs(n)))

def nwords(s):
 l = s.split()
 return len(l)
 
def nsentence(s):
 l = s.count(".") + s.count("!")+s.count("?")
 return l

def largest(a,b,c):
 if a>b:
  if a>c:
   return a
  else:
   return c
 elif b>c:
  return b
 else:
  return c

def category(n):
 if n<10:
  return "sub-junior"
 elif n<15:
  return "junior"
 elif n<25:
  return "cadet"
 elif n<35:
  return "senior"
 else:
  return "veteran"

def verify_password():
 secret = "topsecret"
 got = input("Enter password")
 
 while got != secret:
  got = input(Enter password")

 print ("Success")

def average(l):
 count = len(l)
 sum = 0
 for i in l:
  sum += i
 return sum/count

def panagram(s):
 letters = "abcdefghijklmnopqrstuvwxyz"
 for i in letters:
  if i not in s:
   print (i, "is missing")
   return False
 return True

def dumpfile(file):
 f = open(file)
 for i in f:
   print(i)
 f.close()
