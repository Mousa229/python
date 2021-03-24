#In sets all the values need to be unique,and you can't repeat it.

#Create an empty set
s =set()

# add elemnts to the set but you can not repeat them
s.add(1)
s.add(2)
s.add(3)
s.add(3)
s.add(4)
s.remove(2)

print(s)
#if you want to culcuate the length of a set
print(f"This set has {len(s)} elements.")