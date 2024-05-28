import random
i = [random.randint(1,100)for i in range(20)]
a = sorted(i[0:10])
b = sorted(i[10:20],reverse = True)
print(" 20 random numbers：",tuple(i))
print("the first 10 elements in ascending：",tuple(a))
print("the last 10 elements in descending：",tuple(b))
