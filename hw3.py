def print_params(a = 1, b = "строка", c = True):
    print(a, b, c)

print_params()
print_params(a = 10)
print_params(b = "текст", c = False)
print_params(b = 25)
print_params(c = [1, 2, 3])


values_list = [1, "string", True]
values_dict = {"a" : 1, "b" : 2, "c" : 3}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1, "cat"]
print_params(*values_list_2, 42)