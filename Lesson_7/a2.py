setx = {"green", "blue"}
sety = {"blue", "yellow"}

print ("Original Set of Elements:")
print (setx)
print (sety)

print ("\nIntersection of two said sets:")
setz = setx.intersection(sety)
print (sety)
a = setx.union(sety)
print (a)
b = setx.difference(sety)
print (b)
c = setx.symmetric_difference(sety)
print (c)