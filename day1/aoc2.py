with open('day1/input.txt', 'r') as f:
    n1 = []
    n2 = []
    for line in f:
        left, right = line.strip().split()
        n1.append(left)
        n2.append(right)

def frequency_count(my_list):
    element_counts = {}
    for element in my_list:
        element_counts[element] = element_counts.get(element, 0) + 1
    return element_counts

map2 = frequency_count(n2)

sim = []
for s in n1:
    try:
        sim.append( int(s) * int(map2[s]))
    except KeyError:
        sim.append(0)

print(sum(sim))
