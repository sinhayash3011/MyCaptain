E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}


union = E.union(N)
inter = E.intersection(N)
diff = E.difference(N)
sym_dif = E.symmetric_difference(N)


print(f"Union of E and N is {union}")
print(f"Intersection of E and N is {inter}")
print(f"Difference of E and N is {diff}")
print(f"Symmetric difference of E and N is {sym_dif}")
