with open('day1/input.txt', 'r') as f:
    n1 = []
    n2 = []
    for line in f:
        left, right = line.strip().split()
        n1.append(left)
        n2.append(right)

s1 = sorted(n1)
s2 = sorted(n2)

zn = []
for a, b in zip(s1, s2):
    zn.append(abs(int(a)-int(b)))

print(zn[:10])
print(sum(zn))
