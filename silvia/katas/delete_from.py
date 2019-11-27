def delete_from(a_list, *args):
    for arg in args:
        repeated = a_list.count(arg)
        for _ in range(0, repeated):
            a_list.remove(arg)
    return a_list

def good_delete_from(a_list, *args):
    group_result = set(a_list) - set(args)
    return list(group_result)

my_list = [1, 2, 3, 4, 5, 99, 4, 1]
print(delete_from(my_list, 2, 4))
print(good_delete_from(my_list, 2, 4))