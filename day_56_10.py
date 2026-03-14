def second_largest(arr):

    largest = arr[0]
    second = -1

    for num in arr:

        if num > largest:
            second = largest
            largest = num

        elif num > second and num != largest:
            second = num

    return second


arr = [10, 20, 4, 45, 99]

print(second_largest(arr))