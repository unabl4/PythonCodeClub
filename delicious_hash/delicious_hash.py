# https://codeclub.thorgate.eu/challenges/33
import math,hashlib

def crack_hash(thing, correct_hash):
    times = math.ceil(20/(len(t)+1))
    for i in range(10):
        v=(thing+str(i)) * times
        for y in [v,v.title()]:
            if hashlib.md5(y.encode()).hexdigest() == correct_hash:
                return y
