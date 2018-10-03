from sonic_the_hedgehog import sonic_how_many_rings_did_you_get

assert sonic_how_many_rings_did_you_get("a") == 1
assert sonic_how_many_rings_did_you_get("z") == 0
assert sonic_how_many_rings_did_you_get("A") == 0
assert sonic_how_many_rings_did_you_get("B") == 2
assert sonic_how_many_rings_did_you_get("GAG") == 0
assert sonic_how_many_rings_did_you_get("BRB") == 5
# ---
assert sonic_how_many_rings_did_you_get("39007180237") == 6


# 0,1,2,3,4,5,6,7,8,9
# a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z
# A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z