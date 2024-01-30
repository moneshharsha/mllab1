def find_intersection(list1, list2):
    intersection_list = []
    for item in list1:
        if item in list2:
            intersection_list.append(item)
    return intersection_list
list1 = [1, 3, 4, 5, 6, 7]
list2 = [2, 5, 7, 8, 9, 1]
intersection_result = find_intersection(list1, list2)
print("Intersection of the two lists:", intersection_result)
