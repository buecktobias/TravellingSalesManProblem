import itertools
combinations = list(itertools.permutations(["B", "C", "D", "E", "F", "G"], 6))
new_combinations = []
for combination in combinations:
    combination = list(combination)
    combination.insert(0, "A")
    new_combinations.append(combination)

print(new_combinations)
