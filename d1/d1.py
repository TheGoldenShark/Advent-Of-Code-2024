with open("input.txt","r") as f: data=f.readlines()
d = [x[:-1].split('   ') for x in data]
d0 = sorted([int(x[0]) for x in d])
d1 = sorted([int(x[1]) for x in d])
sum = 0
for i in range(0, len(d0)):
    sum += abs(d0[i] - d1[i])
print(sum)