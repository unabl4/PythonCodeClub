from elements_count import elements_count

list_one = [1, 3, 5, 7, 9, 11]
list_two = [3, 4, 5, 6, 7]
list_three = [5, 6, 7, 8, 9, 10]
assert elements_count(list_one, list_two, list_three) == {3:1, 5:2, 6:1, 7:2, 9:1}
