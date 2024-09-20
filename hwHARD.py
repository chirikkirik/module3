def calculate(structure):
    total_sum = 0
    for i in structure:
        if isinstance(i, (int, float)):
            total_sum += i
        elif isinstance(i, str):
            total_sum += len(i)
        elif isinstance(i, (list, tuple, dict, set)):
            if isinstance(i, dict):
                for key, value in i.items():
                    total_sum += calculate([key, value])
            else:
                total_sum += calculate(i)
    return total_sum

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate((data_structure))
print(result)


