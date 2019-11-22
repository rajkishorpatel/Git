from functools import reduce

l1 = [10,20,30,40,50]
sum = reduce(lambda x,y:x+y, l1)
print(sum)