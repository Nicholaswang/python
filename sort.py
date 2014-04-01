#Randomly generate a list of random integers, put them into a file.
#read the integers from the file, sort and appen the file.
import random
import array
a=array.array('b')
f=open("intefer","wb")
for i in range(1,100):
    a.append(random.randint(0,99))
#z="Before sorting:"
#z.tofile(f)
a.sort()
s=a.tostring()
s.tofile(f)
f.close()

