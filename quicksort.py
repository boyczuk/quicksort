def quick_sort(s, low, high):
    if low >= high:
        return
    pivot = s[high] # comparison point

    partition = low
    for i in range(low, high):
        if s[i] < pivot:
            s[partition], s[i] = s[i], s[partition]
            partition += 1
    s[partition], s[high] = s[high], s[partition]
    pivot_index = partition

    quick_sort(s, low, pivot_index-1)
    quick_sort(s, pivot_index+1, high)

def main():
    array = [1, 2, 7, 8, 9, 10, 3, 4, 6, 5, 7, 8]

    quick_sort(array, 0, len(array)-1)
    print(array)