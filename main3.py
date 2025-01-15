def calculate_structure_sum(j):
    if isinstance(j,(list, tuple, set)):
        return sum(calculate_structure_sum(item) for item in j)
    elif isinstance(j, dict):
        return sum(calculate_structure_sum(key) for key in j) + sum(calculate_structure_sum(value) for value in j.values())
    elif isinstance(j,str):
        return len(j)
    elif isinstance(j,(int, float)):
        return j
    else:
        return 0

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)