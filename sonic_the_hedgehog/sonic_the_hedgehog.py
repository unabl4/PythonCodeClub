m={'a':1,'b':1,'d':1,'e':1,'g':1,'o':1,'p':1,'q':1,'A':0,'B':2,'E':0,'G':0,'R':1,'0':1,'6':1,'8':2,'9':1}
def sonic_how_many_rings_did_you_get(i):
    s=0
    for c in i:
        l=c.lower()
        s+=m.get(c, m.get(l,0))
    return s