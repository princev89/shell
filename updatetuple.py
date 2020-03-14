t=('a','e','i','o','u')
print("The initial tuple is: ",end='')
print(t)
v1,v2,v3,v4,v5=t
t=v5,v4,v3,v2,v1
print("The updated tuple is: ",end='')
print(t)
