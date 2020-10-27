# quick sort algorithm notes

example_list = [98,93,100,44,61,53,46,100,63,37,91,90,60,11,74,87,71,58,25,55,56,71,52,89,35]

def partition(arr, low, high):
    pivot_index = low-1 # the -1 handles the case where the pivot is the lowest element
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] < pivot:

            # increment the pivot element index
            pivot_index += 1
            # move the smaller element before the pivot index
            arr[pivot_index], arr[j] = arr[j], arr[pivot_index]
    
    # switches the pivot element with the element in the place for the pivot element
    # the +1 restores the actual index of the pivot element
    arr[pivot_index+1],arr[high] = arr[high],arr[pivot_index+1]

    return pivot_index+1



def quicksort (arr, low, high):

    # this prevents extra loops from running
    if low < high:

        # partitions the array into higher than the pivot and lower than the pivot
        pi = partition(arr, low, high)

        quicksort(example_list, low, pi - 1)
        quicksort(example_list, pi + 1, high)
        
    print(example_list)

quicksort(example_list, 0, len(example_list)-1)