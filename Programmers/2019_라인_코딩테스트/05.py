import itertools

x = 2
y = 1

all_comb = list(itertools.combinations(range(x+y), x))
print(len(all_comb))


