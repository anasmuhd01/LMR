tup=(1,2,3)
print(type(tup))

tup1=(1)
print(type(tup1)) #--> will return int type 

tup1=(1,)
print(type(tup1))

#PACKING AND UNPACKING IN TUPLE

tup2=(1,2,3,"apple") #--> Packiing 
(p,q,r,w)=tup2 #--> Unpacking
print(p)
print(q)
print(r)
print(w)


