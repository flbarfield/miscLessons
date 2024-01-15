'''exercises from ch8'''

def return_intersection(arr1, arr2):
    '''return intersection of two arrays. Don't use
    the built in methods to do so, and have the complexity
    of O(N)
    '''

    # instant thought of O(n^2 way)
    # intersection = []

    # for i in arr1:
    #     for j in arr2:
    #         if j == i:
    #             intersection.append(j)
    # return intersection

    # ---- O(N) way with hash table ----
    arr1_values = {}
    match_list = []

    for i in arr1:
        arr1_values[i] = True

    for i in arr2:
        try:
            if arr1_values[i] is True:
                match_list.append(i)
        except KeyError:
            continue

    return match_list

print(return_intersection([1,2,3,4,5], [0,2,4,7,8]))
