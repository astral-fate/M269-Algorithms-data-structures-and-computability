def mergesort(lst):

    if (len(lst) <= 1):

        return lst

    mid = int(len(lst)/2)

    left = mergesort(lst[:mid])

    right = mergesort(lst[mid:])

    return merge(left, right)

def merge(left, right):

    result = []

    i = 0

    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:

            result.append(left[i])

            i += 1

        else:

            result.append(right[j])

            j += 1

    result += left[i:]

    result += right[j:]

    return result

arr = [9, 1, 345, 2, 8, 4, 22, 7]

print(mergesort(arr))

