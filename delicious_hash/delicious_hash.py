import math,hashlib
def crack_hash(t,c):
 for i in range(10):
  v=(t+str(i))*math.ceil(20/(len(t)+1))
  for y in [v,v.title()]:
   if hashlib.md5(y.encode()).hexdigest() == c:
    return y
