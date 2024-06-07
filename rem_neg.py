def rem_neg(list):
    res = []
    for i in list:
        if i >= 0:
            res.append(i)
    return res

list1 = [12,-7,5,64,-14]
list2 = [12,14,-95,3] 

list1 = rem_neg(list1)
list2 = rem_neg(list2)

print(list1)
print(list2)

